# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
import TQRequests
import TQConnection

# API: market_fx_rates
# Explanation: It provides the spot and market implied forward FX rates. We use ois curves for calculating the forwards.
# Arguments: Run this API with three arguments: 1) asof date 2) to_date and 2) the base_currency. Set to_date=asof,
#            for spot fx rates.  Set to_date>asof for forward fx rates.
#
# About this example: In this example, we retrieve the (implied fx forward)/ fx spot rates for various currencies.
#


connection = TQConnection.Connection()
#
# Check if we have connections
#
request_ip_return = TQRequests.request_ip_return()
message = connection.send(request_ip_return)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit


#
# Markets we currently support
#
currencies = ['chf', 'eur', 'usd', 'gbp', 'jpy']
asof = '20201023'

#
# Get the spot FX by setting the to_date=asof
#
to_date = asof
for base_currency in currencies:
    request_function_market_fx_rates = TQRequests.request_function_market_fx_rates(asof, to_date, base_currency)
    message = connection.send(request_function_market_fx_rates)
    if not message.is_OK:
        print(message.is_OK, message.content)
        exit
    print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

print('\n')
#
# Get the forward FX rates by setting the to_date>asof. Note that we use currency.ois curve to build the forwards
#
to_date = "20211023"  # 1 year forward
for base_currency in currencies:
    request_function_market_fx_rates = TQRequests.request_function_market_fx_rates(asof, to_date, base_currency)
    message = connection.send(request_function_market_fx_rates)
    if not message.is_OK:
        print(message.is_OK, message.content)
        exit
    print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK,connection.cost,connection.balance, message.content))
