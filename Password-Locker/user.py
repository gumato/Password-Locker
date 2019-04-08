class User:
    '''
    Class to create user accounts and save their information
    '''
    users_list = []
    def __init__(self,first_name,last_name,password):
        '''
        Method to define the properties for user object.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    def save_user(self):
        '''
        Save_user method saves user objects into user_list.
        '''
        User.users_list.append(self)

    @classmethod
    def check_user(cls,password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        for user in cls.users_list:
            if user.password == password:
                return True

        return False
