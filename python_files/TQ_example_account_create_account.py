# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
from TQPython.python_files import TQConnection
from TQPython.python_files import  TQRequests
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

connection = TQConnection.Connection()
#
# Check if we have connections
#
request_ip_return = TQRequests.request_ip_return()
message = connection.send(request_ip_return)
if not message.is_ok:
    print(message.is_ok, message.content)
    exit

# Step 1: Ask for an activation key using you email address. (Keep below commented out except for when you are sking for an activation key)
#         otherwise, it will give an error telling you that the email already exists.

# request_account_create = TQRequests.request_account_create("your.email@address.here")
# message = connection.send(request_account_create)
# if not message.is_ok:
#     print(message.is_ok, message.content)
#     exit
# print("result status:{} cost:{} balance:{} content:{}".format(message.is_ok,connection.cost,connection.balance, message.content))



# Step 2: Use:
# make sure to comment out the previous request. Otherwise, you will be sent another key rendering the recent one invalid.
# 1) the activation key sent to your email,
# 2) a same/new password and
# 3) the IP of the computer from which you will initiate your requests
# to reset your account.

# request_account_reset= TQRequests.request_account_reset('usmgjyq4ujvsdijnsn_9efxmtzisrnscskhtqbrz7wnlyijzr3jniq',connection.email,"EnterYourNewPasswordHere",connection.source_id)
# message = connection.send(request_account_reset)
# if not message.is_ok:
#     print(message.is_ok, message.content)
#     exit
# print("result status:{} cost:{} balance:{} content:{}".format(message.is_ok,connection.cost,connection.balance, message.content))




