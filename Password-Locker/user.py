class User:
    '''
    Class to create user accounts and save their information
    '''
    user_list = []
    def __init__(self,first_name,last_name,password):
        '''
        Method to define the properties for user objects.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

  
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.users_list.append(self)   


  