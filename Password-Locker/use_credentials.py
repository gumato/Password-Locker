class User:
    '''
    Class to create user accounts and save their information
    '''
    users_list = []
    def __init__(self,first_name,last_name,password):
        '''
        Method to define the properties for user objects.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


    # def save_user(self):
    #     '''
    #     save_user method saves user objects into user_list
    #     '''
    #     User.users_list.append(self)
class Credentials:
    '''
    Class to create account credentials,generate password and save their information
    '''
    credentials_list = []
    user_credentials_list = []
    @classmethod
    def check_user(cls,first_name,password):
        '''
        Method that check if the name and password entered matches the one of the user_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self,user_name,site_name,account_name,password):
        '''
        Method to define the properties for each user object will hold.
        '''
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    # def save_credentials(self):
    #     '''
    #     Method to save a new instance of user
    #     '''
    #     Credential.credentials_list.append()
