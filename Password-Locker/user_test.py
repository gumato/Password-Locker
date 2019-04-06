import unittest # Importing the unittest module
from user import User # Importing the user class


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     
    def setUp(self):
         '''
         method to create user account before each test cases.
         '''
         self.new_user = User('Pricilla','Gumato','715385641')

    def test_init(self):
             '''
             test_init test case to test if the object is initialized properly
             '''
             self.assertEqual(self.new_user.first_name,'Pricilla')
             self.assertEqual(self.new_user.last_name,'Gumato')
             self.assertEqual(self.new_user.password,'715385641')
    def test_save_user(self):
        '''
        test_save_user test case to test if the new users info is saved into the users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)


     

if __name__ == '__main__':
    unittest.main()