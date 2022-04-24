#!/usr/bin/env python3.8
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
    

