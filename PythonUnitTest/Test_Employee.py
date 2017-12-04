import unittest
from Employee import Employee

class Test_Employee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #Can u used in scenerio where it is costy to connect to database all the time we can set connection and query and store it.
        print("----Setupclass----")

    @classmethod
    def tearDownClass(cls):
        #Once all test are done we are disconnect to database
        print("----Teardownclass----")


    def setUp(self):
        print("Setup")
        #runs befor every testcase, Reduces the redundancy of code
        self.emp1=Employee('gnanadeepika','nadimpalli',750000)
        self.emp2=Employee('harshavikram','kesavareddy',900000)


    def tearDown(self):
        #run after every testcase, Example need to copy file to directory, we can upload in setup and after test is done that can be deleted in tearDown
        print("Tear Down")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email,'gnanadeepika.nadimpalli@email.com')
        self.assertEqual(self.emp2.email,'harshavikram.kesavareddy@email.com')
        self.emp1.last='N'
        self.emp2.last="K"
        self.assertEqual(self.emp1.email,'gnanadeepika.N@email.com')
        self.assertEqual(self.emp2.email,'harshavikram.K@email.com')

    def test_raise_pay(self):
        print("test_raise_pay")
        self.emp1.raise_pay()
        self.emp2.raise_pay()
        self.assertEqual(self.emp1.pay,825000)
        self.assertEqual(self.emp2.pay,990000)

if __name__=="__main__":
    unittest.main()