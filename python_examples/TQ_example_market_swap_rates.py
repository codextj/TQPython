# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/

from TQapis import TQRequests, TQConnection

# API: market_swap_rates
# Explanation: It provides the market implied swap rates for various tenors.
# Arguments: Run this API with two arguments: 1) asof date and 2) currency
#
# About this example: In this example, we run the implied swap rates for various currencies.
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

#
# Get "implied" swap rates
#
for currency in currencies:
    market_swap_rates = TQRequests.request_function_market_swap_rates('20201023', currency)
    message = connection.send(market_swap_rates)
    print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK,connection.cost,connection.balance, message.content))
    print('_'*100)
    
print("\n"+"-"*100)