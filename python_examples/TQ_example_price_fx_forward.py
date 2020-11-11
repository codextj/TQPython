# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
import TQRequests
import TQConnection

# API: price_vanilla_swap
# Explanation: It prices a vanilla interest rate swap.
# Arguments: Run this API with following arguments:
#         asof (example '20201022')
#         type (example 'ir_vanilla_swap')
#         notional (example 100000000)
#         trade_date (example '20201022')
#         trade_expiry (example '20201022')
#         pay_currency (example 'gbp')
#         receive_amount (example 1000000)
#         receive_currency (example 'usd')
#
# About this example: In this example, we use the arguments above to price an fx forward.



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
# FX Forward entry
#
market_fx_forward = TQRequests.request_function_price_fx_forward(
    asof=20201022
    , type='fx_forward'
    , trade_date=20201022
    , trade_expiry=20201222
    , pay_amount=1000000
    , pay_currency='gbp'
    , receive_amount=1000000
    , receive_currency='usd'
    # , save_as = 'test_fx_forward.xml' # save_as is optional for if you want to save your trade in your workspace. For example, for risking later on.
)
message = connection.send(market_fx_forward)
print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

