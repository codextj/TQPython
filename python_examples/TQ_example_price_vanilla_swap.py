# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/

from TQapis import TQRequests, TQConnection

# API: price_vanilla_swap
# Explanation: It prices a vanilla interest rate swap.
# Arguments: Run this API with following arguments:
#         asof (example '20201022')
#         type (example 'ir_vanilla_swap')
#         notional (example 100000000)
#         trade_date (example '20201022')
#         trade_maturity (example '30Y')
#         index_id (example 'eur.libor6m')                # See show_available api to see the various other options
#         discount_id (example 'eur.ois')                 # See show_available api to see the various other options
#         floating_leg_period (example '6M')
#         fixed_leg_period (example '1y')
#         floating_leg_daycount (example 'act/360')       # See show_available api to see the various other options
#         fixed_leg_daycount (example '30/360')           # See show_available api to see the various other options
#         spread (example 0)
#         fixed_rate (example -0.000032181335)            # You can take this number from the market_swap_rates API
#         is_payer (example False)
#         business_day_rule (example 'modified_following')# See show_available api to see the various other options
#         business_centres (example 'london,target')      # See show_available api to see the various other options
#         spot_lag_days (example 2)
#
# About this example: In this example, we use the arguments above to price a vanilla swap.


connection = TQConnection.Connection(email="your.email@address.here", is_post=False)
#
# Check if we have connections
#
request_ip_return = TQRequests.request_ip_return()
message = connection.send(request_ip_return)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit


#
# Vanilla interest rate swap entry
#
market_swap_rates = TQRequests.request_function_price_vanilla_swap(
        asof='20201022'
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
        #, save_as = 'test_ir_swap' # "save_as" is optional for when you want to save your trade in your workspace. For example, for risking later on.
)
message = connection.send(market_swap_rates)
print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

print("\n"+"-"*100)