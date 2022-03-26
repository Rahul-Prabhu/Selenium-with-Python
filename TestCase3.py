import unittest

class AppTest(unittest.TestCase):

    @classmethod
    def setUp(self):                            #executed before the start of any method
        print("This is login test")
    @classmethod
    def tearDown(self):                         #executed after the end of any method
        print("This is Tear Down Test")

    @classmethod
    def setUpClass(cls):
        print("Open Application")       #Starts Application

    @classmethod
    def tearDownClass(cls):
        print("Close Application")      #Closes Application

    def test_search(self):
        print("This is Test Search ")
    def test_advancedsearch(self):
        print("This is Advanced search")
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")
    def test_postpaidRecharge(self):
        print("This is Post Paid Recharge")

if __name__=="main":
    unittest.main()