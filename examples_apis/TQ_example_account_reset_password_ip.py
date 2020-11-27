# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/

from TQapis import TQRequests, TQConnection

# API: account_send_activation_key and account_reset
# Explanation:  Two change your password and/or your IP (account reset) with us, you need to use both APIs.
#               This is a two-step process: you first need to ask for an activation key using your email.
#               Once you received your email (check your spam/junk folder), copy the activation key for the second step.
#               There are two situations where you need to reset your account:
#               1) You need to change your password. Password should be at least 10 characters long and should not
#                   include any of the following characters ;<.\{}[]'+"=?&,:
#               2) You need to change your IP. This is because your account is tied to your registered IP. Any
#                   requests arriving from a different IP will be rejected. So the account holder is able to assign an .
#                   IP to a dedicated client.
# Note: For as long as you use the same computer and password, you'll never need to run this API more than once.
# Arguments: account_send_activation_key: uses only the email that it is already registered.
#            account_reset: uses your recent activation key, email, password (new or the same) and IP (new or the same)
#
# About this example: In this example we first run "account_send_activation_key" with an existing email address
#                     We then run "account_reset".
#

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

# Step 1: Ask for an activation key. (Keep below commented out except for when you are asking for an activation key)
#         otherwise, it will invoke a new activation key and renders the previous one invalid.

# request_account_send_activation_key = TQRequests.request_account_send_activation_key(connection.email)
# message = connection.send(request_account_send_activation_key)
# if not message.is_OK:
#     print(message.is_OK, message.content)
#     exit()
# print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

print("\n"+"-"*100)

# Step 2: Use:
# make sure to comment out the previous request. Otherwise, you will be sent another key.
# 1) the activation key sent to your email,
# 2) a same/new password and
# 3) the IP of the computer from which you will initiate your requests
# to reset your account.

# TODO: check length, it should be equal to 54
activation_key = input("Enter/paste the activation key sent to your email: ")

# TODO: enforce password constraints
password = input("Set password: ")

request_account_reset= TQRequests.request_account_reset(activation_key, connection.email, password, connection.source_id)
message = connection.send(request_account_reset)
if not message.is_OK:
    print(message.is_OK, message.content)
    input("press any key to exit().")
    exit()

print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

print("\n"+"-"*100)

