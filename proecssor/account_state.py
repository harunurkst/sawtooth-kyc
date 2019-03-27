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
    def __init__(self, **kwargs):
        self.account_name = kwargs['account_name']
        self.account_type = kwargs['account_type']
        self.account_number = kwargs['account_number']
        self.created_by = kwargs['created_by']
        self.business_type = kwargs['business_type']
        self.fund_source = kwargs['fund_source']
        self.beneficial_owner_info = kwargs['beneficial_owner_info']

        self.passport_number = kwargs.get('passport_number', '')
        self.nid_number = kwargs.get('nid_number', '')
        self.tin_number = kwargs.get('tin_number', '')
        self.vat_reg_number = kwargs.get('vat_reg_number', '')
        self.driving_licence_number = kwargs.get('driving_licence_number', '')

        self.occupation = kwargs['occupation']
        self.comments = kwargs.get('comments', '')

    def to_dict(self):
        return self.__dict__


class AccountState:
    def __init__(self, context):
        self._context = context

    def make_account(self, account_obj):
        """
        Create new account state
        """
        account_address = _make_account_address(account_obj.nid_number)
        LOGGER.info('Got the  account address %s.',
                    account_address)

        state_data = cbor.dumps(account_obj.to_dict())
        addresses = self._context.set_state({account_address: state_data})

        if len(addresses) < 1:
            raise InternalError("State Error")

    # def get_account(self, ac_number):
    #     account_address = _make_account_address(str(account_obj.ac_number))
    #     data = self._context.get_state([account_address])

