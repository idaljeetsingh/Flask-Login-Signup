"""
    Title: Flask Login/Signup with Email-Verification
    Module Name: backend
    Author: Daljeet Singh Chhabra
    Language: Python
    Date Created: 27-03-2020
    Date Modified: 27-03-2020
    Description:
        ###############################################################
        ##  Controls the backend functionality of server.
        ###############################################################
"""
from proj_constants import MONGO_HOST_URL, MONGO_USER_PWD, MONGO_USER_NAME, MONGO_DATABASE_NAME, salt
from mailer import send_email_verification_mail
from flask import request
import hashlib
import pymongo


def string_hash(text):
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest() + ':' + salt


def register_auth_user(usr_fname, usr_lname, usr_eml, usr_pwd, usr_phone):
    """
        Function to register new user for the system
    :param usr_fname: First name of the user.
    :param usr_lname: Last name of the user.
    :param usr_eml: Email address of the user.
    :param usr_pwd: Password of the user.
    :param usr_phone: Phone number of the user.
    :return: True if registration successful, else False.
    """
    client = pymongo.MongoClient(MONGO_HOST_URL, username=MONGO_USER_NAME, password=MONGO_USER_PWD)
    db = client[MONGO_DATABASE_NAME]

    auth_users_col = db['auth_user']
    if auth_users_col.count_documents({'usr_eml': usr_eml}):
        print(f'User with email {usr_eml} is already created.')
        return False

    hashed_pwd = string_hash(usr_pwd)

    new_user_data = {'usr_fname': usr_fname, 'usr_lname': usr_lname, 'usr_eml': usr_eml, 'usr_pwd': hashed_pwd,
                     'usr_phone': usr_phone, 'is_activated': 'False'}
    ins = auth_users_col.insert_one(new_user_data)

    # Generating a validation key
    key, pkey = string_hash(usr_eml).split(':')

    # Setting the validation key in the DB
    verification_data = {
        'usr_eml': usr_eml,
        'key': key
    }
    verify_usr_eml_col = db['verify_usr_eml']
    ins = verify_usr_eml_col.insert_one(verification_data)
    client.close()
    link = request.host_url + f'verify/{key}'
    # Send Email verification mail
    send_email_verification_mail(usr_eml, usr_fname, link)
    return ins.acknowledged


def check_auth_login(usr_eml, usr_pwd):
    """
        Function to authenticate user's login credentials in the database.
    :param usr_eml: Email address of the user.
    :param usr_pwd: Password of the user.
    :return: True if login successful, else False.
    """
    client = pymongo.MongoClient(MONGO_HOST_URL, username=MONGO_USER_NAME, password=MONGO_USER_PWD)
    db = client[MONGO_DATABASE_NAME]

    auth_users_col = db['auth_user']
    hashed_pwd = string_hash(usr_pwd)
    search_data = {'usr_eml': usr_eml, 'usr_pwd': hashed_pwd}

    res = auth_users_col.count_documents(search_data)
    is_activated = auth_users_col.find_one({'usr_eml': usr_eml}, {'is_activated': 1, '_id': 0})

    if is_activated is None:
        return False
    is_activated = is_activated.get('is_activated')
    client.close()

    if res == 1 and is_activated == 'True':
        # User verification successful
        return True
    else:
        # User verification failed
        return False


def verify_usr_eml(key):
    """
        Function to verify user's email address and activates the account so that user can login to the system.
    :param key: Email address of the user
    :return: Success/Failure
    """
    search_data = {
        'key': key,
    }
    client = pymongo.MongoClient(MONGO_HOST_URL, username=MONGO_USER_NAME, password=MONGO_USER_PWD)
    db = client[MONGO_DATABASE_NAME]

    verify_usr_eml_col = db['verify_usr_eml']
    auth_user_col = db['auth_user']
    res = verify_usr_eml_col.count_documents(search_data)
    if res == 1:
        usr_eml = verify_usr_eml_col.find_one(search_data, {'_id': 0, 'usr_eml': 1}).get('usr_eml')
        user_search_data = {
            'usr_eml': usr_eml
        }
        new_data = {
            'is_activated': 'True'
        }
        auth_user_col.update_one(user_search_data, {"$set": new_data})

        verify_usr_eml_col.delete_one(search_data)
        return f'User verification for {usr_eml} successful!!'
    else:
        return f'User verification failed!!'
