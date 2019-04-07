import unittest
from user import User #Importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
      unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
           '''
           Set up method  to create user account before each test cases.
           '''
           self.new_user = User('Pricilla','Gumato','715385641')# create user object

    def test__init__(self):
           '''
           Test  to check if user instances is properly initialized
           '''
           self.assertEqual(self.new_user.first_name,'Pricilla')
           self.assertEqual(self.new_user.last_name,'Gumato')
           self.assertEqual(self.new_user.password,'715385641')
    def test_save_user(self):
        '''
        Test_save_user test case to test if the user object is saved into the  user list
        '''
        self.new_user.save_user()# saving the new user
        self.assertEqual(len(User.users_list),1)

    def tearDown(self):
        '''
        Method to clear the users list after every test
        '''
        User.users_list = []




if __name__ == '__main__':
    unittest.main()
