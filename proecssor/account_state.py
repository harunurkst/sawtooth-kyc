import logging
import hashlib
import json
import cbor
from sawtooth_sdk.processor.exceptions import InternalError

LOGGER = logging.getLogger(__name__)


FAMILY_NAME = "gkyc"
# TF Prefix is first 6 characters of SHA-512("cookiejar"), a4d219

XO_NAMESPACE = hashlib.sha512('account'.encode("utf-8")).hexdigest()[0:6]


def _make_account_address(name):
    return XO_NAMESPACE + \
        hashlib.sha512(name.encode('utf-8')).hexdigest()[:64]


class Account:
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def to_dict(self):
        return self.__dict__


class AccountState:
    def __init__(self, context):
        self._context = context

    def make_account(self, account_obj):
        """
        Create new account
        """
        account_address = _make_account_address(str(account_obj.account_number))
        LOGGER.info('Got the  account address %s.',
                    account_address)

        state_data = cbor.dumps(account_obj.to_dict())
        addresses = self._context.set_state({account_address: state_data})

        if len(addresses) < 1:
            raise InternalError("State Error")

    # def get_account(self, ac_number):
    #     account_address = _make_account_address(str(account_obj.ac_number))
    #     data = self._context.get_state([account_address])

