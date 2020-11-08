import TQRequests
from TQConnection import Connection, Message


class ParamBuilder:
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


# describe
# market_fx_rates
# market_swap_rates
# pnl_attribute
# pnl_predict
# price
# price_fx_forward
# price_vanilla_swap
# risk_ladder
# show_available
# workspace

class ValidatorDescribe(ParamBuilder):
    def validate(self, param):
        return Message(True, "")


class ValidatorShowAvailable(ParamBuilder):
    _required_arguments = ["element"]

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorWorkSpace(ParamBuilder):
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


class ValidatorMarketSwapRates(ParamBuilder):
    _required_arguments = ["asof", "currency"]

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorMarketFXRates(ParamBuilder):
    _required_arguments = ["asof", "to_date", "base_currency"]

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorPriceVanillaSwap(ParamBuilder):
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


class ValidatorPriceFXForward(ParamBuilder):
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


class ValidatorPrice(ParamBuilder):
    _required_arguments = ['asof', 'load_as']

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorRiskLadder(ParamBuilder):
    _required_arguments = ['asof', 'load_as']

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorPnLPredict(ParamBuilder):
    _required_arguments = ['load_as', 'from_date', 'to_date']

    def validate(self, param):
        return self.validate_mandatory(self._required_arguments, param)


class ValidatorPnLAttribute(ParamBuilder):
    _required_arguments = ['load_as', 'from_date', 'to_date']



class Runner:
    def __init__(self, email):
        self.__param_factory = {
            'describe': ValidatorDescribe(),
            'market_fx_rates': ValidatorMarketFXRates(),
            'show_available': ValidatorShowAvailable(),
            'workspace': ValidatorWorkSpace()
        }
        self.connection = Connection(email, True)

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
        message = self.connection.send(params)
        return message

    def get_response(self):
        return self.connection.response
