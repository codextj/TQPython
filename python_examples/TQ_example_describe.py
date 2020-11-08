# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
import TQRequests
import TQConnection

# API: describe
# Explanation: It lists and explains the APIs and the arguments that each API expects.
# Arguments: If no argument is given, it provide a list of all APIs available and a description for each. Once a name
#            of the API is passed as the argument, it describes the API and lists the expected argument with
#            a description for each.
#
# About this example: In this example we first run "describe" with no arguments just to get a list of APIs
#                     We then re-run "describe" with each API name to see 1) what the API does and 2) what
#                     arguments we need to run it with.
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
# Get the list of all functions
#
request_function_describe = TQRequests.request_function_describe() #no arguments passed
message_describe = connection.send(request_function_describe)
if not message_describe.is_ok:
    print(message_describe.is_ok, message_describe.content)
    exit
print("result status:{} cost:{} balance:{} content:{}".format(message.is_ok,connection.cost,connection.balance, message.content))

for key, description in message_describe.content.items():
    print("{}: {}".format(key, description))



#
# Get the list of all input arguments for each functions
#
for function_name, description in message_describe.content.items():
    request_function_describe = TQRequests.request_function_describe(function_name)
    message = connection.send(request_function_describe)
    if not message.is_ok:
        print(message.is_ok, message.content)
        exit
    print("Describe:{}".format(function_name)) # pass the name of the API as the argument
    for key, description in message.content.items():
        print("{}: {}".format(key, description))
    print('\n')
