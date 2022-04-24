##### By FeverCode 
### Password-Locker

## Table of Content

+ [Description](#description)
+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Running Project](#running-project)
+ [Running Tests](#running-tests)
+ [Behaviour Driven Development(BDD)](#behaviour-driven-development-bdd)
+ [Technologies Used](#technologies-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)


## Description
<p>Python application that helps users manage and store their login credentials for different accounts and even generate new passwords for the users.</p>

## Requirements
* python3.8
* pip
* pyperclip
## Installation
* Open Terminal {Ctrl+Alt+T} on ubuntu
* git clone `https://github.com/FeverCode/password-locker`
* cd password-locker
* code . or atom . based on prefered text editor

## Running Project
* On terminal where you have opened the cloned project
    * `$ chmod +x run.py` - to make the projet executable
    * `$ ./run.py` - to run the project

## Running Tests
* To run test for the project
    * `$ python3.8 user_test.py`

## Behaviour Driven Development (BDD)
1. Displays Intro Message to user
   - OUTPUT: "Welcome to Password Locker...Choose one of the following to continue"
2. Enter Short Code
   - INPUT: "cn"
   - OUTPUT: "User_Name" - Prompts User to enter username
   - INPUT: "Giddy"
   - OUTPUT: "Displays options "TYP" - To type your own password and "GEN" - To generate random password
3. Enter Short Code
   - INPUT: "typ" 
   - OUTPUT: "Enter Password" - Prompts user to enter desired password
   - OUTPUT: "Hello Giddy,Account created successfully! Your password is: 1234"
   - INPUT:"gen"
   - OUTPUT:"
4. Enter Short Code
   - INPUT:"ac"
   - OUTPUT:Prompts user to enter usename 
   - INPUT: "Giddy"
   - OUTPUT: Prompts user to enter password
   - OUTPUT: "Use the following short codes:" - Displays short codes used to run the app
5. Enter Short Code
   - INPUT: "cnc"
   - OUTPUT: "Create new credentials" - Prompts user to input Account name
   - INPUT:"Twitter"
   - OUTPUT: "Prompts user to enter Account username"
   - INPUT: "giddy_lancs"
   - OUTPUT: "Display options "TYP" - To type your own password and "GEN" - To generate random password
6. Enter Short Code
   - INPUT: "typ" - Prompts user to enter preferred password
   - INPUT:"1234"
   - OUTPUT: "Account Credential for: Twitter - Username: giddy_lancs - password: 1234 created successfully"
7. Enter Short Code
   - INPUT:"gen"
   - OUTPUT:"Account credential for: Twitter - Username: giddy_lancs - password - Mlb395hlt created successfully"
8. Enter Short Code
   - INPUT: "d"
   - OUTPUT: "Saved Accounts <br>
             Account: Twitter
             Username: giddy_lancs
             Password: Mlb395hlt"
   - OUTPUT: "You have not yet saved any credentials" - Displays if user hasn't created any credentials
9. Enter Short Code
   - INPUT: "FND" - Prompts user to input account name they want to find
   - INPUT: "Twitter"
   - OUTPUT: "Account Name: Twitter <br>
             Username: giddy_lancs password:Mlb395hlt
   - INPUT: "Facebook" - User enter a none existent account name
   - OUTPUT: "Credential doesn't exist"
10. Enter Short Code
   - INPUT: "gen"
   - OUTPUT: "Lw3uVaJ3e* has been generated successfully. Procced to use it in your account"
11. Enter Short Code
    - INPUT: "del" - Prompts user to enter account of the credential they wish to delete
    - INPUT: "Twitter"
    - OUTPUT: "Saved credentials for: Twitter successfully deleted
12. Enter Short Code
    - INPUT: "ext"
    - OUTPUT: "You have successfully exited password locker
13. Enter Short Code
    - INPUT: " User inputs wrong short"
    - OUTPUT: "Invalid short code....Please try again"
 
## Technologies Used
* python3.8

## Licence

MIT License

Copyright (c) [2022] [FeverCode]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Authors Info

LinkedIn - [https://www.linkedin.com/in/gedion-onsongo-112543210/)

Reddit - [https://www.reddit.com/user/stainscode]
   
