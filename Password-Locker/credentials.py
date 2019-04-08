import pyperclip
import string
import random
import string
class Credential:
    '''
    Class to create account credentials,generate password and save their information
    '''
    credentials_list = []

    # @classmethod
    # def check_user(cls,first_name,password):
    #     '''
    #     Method that checks if the name and password entered match entries in the users_list
    #     '''
    #     current_user = ''
    #     for user in User_list:
    #         if(user.first_name == first_name and user.password == password):
    #             current_user = user.first_name
    #
    #     return current_user

    def __init__(self,user_name,account_name,password, confirm_password):
        '''
        Method to define the properties for each user object will hold.
        '''
        self.user_name = user_name
        self.account_name = account_name
        self.site_name =site_name
        self.password = password


    def save_credentials(self):
        '''
        Save_user method saves credentials objects into credentials_list.
        '''
        Credential.credentials_list.append(self)

    def generate_password(size = 8, char = string.ascii_uppercase + string.ascii_lowercase + string.digits):
        '''
        Method to generate an 8 character password for a credential
        '''
        gen_pass = ''.join(random.choice(char)for _ in range(size))
        return generate_password


    @classmethod
    def find_by_site_name(cls,user_name):
        '''
		Method that takes in a sit_name and returns a credential that matches the site_name.
		'''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def display_credentials(cls,user_name):
        '''
        Class method to display list of  credentials saved
        '''
        return cls.user_name


    @classmethod
    def copy_credential(cls,site_name):
        '''
		Class method that copies a credential's info after the credential's site name is entered
		'''
        find_credential = Credential.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)
