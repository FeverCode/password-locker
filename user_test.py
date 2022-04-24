from cgi import test
import unittest
from user import User
from user import Credentials
import pyperclip

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


class TestCresentials(unittest.TestCase):
    '''
    Test case class for defining test cases for credentials
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_credential = Credentials('Space','GiddyLancs', '12345678')
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account,'Space')
        self.assertEqual(self.new_credential.user_name,'GiddyLancs')
        self.assertEqual(self.new_credential.password,'12345678')
        
    def save_credential_test(self):
        '''
         test_save_credential test case to test if the contact object is saved into
         the contact list
        '''
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
        
        
    def test_save_mutiple_credentials(self):
        '''
         test_save_multiple_credential to check if we can save multiple contact
            objects to our contact_list
        '''
        self.new_credential.save_details()
        test_credential = Credentials('Test','TestUser' '123456789')
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def test_delete_credentials(self):
        '''
        test_delete_contact to test if we can remove a contact
        from our credential list
        '''

        self.new_credential.save_details()
        test_credential = Credentials('Test', 'TestUser', '123456789')
        test_credential.save_details()
        
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
        
    def test_find_exists_by_account_name(self):
        '''
         test to check if we can find a credential by account name
        and display information
        '''
        
        self.new_credential.save_details()
        test_credential = Credentials('Test', 'TestUser','123456789')
        test_credential.save_details()
        
        found_credential = Credentials.find_by_account('Space')
        
        self.assertEqual(found_credential.account,test_credential.account)
        
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the credential.
        '''
        self.new_credential.save_details()
        test_credential = Credentials('Test', 'TestUser', '123456789')
        test_credential.saving_details()
        
        credential_exists = Credentials.credential_exist('12345678')
        
        self.assertTrue(credential_exists)
        
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        
        self.assertEqual(Credentials.display_crendtials(), Credentials.credentials_list)
        
    def test_copy_credential(self):
        '''
        Test to confirm that we are copying the credential from a found credentials
        '''
        self.new_credential.save_details()
        Credentials.copy_password('GiddyLancs')
        
        self.assertEqual(self.new_credential.password, pyperclip.paste())
        
           


if __name__ == '__main__':
    unittest.main()


