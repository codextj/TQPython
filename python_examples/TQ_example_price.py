# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
import TQRequests
import TQConnection

# API: price
# Explanation: It prices a saved trade.
# Arguments: Run this API with two arguments: 1) asof date and 2) tradeId
#
# About this example: In this example, we first use the API price_vanilla_swap with "save_as" option to save the trade
#                     under a tradeId. We then use the tradeId to call the API price to evaluate the trade for a given
#                     date. At the end, we delete the file to clean up the example.



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
# Step 1 - Price a trade with "save_as" optional argument.
#
tradeId='test_ir_swap'
asof='20201022'

market_swap_rates = TQRequests.request_function_price_vanilla_swap(
        asof=asof
        , type='ir_vanilla_swap'
        , notional=100000000
        , trade_date='20201022'
        , trade_maturity='30Y'
        , index_id='eur.libor6m'                  # See show_available api to see the various other options
        , discount_id='eur.ois'                   # See show_available api to see the various other options
        , floating_leg_period='6M'
        , fixed_leg_period='1y'
        , floating_leg_daycount='act/360'         # See show_available api to see the various other options
        , fixed_leg_daycount='30/360'             # See show_available api to see the various other options
        , spread=0
        , fixed_rate=-0.000032181335              # You can take this number from the market_swap_rates API
        , is_payer=False
        , business_day_rule='modified_following'  # See show_available api to see the various other options
        , business_centres='london,target'        # See show_available api to see the various other options
        , spot_lag_days=2
        , save_as = tradeId # "save_as" is optional for when you want to save your trade in your workspace. For example, for risking later on.
)
message = connection.send(market_swap_rates)
print("result status:{} cost:{} balance:{} content:{}".format(message.is_ok,connection.cost,connection.balance, message.content))

if not message.is_ok:
        exit



#
# Step 2 - Price the trade using only the trade id.
#
request_price = TQRequests.request_function_price(asof, tradeId)
message = connection.send(request_price)
print("result status:{} cost:{} balance:{} content:{}".format(message.is_ok,connection.cost,connection.balance, message.content))


#
# Step 3 - Delete the trade to clean up this example.
#
function_workspace_delete_file = TQRequests.request_function_workspace_delete_file(tradeId)
message = connection.send(function_workspace_delete_file)
print("result status:{} cost:{} balance:{} content:{}".format(message.is_ok,connection.cost,connection.balance, message.content))
