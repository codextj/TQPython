import TQUnitTest
import TQConfig
from TQConnection import Message
import os



runner = TQUnitTest.Runner(TQConfig.email)
report=runner.run("./tests_files/")
for key, value  in report.items():
    print(key, value)
