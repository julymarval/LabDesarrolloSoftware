# -*- coding: utf-8 -*-

import logging
import time
import datetime


logging.basicConfig(filename="/var/log/LabDdS", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Exceptions:

    INVALID_REQUEST_CODE = 1
    INVALID_REQUEST_MSG = "InvalidRequest"
    INVALID_USER_CODE = 2
    INVALID_USER_MSG = "InvalidUser"
    USER_ALREADY_EXISTS_CODE = 3
    USER_ALREADY_EXISTS_MSG = "UserAlreadyExists"


    INTERNAL_ERROR_MSG = "InternalError"
    INTERNAL_ERROR_CODE = 999


    
    
    def __str__(self):
        return repr(self.msg)

    def getCode(self):
        return self.code

    def getMsg(self):
        return self.msg

