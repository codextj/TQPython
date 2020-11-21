"""
Once you have registered your account through Treasury Quants API 
(see python_example:TQ_example_account_apis.py) and
Installed TQapis package, You can run this script to Test
that everything is working fine for your registered email.
"""

import os, pathlib
from TQapis.TQConnection import Connection, Message
from TQapis.TQRequests import ParamBuilder


class RequestBuilder:
    def make_request(self, param, function_name):
        return ParamBuilder().build(param, function_name)

    def validate_mandatory(self, required_arguments, param):

        missing_arguments = []
        for argument in required_arguments:
            if argument not in param:
                missing_arguments.append(argument)
        if len(missing_arguments) > 0:
            error_message = "Following mandatory arguments are missing:"
            i = 0
            for item in missing_arguments:
                if i > 0:
                    error_message += ", "
                error_message += item
                i += 1
            error_message += "."
            return Message(False, error_message)
        return Message(True, "")


class ValidatorDescribe(RequestBuilder):
    def validate(self, param):
        return Message(True, "")


class ValidatorShowAvailable(RequestBuilder):
    _required_arguments = ["element"]

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorWorkSpace(RequestBuilder):
    def validate(self, param):
        if 'list' in param:
            if param['list'] != 'all':
                return Message(False, "Param should contain {'list':'all'}")
        elif 'delete' in param:
            if param['delete'] == '':
                return Message(False, "key 'delete' had not file name value")
        else:
            return Message(False, "Neither 'list' nor 'delete' found in the param dictionary")
        return Message(True, "")


class ValidatorMarketSwapRates(RequestBuilder):
    _required_arguments = ["asof", "currency"]

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorMarketFXRates(RequestBuilder):
    _required_arguments = ["asof", "to_date", "base_currency"]

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorPriceVanillaSwap(RequestBuilder):
    _required_arguments = [
        "asof"
        , "type"
        , "notional"
        , "trade_date"
        , "trade_maturity"
        , "index_id"
        , "discount_id"
        , "floating_leg_period"
        , "fixed_leg_period"
        , "floating_leg_daycount"
        , "fixed_leg_daycount"
        , "fixed_rate"
        , "is_payer"
        , "spread"
        , "business_day_rule"
        , "business_centres"
        , "spot_lag_days"]

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorPriceFXForward(RequestBuilder):
    _required_arguments = [
        "asof"
        , "type"
        , "trade_date"
        , "trade_expiry"
        , "pay_amount"
        , "pay_currency"
        , "receive_amount"
        , "receive_currency"]

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorPrice(RequestBuilder):
    _required_arguments = ['asof', 'load_as']

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorRiskLadder(RequestBuilder):
    _required_arguments = ['asof', 'load_as']

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorPnLPredict(RequestBuilder):
    _required_arguments = ['load_as', 'from_date', 'to_date']

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorPnLAttribute(RequestBuilder):
    _required_arguments = ['load_as', 'from_date', 'to_date']

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


def delete_file(result_new_file_path):
    try:
        os.remove(result_new_file_path)
    except:
        pass
    return Message(True, "")


def write_unit_file(file_path,section_tag, params, delimiter_char, comment_char):
    try:
        writefile = open(file_path, "w")
        for param in params:
            line = section_tag+"\n"
            writefile.write(line)
            for key, value in param.items():
                line = key + delimiter_char + value + "\n"
                writefile.write(line)
        writefile.write("\n")
        writefile.close()
        return Message(True, "")
    except Exception as e:
        return Message(False, str(e))


def read_unit_file(file_path, section_tag, delimiter, comment):
    params = list()
    param = None
    try:
        line_cntr = 0
        inputfile = open(file_path, "r")
        for line in inputfile:
            # ignore blank lines
            if len(line.lstrip()) == 0:
                line_cntr += 1
                continue
            loc = line.rfind(comment)
            if loc == 0:
                line_cntr += 1
                continue

            #
            # a proper line to process
            #
            if loc > 0:
                line = line[:loc]
            if section_tag in line:
                param = dict()
                params.append(param)
                continue

            if line.find(delimiter)==-1:
                line_cntr += 1
                return Message(False,
                               "Missing delimiter {} in file {} line:{}".format(delimiter, file_path,
                                                                                line_cntr)), params
            tokens = line.split(delimiter)
            tokens[0] = tokens[0].lstrip().rstrip()
            tokens[1] = tokens[1].lstrip().rstrip().replace('"', '')
            if len(tokens[0]) == 0:
                line_cntr += 1
                return Message(False,
                               "Missing delimiter key in key-value pair in file {} line:{}".format(file_path,
                                                                                                   line_cntr)), params
            if len(tokens[1]) == 0:
                line_cntr += 1
                return Message(False,
                               "Missing delimiter value in key-value pair in file {} line:{}".format(file_path,
                                                                                                     line_cntr)), params
            param[tokens[0]] = tokens[1]
            line_cntr += 1
        inputfile.close()
        return Message(True, ""), params
    except Exception as e:
        return Message(False, str(e)), params


class Runner:
    def __init__(self, email,is_post,target_url):
        self.__param_factory = {
            'describe': ValidatorDescribe()
            , 'market_fx_rates': ValidatorMarketFXRates()
            , 'show_available': ValidatorShowAvailable()
            , 'workspace': ValidatorWorkSpace()
            , 'market_swap_rates': ValidatorMarketSwapRates()
            , 'pnl_attribute': ValidatorPnLAttribute()
            , 'pnl_predict': ValidatorPnLPredict()
            , 'price': ValidatorPrice()
            , 'price_fx_forward': ValidatorPriceFXForward()
            , 'price_vanilla_swap': ValidatorPriceVanillaSwap()
            , 'risk_ladder': ValidatorRiskLadder()
        }
        self.connection = Connection(email,is_post,target_url)

    def validate(self, params):
        if 'function_name' not in params:
            return Message(False, "There is no value for the key 'function_name'.")
        function_name = params['function_name']
        if function_name not in self.__param_factory:
            return Message(False, "function_name '" + function_name + "' is not recognised.")
        param_builder = self.__param_factory[function_name]
        message = param_builder.validate(params)
        if not message.is_OK:
            return message
        return Message(True, "")

    def send(self, params):
        function_name = params['function_name']
        param_builder = self.__param_factory[function_name]
        request = param_builder.make_request(params, function_name)

        message = self.connection.send(request)
        return message

    def get_response(self):
        return self.connection.response

    def get_all_unit_file_names(self, root_folder, request_extension):
        file_names = list()
        for root, dirs, files in os.walk(root_folder):
            for filename in files:
                fname, fextension = os.path.splitext(filename)
                if fextension.lower() == "." + request_extension.lower():
                    file_names.append(fname)
        return file_names

    def run(self, root_folder, request_extension='request', result_extension='result',
            result_new_extension='result_new'):
        report = dict()
        test_file_names = self.get_all_unit_file_names(root_folder, request_extension)
        for test_file_name in test_file_names:
            message = self.execute_unit_test(root_folder, test_file_name, request_extension, result_extension,
                                             result_new_extension)
            status_result = "OK"
            if len(message.content) > 0:
                status_result = message.content
            report[test_file_name] = status_result
        return report

    def execute_unit_test(self, root_folder, test_file_name, request_extension="request", result_extension="result", result_new_extension="result_new"):
        delimiter_char = '='
        comment_char = '#'
        test_section_tag = "[test]"
        result_section_tag = "[result]"

        request_file_path = os.path.join(root_folder, test_file_name + "." + request_extension)
        result_file_path = os.path.join(root_folder, test_file_name + "." + result_extension)
        result_new_file_path = os.path.join(root_folder, test_file_name + "." + result_new_extension)

        message, params = read_unit_file(request_file_path,test_section_tag, delimiter_char, comment_char)
        result_news=list()
        if not message.is_OK:
            return message

        for param in params:
            message = self.validate(param)
            if not message.is_OK:
                return message

            message = self.send(param)
            if not message.is_OK:
                return message

            results = self.connection.response.results
            result_news.append(results)
            message = delete_file(result_new_file_path)
            if not message.is_OK:
                return message

        message, base_results = read_unit_file(result_file_path,result_section_tag, delimiter_char, comment_char)
        if (len(base_results) == 0):
            message = write_unit_file(result_file_path,result_section_tag, result_news, delimiter_char, comment_char)
        elif base_results != result_news:
            message = write_unit_file(result_new_file_path,result_section_tag, result_news, delimiter_char, comment_char)
            message.content = "New results generated!"
        return message


def runtestAll(folder,email,is_post, target_url):
    # print(pathlib.Path(__file__).parent.absolute().joinpath("tests_files"))
    runner = Runner(email, is_post, target_url)
    return runner.run(folder)


def run_test_single(root_folder, file_path,email,is_post, target_url):
    # print(pathlib.Path(__file__).parent.absolute().joinpath("tests_files"))
    runner = Runner(email,is_post, target_url)
    status_result = "OK"
    message=runner.execute_unit_test(root_folder,file_path)
    if len(message.content) > 0:
        status_result = message.content
    report={file_path:status_result}
    return report


if __name__ == "__main__":
    email = "shahram_alavian@yahoo.com"
    target_url="http://operations.treasuryquants.com"#<-this is your active email account
    is_post=True#<- True = use POST method and False = use GET method


    single_file_name="unit_pnl_attribute"#<- test a single file for debugging
    folder=pathlib.Path(__file__).parent.absolute().joinpath("tests_files")#<- test all files for reporting'

    #
    # run all the files inside a folder
    #
    # report = runtestAll(folder, email, is_post,target_url)
    
    #
    # run a single test file
    #
    report =  run_test_single(folder,single_file_name,email,is_post,target_url)

    for key, value  in report.items():
        print(key, value)
