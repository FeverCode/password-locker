import unittest
from user import User
from user import Credentials

class TestClass(unittest.TestCase):
    '''
    Test class
    '''
    def setUp(self):
        '''
        method that sets up application
        '''
        self.new_user = User('GiddyLancs','12345678')
        
    def test_init(self):
        '''
        test case initialization is successful
        '''
        self.assertEqual(self.new_user.username, 'GiddyLancs')
        self.assertEqual(self.new_user.password, '12345678')
    
    def test_add_user(self):
        '''
        test case adding user is successful
        '''
        self.new_user.add_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()


