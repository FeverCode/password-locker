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