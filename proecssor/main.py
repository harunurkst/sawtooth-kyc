'''
CookieJarTransactionHandler class interfaces for cookiejar Transaction Family.
'''

import traceback
import sys
import hashlib
import logging


from sawtooth_sdk.processor.exceptions import InvalidTransaction
from sawtooth_sdk.processor.core import TransactionProcessor
#from .. import handler
from handler import AccountTransactionHandler


# hard-coded for simplicity (otherwise get the URL from the args in main):
# DEFAULT_URL = 'tcp://localhost:4004'
# For Docker:
DEFAULT_URL = 'tcp://localhost:4004'


FAMILY_NAME = "gkyc"
# TF Prefix is first 6 characters of SHA-512("cookiejar"), a4d219


def _hash(data):
    """Compute the SHA-512 hash and return the result as hex characters."""
    return hashlib.sha512(data).hexdigest()


def main():
    """Entry-point function for the cookiejar Transaction Processor."""
    try:
        # Setup logging for this class.
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

        # Register the Transaction Handler and start it.
        processor = TransactionProcessor(url=DEFAULT_URL)
        sw_namespace = _hash(FAMILY_NAME.encode('utf-8'))[0:6]
        handler = AccountTransactionHandler(sw_namespace)
        processor.add_handler(handler)
        processor.start()
    except KeyboardInterrupt:
        pass
    except SystemExit as err:
        raise err
    except BaseException as err:
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
