# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/

from TQapis import TQRequests, TQConnection

# API: show_available
# Explanation: It lists and explains various contexts like market data dates, day-count fractions, business rules, etc..
# Arguments: If no argument is given, it provide a list of all context available and a description for each. Once a name
#            of the context is passed as the argument, it lists the options available for that context.
#
# About this example: In this example we first run "show_available" with no arguments just to get a list of contexts
#                     We then re-run "show_available" with each context name to see what options are available.
#

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
# Get the list of selections like market data dates, day-count fractions, business rules, etc.
#
param_describe= TQRequests.request_function_show_available()
message_show_available=connection.send(param_describe)

print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message_show_available.is_OK
                                                              ,connection.cost
                                                              ,connection.balance
                                                              , message_show_available.content))

print("\n"+"-"*100)

for option,description in message_show_available.content.items():
    print("{}: {}".format(option,description))

print("\n"+"-"*100)

#
# get the list of various available options
#
for option_name,description in message_show_available.content.items():
    param_show_available= TQRequests.request_function_show_available(option_name)
    message=connection.send(param_show_available)
    print("Show Available:{}".format(option_name))
    for key,description in message.content.items():
        print("{}: {}".format(key,description))
    print('_'*100)

print("\n"+"-"*100)
