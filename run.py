#!/usr/bin/env python3.8
from enum import auto
from json.tool import main
from user import User
from user import Credentials

def create_new_user(username,password):
    '''
    Function to create new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save new user
    '''
    user.save_user()

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

def authenticate_user(username,password):
    '''
    Function to check if user exists and log them in
    '''
    
    validate_user = Credentials.validate_user(username,password)
    return validate_user

def save_credentials(credentials):
    '''
    Function to add credentials to credential list
    '''
    credentials.save_details()

def display_accounts_details():
    '''
    Function returns all saved credentials
    '''
    return Credentials.display_credentials()

def delete_credentials(credentials):
    '''
    Function deletes credentials from credential list
    '''
    credentials.delete_credentials()
    

def find_credential(account):
    '''
    Function finds credential
    '''
    return Credentials.find_credential(account)


def credential_exists(account):
    '''
    Function that checks if credential exists
    '''
    return Credentials.if_credential_exists(account)

def generate_Password():
    '''
    generate random password
    '''
    auto_password = Credentials.generatePassword()
    return auto_password

def copy_password(account):
    '''
    Function that copies password using pyperclip
    '''
    return Credentials.copyPassword(account)


def main():
    print("Welcome to Password Locker")































    

if __name__ == '__main__':
    
    
    main()
