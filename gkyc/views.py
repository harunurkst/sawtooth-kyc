from django.shortcuts import render
from django.views import View
from account.views import _get_private_keyfile
from client.account_client import AccountClient

KEY_NAME = 'gkyc'
DEFAULT_URL = 'http://localhost:8008'


class SearchMyAccount(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request):
        nid_number = request.POST.get('nid_number')
        privkeyfile = _get_private_keyfile(KEY_NAME)
        client = AccountClient(base_url=DEFAULT_URL, key_file=privkeyfile)
        response = client.check(nid_number)
        print(response)

        return render(request, self.template_name, response)