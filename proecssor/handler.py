import hashlib
import logging
import cbor

from sawtooth_sdk.processor.handler import TransactionHandler
from account_state import Account, AccountState

LOGGER = logging.getLogger(__name__)
FAMILY_NAME = "gkyc"


class AccountTransactionHandler(TransactionHandler):
    '''
    Transaction Processor class for the cookiejar Transaction Family.

    This TP communicates with the Validator using the accept/get/set functions.
    This implements functions to "bake" or "eat" cookies in a cookie jar.
    '''

    def __init__(self, namespace_prefix):
        '''Initialize the transaction handler class.

           This is setting the "cookiejar" TF namespace prefix.
        '''
        self._namespace_prefix = namespace_prefix

    @property
    def family_name(self):
        '''Return Transaction Family name string.'''
        return FAMILY_NAME

    @property
    def family_versions(self):
        '''Return Transaction Family version string.'''
        return ['1.0']

    @property
    def namespaces(self):
        '''Return Transaction Family namespace 6-character prefix.'''
        return [self._namespace_prefix]

    def apply(self, transaction, context):
        '''This implements the apply function for the TransactionHandler class.

           The apply function does most of the work for this class by
           processing a transaction for the cookiejar transaction family.
        '''

        # Get the payload and extract the cookiejar-specific information.
        # It has already been converted from Base64, but needs deserializing.
        # It was serialized with CSV: action, value
        header = transaction.header
        acc_state = AccountState(context)

        content = cbor.loads(transaction.payload)
        action = content.pop("action")
        ac_number = content["account_number"]

        # Get the signer's public key, sent in the header from the client.
        from_key = header.signer_public_key

        # Perform the action.
        LOGGER.info("Action = %s.", action)
        LOGGER.info("Account Number = %s.", ac_number)

        if action == "create":
            account_obj = Account(**content)
            acc_state.make_account(account_obj)
            # self._make_account(context, ac_number, from_key)


        else:
            LOGGER.info("Unhandled action. Action should be create")

