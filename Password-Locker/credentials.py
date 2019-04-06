class Credentials:
    '''
    Class to create account credentials,generate passwords and save their info
    '''
     credentials_list = []
 def __init__(self,user_name,site_name,account_name,password):
     '''
     Method to define the properties for each user object will hold.
     '''
     self.user_name = user_name
     self.site_name = site_name
     self.account_name = account_name 
     self.password = password
def save_credentials(self):
    '''
    method to save a newly created user instance
    '''
    Credential.credentials_list.append()
