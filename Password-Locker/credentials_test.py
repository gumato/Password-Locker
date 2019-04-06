import unittest # Importing unittest module
from credentials import Credentials # Importing credentials class
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
       unittest.TestCase:helps in creating test cases
    '''
    def setUp(self):
      '''
      Method  to create account's credential before each test
      '''
      self.new_credential = Credentials('Gumato','Facebook','gumatopricilla','715385641')

    def test_init(self):
      '''
      Test_init test case to test if the credentials account is initialized properly
      '''
      self.assertEqual(self.new_credential.user_name,'Gumato')
      self.assertEqual(self.new_crddential.site_name,'Facebook')
      self.assertEqual(self.new_credential.account_name,'gumatopricilla')
      self.assertEqual(self.new_credential.password,'715385641')
    def test_save_credentials(self):
        '''
        Test to check if the new credentials info is saved into credentials list
        '''
        self.new_credentials.save_credentials()
        twitter = Credentials('Gumato','Twitter','gumatopricilla','715385641')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)

      




if __name__ == '__main__':
    unittest.main()     
      
      

