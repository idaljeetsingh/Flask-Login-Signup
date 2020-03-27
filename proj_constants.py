"""
    Title: Flask Login/Signup with Email-Verification
    Module Name: proj_constants
    Author: Daljeet Singh Chhabra
    Language: Python
    Date Created: 27-03-2020
    Date Modified: 27-03-2020
    Description:
        ###############################################################
        ##  Project constants file containing project constants & secrets.
        ###############################################################
"""


# Database Configuration parameters
MONGO_USER_NAME = '<INSERT-YOUR-MONGO-DB-USERNAME-HERE>'
MONGO_USER_PWD = '<INSERT-YOUR-MONGO-DB-PASSWORD-HERE'
MONGO_HOST_URL = '<INSERT-YOUR-MONGO-DB-HOST_URL-HERE>'  # Example: "mongodb+srv://<DB-ID>.mongodb.net" or "mongodb://localhost:27017/"
MONGO_DATABASE_NAME = '<INSERT-MONGO-DB-DATABASE_NAME-HERE>'

# Mailjet Configuration
MAILJET_API_KEY = '<INSERT-YOUR-MAILJET-API_KEY-HERE>'
MAILJET_API_SECRET = '<INSERT-YOUR-MAILJET-API_SECRET-HERE>'
MAILJET_SENDER_EMAIL = '<INSERT-YOUR-MAILJET-EMAIL-HERE>'
MAILJET_SENDER_NAME = '<INSERT-YOUR-NAME-HERE>'

# String Mixer
salt = '<INSERT-SOME-RANDOM_CHARACTERS-HERE>'  # Example: 'owui4ht3uhtl2thloKSFB'
