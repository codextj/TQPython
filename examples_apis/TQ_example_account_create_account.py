# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/

from TQapis import TQRequests, TQConnection

# API: account_create and account_reset
# Explanation:  Creation of a new account is a two-step process:
#               1) you first need to ask for an activation key using your email address. An email with a new activation
#                key will be sent to your email address (check your spam/junk/inbox folders). Copy the activation key.
#               2) Then, you need to set your password and ip using that activation key that you have just copied.
#
# Arguments: account_create: uses a new email address.
#            account_reset: uses your recent activation key, email, new password and your IP
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
    input("press any key to exit()")
    exit()

# Step 1: Ask for an activation key using you email address. (Keep below commented out except for when you are asking for an activation key)
#         otherwise, it will give an error telling you that the email already exists.

connection.email=input("Enter your email address: ")
request_account_create = TQRequests.request_account_create(connection.email)
message = connection.send(request_account_create)
if not message.is_OK:
    print(message.is_OK, message.content)
    input("press any key to exit()")
    exit()

print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

print("\n"+"-"*100)

# Step 2: Use:
# If you have already received an activation key make sure to comment out the previous request.
# Otherwise, you will be sent another key rendering the recent one invalid.
# 1) the activation key sent to your email,
# 2) a same/new password and
# 3) the IP of the computer from which you will initiate your requests
# to reset your account.

# [not_important] TODO: check length, it should be equal to 54
activation_key = input("Enter/paste the activation key sent to your email: ")

# [not_important] TODO: enforce password constraints
password = input("Set password: ")

request_account_reset= TQRequests.request_account_reset(activation_key, connection.email, password, connection.source_id)
message = connection.send(request_account_reset)
if not message.is_OK:
    print(message.is_OK, message.content)
    input("press any key to exit()")
    exit()

print("\nresult status:{}\ncost:{}\nbalance:{}\ncontent:{}".format(message.is_OK,connection.cost,connection.balance, message.content))

print("\n"+"-"*100)
