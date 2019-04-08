import unittest
import pyperclip
from credentials import Credential # Importing the credentials class
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credeentials class behaviours.

    Args:
      unittest.TestCase: TestCase that helps in creating test cases
    '''

    # def test_check_user(self):
    #     '''
    #     Method to test whether the login method check_user works as expected
    #     '''
    #     self.new_user = Users('Pricilla','Gumato','715385641')
    #     self.new_user.save_user()
    #     user2 = User('Pricilla','Kame','715385641')
    #     user2.save_user()
    #     for user in User.users_list:
    #         if user.first_name == user2.first_name and user.password == user2.password:
    #             current_user = user.first_name
    #     return current_user
    #
    #     self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))
    def setUp(self):
            '''
            Method to create credentials account before each test
            '''
            self.new_credential = Credential('Pricilla','gumatopricilla','Facebook','715385641')
    def test_init(self):
            '''
            Test to check if credential instances is properly initialized
            '''

            self.assertEqual(self.new_credential.user_name,'Pricilla')
            self.assertEqual(self.new_credential.site_name,'gumatopricilla')
            self.assertEqual(self.new_credential.account_name,'Facebook')
            self.assertEqual(self.new_credential.password,'715385641')



   def test_save_credentials(self):
		   '''
		    Test to check if the new credential info is saved into the credentials list
		    '''
		    self.new_credential.save_credentials()
		    twitter = Credential('twitter','user','gumatopricilla','715385641')
		    twitter.save_credentials()
		    self.assertEqual(len(Credential.credentials_list),2)




   def tearDown(self):
            '''
            Method to clear the credentials list after every test
            '''
            Credential.credentials_list = []

     def test_display_credentials(self):
         '''
         Test to check if the display_credentials method, displays the correct credentials.
         '''
         self.new_credential.save_credentials()
         twitter= Credential('Pricilla','Twitter','gumatopricilla','715385641')
         twitter.save_credentials()
         self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

     def test_find_by_user_name(self):
		'''
		Test to check if the find_by_user_name method returns the correct credential
		'''
		self.new_credential.save_credentials()
		twitter= Credential('Pricilla','Twitter','gumatopricilla','715385641')
		twitter.save_credentials()
		credential_exists = Credential.find_by_user_name('Twitter')
		self.assertEqual(credential_exists,twitter)

     def test_copy_credential(self):
         '''
         Test to check if copy credential method copies the correct credential
         '''
         self.new_credential.save_credentials()
         twitter = Credential('Pricilla','Twitter','gumatopricilla','715385641')
         twitter.save_credentials()
         find_credential = None
         for credential in Credential.user_credentials_list:
             find_credential = Credential.find_by_user_name(credential.user_name)
             return pyperclip.copy(find_credential.password)
         Credential.copy_credential(self.new_credential.user_name)
         self.assertEqual('715385641',pyperclip.paste())
         print(pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
