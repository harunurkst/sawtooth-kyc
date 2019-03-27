from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import argparse
import logging
import os
import sys
import traceback
import yaml

from colorlog import ColoredFormatter
from client.account_client import AccountClient
from .serializers import AccountSerializer

KEY_NAME = 'gkyc'

# hard-coded for simplicity (otherwise get the URL from the args in main):
# DEFAULT_URL = 'http://localhost:8008'
# For Docker:
DEFAULT_URL = 'http://localhost:8008'


def create_console_handler(verbose_level):
    '''Setup console logging.'''
    del verbose_level  # unused
    clog = logging.StreamHandler()
    formatter = ColoredFormatter(
        "%(log_color)s[%(asctime)s %(levelname)-8s%(module)s]%(reset)s "
        "%(white)s%(message)s",
        datefmt="%H:%M:%S",
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        })

    clog.setFormatter(formatter)
    clog.setLevel(logging.DEBUG)
    return clog


def setup_loggers(verbose_level):
    '''Setup logging.'''
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(create_console_handler(verbose_level))


def _get_private_keyfile(key_name):
    '''Get the private key for key_name.'''
    home = os.path.expanduser("~")
    key_dir = os.path.join(home, ".sawtooth", "keys")
    return '{}/{}.priv'.format(key_dir, key_name)


class CreateAccount(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            v_data = serializer.validated_data
            v_data["action"] = "create"

            priv_key_file = _get_private_keyfile(KEY_NAME)
            client = AccountClient(base_url=DEFAULT_URL, key_file=priv_key_file)

            response = client.create(**v_data)
            status = yaml.safe_load(response)['data'][0]['status']
            return Response({"data": status})
        return Response(serializer.errors)


class CheckAccount(APIView):
    def get(self, request, account_number):
        privkeyfile = _get_private_keyfile(KEY_NAME)
        client = AccountClient(base_url=DEFAULT_URL, key_file=privkeyfile)
        response = client.check(account_number)
        print(response)
        return Response(response)

