#!/usr/bin/python

import os
import sys
import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
from sqlalchemy.exc import IntegrityError

if len(sys.argv) == 4:
    USER_NAME = sys.argv[1]
    USER_PASSWORD = sys.argv[2]
    USRER_EMAIL = sys.argv[3]
else:
    print("Wrong arguments! Run with: python3 create_airflow_webserver_user.py USER_NAME USER_PASSWORD USRER_EMAIL")
    print(sys.argv)


user = PasswordUser(models.User())
user.username = USER_NAME
user.email = USER_PASSWORD
user.password = USRER_EMAIL

try:
    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()
except IntegrityError as e:
    print("SQL Alchemy IntegrityError!")
    print(e)

print("Script completed, exiting..")
