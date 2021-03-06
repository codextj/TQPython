"""
Handles Treasury Quants API Call
- GET
- POST

GitHub Description:
    This is the connection class that contains the HTTP protocol as well as the running acount balance, etc..
"""

# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/

import requests
import datetime
from TQapis import TQResponse, TQRequests


class Message:
    def __init__(self, is_OK, content):
        """
        Initializes Message Class object.

        Args:
            is_OK: Type[bool], False <- Response Error | True <- Response Result.
            content: Type[dict].

        Raises:
            Exception: Message was created with an object that was not a dictionary. 
        """
        self.is_OK = is_OK
        if not type(content) is dict:
            Exception("Message was created with an object that was not a dictionary.")
        self.content = content


class Connection:
    def __init__(self, email, is_post, url, minutes_to_expiry=1):
        """
        Initializes Connection Class object.

        Args:
            email: Type[str], provide something@domain.com (default <- TQConfig.email).
            is_post: Type[bool], provide True to use POST or False to use GET (default <- TQConfig.is_http_post).  
            url: Type[str], provide TQ api url (default <- TQConfig.url).
            minutes_to_expiry: Type[int], (default = 1).

        Attributes:
            email, is_post, url, minutes_to_expiry,
            token, expiry, cost, balance, client_id, source_id, 
        """
        self.response = TQResponse.Response()
        self.email = email
        self.url = url
        self.token = ""
        self.expiry = datetime.datetime.now()
        self.cost = 0
        self.balance = 0
        self.client_id = ""
        self.source_id = ""
        self.__minutes_to_expiry = minutes_to_expiry
        # self.__has_been_initialised = False
        self.is_post = is_post

    def send(self, request):
        """
        Uses [is_post] attribute of Connection Object to determine
        whether to do a GET request or POST request.

        Args:
            request: Type[Request], Note: Request is `TQ` class not `requests` package class.
                     Attribute:
                        params: Type[dict], have key `function_name`
                        needs_token: Type[bool]
        """
        if self.is_post:
            return self.post(request)
        return self.get(request)

    def post(self, request):
        """
        Pre-Check before sending POST request
        - checks if token is needed
            -- generate token, if previous token expired 
        """
        param_dictionary = request.params
        request_needs_token = request.needs_token
        if request_needs_token:
            # add token here
            now = datetime.datetime.now()
            if (self.expiry - now).total_seconds() / 60 < self.__minutes_to_expiry:
                request_account_token_create = TQRequests.request_account_token_create(self.email)
                message = self.__post(request_account_token_create.params)
                if not message.is_OK:
                    return message
                self.token = list(message.content.values())[0]
            param_dictionary['token'] = self.token
        return self.__post(param_dictionary)

    def get(self, request):
        """
        Pre-Check before sending GET request
        - checks if token is needed
            -- generate token, if previous token expired 
        """
        param_dictionary = request.params
        request_needs_token = request.needs_token
        if request_needs_token:
            # add token here
            now = datetime.datetime.now()
            if (self.expiry - now).total_seconds() / 60 < self.__minutes_to_expiry:
                request_account_token_create = TQRequests.request_account_token_create(self.email)
                message = self.__get(request_account_token_create.params)
                if not message.is_OK:
                    return message
                self.token = list(message.content.values())[0]
            param_dictionary['token'] = self.token
        return self.__get(param_dictionary)

    def __result_to_message(self, result):
        """
        Triggers parsing of GET/POST response &
        From parsing result, Updates Attribute (clint_id, source_id, balance, cost, expiry)

        Args:
            result: Type[requests HTTP Response Object]
        
        Returns:
            Type[TQ Message], Message Object with Store Response (Error or Results)
        """
        store = TQResponse.Store()
        store.fromXml(result.text)
        self.client_id = store.client_id
        self.source_id = store.source_id  # ip
        self.balance = store.response.balance
        self.cost = store.response.cost
        self.expiry = datetime.datetime.now() + datetime.timedelta(store.response.expiry_minutes * 60)
        self.response = store.response

        if (store.response.errors is None or len(store.response.errors) > 0):
            return Message(False, store.response.errors)
        return Message(True, store.response.results)

    def __post(self, param_dictionary):
        """
        Perform Actual POST Request

        Args:
            param_dictionary: Type[dict], contains `function_name`, `token`(optional)

        Returns:
            requests HTTP Response Object
        """
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
        """
        Perform Actual GET Request

        Args:
            param_dictionary: Type[dict], contains `function_name`, `token`(optional)

        Returns:
            requests HTTP Response Object
        """
        result = requests.get(self.url, params=param_dictionary)
        return self.__result_to_message(result)
