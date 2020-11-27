<p><img src="https://github.com/treasuryquants/examples/raw/main/assets/MainPic2.png" width="1100"></p>

***
# Python API Examples
This branch is a set of examples and unit_tests in python to help you get up and running quickly.
 
Before you start, the most important step is to ensure that you have an account. This is where most people get into issues. Contrary to most websites, you create your account using the API themselves. So all you need to open your account are these APIs, themselves. Just head straight to *TQ_example_account_create_account.py* to open your new account.

## Open Your New Account
If you do not have an account with us already, You need to open a new one.

You have two options:
1) You can use our Excel example from https://github.com/treasuryquants/TQExcel to open an account yourself following the instruction.
2) You email us (contact@treasuryquants.com) your public IP address of the machine you will be using, we will open an account for you. You will receive an email when it is done. Here is a link to help you with your IP address (https://www.showmyip.com).

Armed with an active account we are now ready to get started. 

## Install TQapis

Before running any code you need to install **TQapis** package:

    pip install TQapis

You can see more information about this package at https://pypi.org/project/TQapis

Next, download/clone the python code from here.


## Running the Examples 
You are now ready to run each of the examples separately.

At the top of each example you can see the following statement:

    user_email="client.email@address.here"

Replace the quotation with your email instead and run the example.

 
## Getting Around the Python Files

Here is a list of examples and a brief explanation of what they are.


| Files | Description |
| ------ | ----------- |
| TQ_example_account_create_apis.py    | Shows the apis necessary to develop the account life cycle.  |
| TQ_example_describe.py    | Shows the way to list all our API functions and how to run them.|
| TQ_example_market_fx_rates.py    | Shows the steps of generating market spot FX and forward implied FX rates for a given date. |
| TQ_example_market_swap_rates.py | Shows the steps of generating market implied swap rates for a given date.|
| TQ_example_market_price.py | Shows the steps of pricing a save trade for a given date.|
| TQ_example_market_price_fx_forward.py | Shows the steps of pricing an fx forward for a given date.|
| TQ_example_market_price_vanilla_swap.py | Shows the steps of pricing a vanilla swap for a given date.|
| TQ_example_market_risk_ladder.py | Shows the steps of calculating the ladder sensitivities of a saved trade for a given date.|
| TQ_example_market_pnl_predict.py | Shows the steps of calculating the pnl predict of a saved trade between two dates.|
| TQ_example_market_pnl_attribute.py | Shows the steps of calculating the pnl attribute of a saved trade between two dates.|
| TQ_example_show_available.py | Shows list of all options available for each input data like business centers, day-count basis, etc.|
| TQ_example_workspace.py | Shows list of all the saved file and delete the one you ask.|
| TQ_example_unit_test.py | Shows how you can run unit tests. Files are split as *.request and *.response. Use them a template. Take a look at each set and you can create many more. |

<a name="what_can_we_do_better"></a>
## What can we do better?
Any comments, feedback, question? just drop us a line.

<p align="left"><a href="https://treasuryquants.com/"> <img src="https://github.com/treasuryquants/examples/raw/main/assets/logoBlackSmall.png" width="300">
<p align="left">
Email: <a href="mailto:contact@treasuryquants.com">contact@treasuryquants.com</a><br>
Website: <a href="https://treasuryquants.com/" target="_blank">TreasuryQuants.com</a><br>
<p align="left"><a href="https://www.linkedin.com/company/treasury-quants/"><img src="https://github.com/treasuryquants/examples/raw/main/assets/linkedIn.png" width="35"></a></p>
