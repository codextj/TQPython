# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
import TQRequests
import TQConnection

# API: workspace
# Explanation: It lists all the saved files in your workspace and provides ability to delete any of the saved files.
# Arguments: Run this API as two different configurations:
#            configuration 1: argument: 'listl' value: 'all' (see request_function_workspace_show_files)
#            configuration 1: argument: 'delete' value: <file_id> (see request_function_workspace_delete_file)
#            Note that we have given two different API names (request_function_workspace_show_files and
#            request_function_workspace_delete_file) in this example
#
# About this example: In this example, we first run "workspace_show_files" with no arguments just to get a
#                     list of saved files. We then run "workspace_delete_file" with each file name/id
#                     to delete it.
#
# Notes: if you want to see how to save a file, see the risk example.

connection = TQConnection.Connection()
#
# Check if we have connections
#
request_ip_return = TQRequests.request_ip_return()
message = connection.send(request_ip_return)
if not message.is_ok:
    print(message.is_ok, message.content)
    exit


print("result status:{} cost:{} balance:{} content:{}".format(message.is_ok,connection.cost,connection.balance, message.content))

#
# Get the list of all saved files
#
function_workspace_show_files = TQRequests.request_function_workspace_show_files()
message = connection.send(function_workspace_show_files)

for file_name in message.content:
    print("{}".format(file_name))
print('\n')
#
# Delete all saved files, one-by-one.
#
for file_name in message.content:
    function_workspace_delete_file = TQRequests.request_function_workspace_delete_file(file_name)
    message = connection.send(function_workspace_delete_file)
    print("{}".format(file_name))
print('\n')