# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
import requests
import datetime

from TQPython.python_files import TQConfig, TQResponse, TQRequests


class Message:
    def __init__(self, is_ok, content):
        self.is_ok = is_ok
        if not type(content) is dict:
            Exception("Message was created with an object that was not a dictionary.")
        self.content = content


class Connection:
    def __init__(self, email=TQConfig.email, is_post=TQConfig.is_http_post, url=TQConfig.url, minutes_to_expiry=1):
        self.email = email
        self.url = url
        self.token = ""
        self.expiry = datetime.datetime.now()
        self.cost = 0
        self.balance = 0
        self.client_id = ""
        self.source_id = ""

        self.__minutes_to_expiry = minutes_to_expiry
        #self.__has_been_initialised = False
        self.is_post=is_post




    def send(self, request):
        if self.is_post:
            return self.post(request)
        return self.get(request)

    def post(self, request):
        param_dictionary=request.params
        request_needs_token=request.needs_token
        if request_needs_token:
            # add token here
            now = datetime.datetime.now()
            if (self.expiry - now).total_seconds() / 60 < self.__minutes_to_expiry:
                request_account_token_create = TQRequests.request_account_token_create(self.email)
                message = self.__post(request_account_token_create.params)
                if not message.is_ok:
                    return message
                self.token = list(message.content.values())[0]
            param_dictionary['token'] = self.token
        return self.__post(param_dictionary)

    def get(self, request):
        param_dictionary=request.params
        request_needs_token=request.needs_token
        if request_needs_token:
            # add token here
            now = datetime.datetime.now()
            if (self.expiry - now).total_seconds() / 60 < self.__minutes_to_expiry:
                request_account_token_create = TQRequests.request_account_token_create(self.email)
                message = self.__get(request_account_token_create.params)
                if not message.is_ok:
                    return message
                self.token = list(message.content.values())[0]
            param_dictionary['token'] = self.token
        return self.__get(param_dictionary)


    def __result_to_message(self, result):
        store = TQResponse.Store()
        store.fromXml(result.text)
        self.client_id = store.client_id
        self.source_id = store.source_id  # ip
        self.balance = store.response.balance
        self.cost = store.response.cost
        self.expiry = datetime.datetime.now() + datetime.timedelta(store.response.expiry_minutes * 60)

        if (store.response.errors is None or len(store.response.errors) > 0):
            return Message(False, store.response.errors)
        return Message(True, store.response.results)

    def __post(self, param_dictionary):
        try:
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
            result = requests.post(url=self.url, headers=headers, data=param_dictionary)
            # currently request turns the second post to get. So we post redirect ourselves
            result = requests.post(url=result.url, headers=headers, data=param_dictionary)
            return self.__result_to_message(result)
        except Exception as e:
            self.cost = 0
            errors = dict()
            errors["Error"] = str(e)
            return Message(False, errors)


    def __get(self, param_dictionary):
        result = requests.get(self.url, params=param_dictionary)
        return self.__result_to_message(result)
