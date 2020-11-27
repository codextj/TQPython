# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/

from TQapis import TQRequests, TQConnection

# API: workspace
# Explanation: It lists all the saved files in your workspace and provides ability to delete any of the saved files.
# Arguments: Run this API as two different configurations:
#            configuration 1: argument: 'list' value: 'all' (see request_function_workspace_show_files)
#            configuration 1: argument: 'delete' value: <file_id> (see request_function_workspace_delete_file)
#            Note that we have given two different API names (request_function_workspace_show_files and
#            request_function_workspace_delete_file) in this example
#
# About this example: In this example, we first run "workspace_show_files" with no arguments just to get a
#                     list of saved files. We then run "workspace_delete_file" with each file name/id
#                     to delete it.
#
# Notes: if you want to see how to save a file, see the risk example.

#configuration for this file
user_email="your.email@address.here"
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

print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK, connection.cost, connection.balance,
                                                              message.content))
print("\n"+"-"*100)

#
# Get the list of all saved files
#
function_workspace_show_files = TQRequests.request_function_workspace_show_files()
message = connection.send(function_workspace_show_files)

for file_name in message.content:
    print("{}".format(file_name))

print("\n"+"-"*100)

#
# Delete all saved files, one-by-one.
#
for file_name in message.content:
    function_workspace_delete_file = TQRequests.request_function_workspace_delete_file(file_name)
    message = connection.send(function_workspace_delete_file)
    print("{}".format(file_name))

print("\n"+"-"*100)
