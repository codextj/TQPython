# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/

from TQapis import TQRequests, TQConnection

# API: market_fx_rates
# Explanation: It provides the spot and market implied forward FX rates. We use ois curves for calculating the forwards.
# Arguments: Run this API with three arguments: 1) asof date 2) to_date and 2) the base_currency. Set to_date=asof,
#            for spot fx rates.  Set to_date>asof for forward fx rates.
#
# About this example: In this example, we retrieve the (implied fx forward)/ fx spot rates for various currencies.
#


#configuration for this file
user_email="client.email@address.here"
target_url="http://operations.treasuryquants.com"
is_post=False # True = use POST method, False = use GET method


connection = TQConnection.Connection(user_email,is_post,target_url)
#
# Check if we have connections
#
request_ip_return = TQRequests.request_ip_return()
message = connection.send(request_ip_return)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit()


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
        exit()
    print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

print("\n"+"-"*100)
#
# Get the forward FX rates by setting the to_date>asof. Note that we use currency.ois curve to build the forwards
#
to_date = "20211023"  # 1 year forward
for base_currency in currencies:
    request_function_market_fx_rates = TQRequests.request_function_market_fx_rates(asof, to_date, base_currency)
    message = connection.send(request_function_market_fx_rates)
    if not message.is_OK:
        print(message.is_OK, message.content)
        exit()
    print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK,connection.cost,connection.balance, message.content))
