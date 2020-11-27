# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
from TQapis import TQRequests, TQConnection

# API:
# account_create
# account_send_activation_key
# account_activate
# account_password_change
# account_ip_change
# account_password_reset
#
# Explanation:
# account_create: It created a (disabled) new account. Sends an email to the email with the activation key.
#               If a call-back url argument was populated, the email will also include the url/?email=...&activation_key=...
#
# account_send_activation_key: It resends a new activation key for activating the new account or for resetting a password.
#               If a call-back url argument was populated, the email will also include the url/?email=...&activation_key=...
#
# account_activate: Activates a new (disabled) account
# account_password_change: Changes an existing password
# account_ip_change: Changes the IP from which the requests will be originating.
# account_password_reset: It resets a new password using an activation key. This API will generate an email with an activation key.
#               If a call-back url argument was populated, the email will also include the url/?email=...&activation_key=...
#
# Arguments:
#
# account_create: user_email, user_password, user_ip, callback_url, is_test (True for development, False for production)
# account_send_activation_key: user_email, callback_url,is_test (True for development, False for production)
# account_activate: user_email, activation_key, is_test (True for development, False for production)
# account_password_change:user_email, password, new_password,is_test (True for development, False for production)
# account_ip_change:user_email, password, new_ip, is_test (True for development, False for production)
# account_password_reset:user_email, activation_key, new_password, is_test (True for development, False for production)
#
# About this example:
# These account APIs are meant to cover the minimum set of utilities required to  go through the account life cycle.

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

#############################################################
# account_create: Create a new account using email and password.
#############################################################
#
# It will:
# 1) open a new disabled account
# 2) send an email containing the activation key as well as any (call-back) url that was send. The email will show url/?email=...&activation_token=....
# 3) it returns the activation key.
#

user_ip = '127.0.0.1'  # this is the IP that the client's requests are coming to TQ. This can be changed later
user_password = "user_password"  # this can be changed later
callback_url = ""  # the email will  show url/?email=...&activation_token=....

# For below, True means that account will not be created
# ( or if it is already created no error wil be produced).
is_test = True
# But the rest of the process will be carried out.
# Try to crete an existing account and use that account for this test

request_account_create = TQRequests.request_account_create(user_email, user_password, user_ip, callback_url,
                                                           is_test)
message = connection.send(request_account_create)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit()
print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK, connection.cost, connection.balance,
                                                              message.content))

#############################################################
# account_send_activation_key: Client asks for the activation key to be resent
#############################################################
#
callback_url = ""  # the email will  show url/?email=...&activation_token=....

# For below, True means that account will not be effected
# ( or if it is already created no error wil be produced).
is_test = True
# But the rest of the process will be carried out.
# Try to crete an existing account and use that account for this test

request_account_send_activation_key = TQRequests.request_account_send_activation_key(user_email, callback_url,
                                                                                     is_test)
message = connection.send(request_account_send_activation_key)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit()
print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK, connection.cost, connection.balance,
                                                              message.content))

#############################################################
# account_activate: Client activates 1) directly from this
# API OR 2) via url call back which triggers this API
#############################################################
#

activation_key = "-ctlzzkb4pcj32f_hwgirdsexfgoiyewmhul2jxi4ibgvgdtpyrufq"

# For below, True means that account will not be effected
# ( or if it is already created no error wil be produced).
is_test = "TRUE"
# But the rest of the process will be carried out.
# Try to crete an existing account and use that account for this test

request_account_activate = TQRequests.request_account_activate(user_email, activation_key, is_test)
message = connection.send(request_account_activate)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit()
print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK, connection.cost, connection.balance,
                                                              message.content))

######################################  ACCOUNT MODIFICATION APIs ######################################


#############################################################
# account_password_change: Client changes its password using
# their current password
#############################################################
#
password = "corresponding_password"
new_password = "corresponding_password"  # <-by keeping the same as current we can run this repeatedly.
# For below, True means that account will not be effected
# ( or if it is already created no error wil be produced).
is_test = True
# But the rest of the process will be carried out.
# Try to crete an existing account and use that account for this test

request_account_password_change = TQRequests.request_account_password_change(user_email, password, new_password,
                                                                             is_test)
message = connection.send(request_account_password_change)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit()
print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK, connection.cost, connection.balance,
                                                              message.content))
#############################################################
# account_ip_change: Client changes its IP using
# their current password
#############################################################
#
password = "corresponding_password"
new_ip = "127.0.0.1"  # this is the ip where the requests are originated
# For below, True means that account will not be effected
# ( or if it is already created no error wil be produced).
is_test = True
# But the rest of the process will be carried out.
# Try to crete an existing account and use that account for this test

request_account_ip_change = TQRequests.request_account_ip_change(user_email, password, new_ip, is_test)
message = connection.send(request_account_ip_change)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit()
print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK, connection.cost, connection.balance,
                                                              message.content))

#############################################################
# Password reset
#############################################################

#############################################################
# account_send_activation_key - Step 1: Request for an activation Key.
#############################################################
#
callback_url = ""  # the email will  show url/?email=...&activation_token=....

# For below, True means that account will not be effected
# ( or if it is already created no error wil be produced).
is_test = True
# But the rest of the process will be carried out.
# Try to crete an existing account and use that account for this test

request_account_send_activation_key = TQRequests.request_account_send_activation_key(user_email, callback_url,
                                                                                     is_test)
message = connection.send(request_account_send_activation_key)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit()
print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK, connection.cost, connection.balance,
                                                              message.content))

#############################################################
# account_password_reset - Step 2: use activation key to reset the password.
#############################################################
#
activation_key = "-ctlzzkb4pcj32f_hwgirdsexfgoiyewmhul2jxi4ibgvgdtpyrufq"
new_password = "newpassword"
# For below, True means that account will not be effected
# ( or if it is already created no error wil be produced).
is_test = "TRUE"
# But the rest of the process will be carried out.
# Try to crete an existing account and use that account for this test

request_account_password_reset = TQRequests.request_account_password_reset(user_email, activation_key, new_password,
                                                                           is_test)
message = connection.send(request_account_password_reset)
if not message.is_OK:
    print(message.is_OK, message.content)
    exit()
print("result status:{} cost:{} balance:{} content:{}".format(message.is_OK, connection.cost, connection.balance,
                                                              message.content))
