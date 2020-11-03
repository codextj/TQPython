# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
from TQPython.python_files import TQConnection, TQRequests

# API: market_swap_rates
# Explanation: It provides the market implied swap rates for various tenors.
# Arguments: Run this API with two arguments: 1) asof date and 2) currency
#
# About this example: In this example, we run the implied swap rates for various currencies.
#


connection = TQConnection.Connection()
#
# Check if we have connections
#
request_ip_return = TQRequests.request_ip_return()
message = connection.send(request_ip_return)
if not message.is_ok:
    print(message.is_ok, message.content)
    exit


#
# Markets we currently support
#
currencies = ['chf', 'eur', 'usd', 'gbp', 'jpy']

#
# Get "implied" swap rates
#
for currency in currencies:
    market_swap_rates = TQRequests.request_function_market_swap_rates('20201023', currency)
    message = connection.send(market_swap_rates)
    print("result status:{} cost:{} balance:{} content:{}".format(message.is_ok,connection.cost,connection.balance, message.content))

