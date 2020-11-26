"""
Once you have registered your account through Treasury Quants API
(see python_example:TQ_example_account_apis.py) and
Installed TQapis package, You can run this script to Test
that everything is working fine for your registered email.
"""

import os, pathlib

from TQapis.TQUnitTest import run_test_all, run_test_single


if __name__ == "__main__":
    email = "your.email@address.here" #<- this is your active email account
    target_url="http://operations.treasuryquants.com"#<-this is your target url
    #target_url="http://192.168.1.179:8080"
    is_post=False#<- True = use POST method and False = use GET method


    folder="./tests_files"#<- folder in where the file(s) are located

    #
    # run all the files inside a folder
    #
    run_test_all(folder, email, is_post, target_url)

    #
    # run a single test file
    #
    single_file_name="unit_pnl_attribute"#<- test a single file for debugging
    #run_test_single(folder,single_file_name,email,is_post,target_url)
