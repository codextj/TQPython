"""
Contains configuration
    email : user_email_id
    url : http://operations.treasuryquants.com/
    is_http_post : Type [boolean], it determines whether to use POST or GET

GitHub Description:
    Keeps configuration parameters that later on can be passed on from the argument line when you write your program.
"""

# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
email = "shahram_alavian@yahoo.com"
url = "http://operations.treasuryquants.com/"

# False=Get and True=Post #many users try these examples from behind firewall. So Get is the only
# method that works.
is_http_post=False
