# from tabnanny import check


from typing_extensions import Self


class User:
    '''
    User class for generating new users
    '''
    user_list = []
    
    def __init__(self,username,password):
        '''
        Create method for defining properties of user
        '''
        self.username = username
        self.password = password

    def add_user(self):
        '''
        method for adding a user to the list of users
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list
    
    def delete_user(self):
        '''
        method for deleting a user from the list of users
        '''
        User.user_list.remove(self)

    
class Credentials():
    '''
    class to create new objects of credentials
    '''
    credentials_list = []
    @classmethod
    def verify_user(cls,username,password):
        '''
        method to verify if a user is already in the list
        '''
        check_user = ""
        for user in User.user_list:
            if (user.username == username and user.password == password):
                check_user = user.username
            return check_user
    
    def __init__(self,account,user_name,password):
        '''
        method defining the user credentials to be stored 
        '''
        self.account = account
        self.user_name = user_name
        self.password = password
        
        
    def saving_details(self):
        '''
        method for saving new credentials to the credentials store
        '''
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        '''
        Method that deletes the credentials from the credentials store
        '''
        Credentials.credentials_list.remove(self)
        
    
            
        