# -*- coding: utf-8 -*-

import logging
import time
import datetime

from DsSExceptionsModule import Exceptions as exception
from ConstantsModule import *


logging.basicConfig(filename="/var/log/LabDdS", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def constant(f):
    """docstring for getter and setter"""

    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)



class Util:

    def __init__(self):
        self.DdSExceptions = exception()
        self.DATE_YEAR_MONTH_DAY_FORMAT = "%Y-%m-%d %H:%M:%S"

    
    def stringToDate(self, strDate):
        try:
            return datetime.datetime.strptime(strDate, self.DATE_YEAR_MONTH_DAY_FORMAT)
        except Exception as e:  
            raise DdSExceptions(DdSExceptions.INTERNAL_ERROR_CODE,
                                   DdSExceptions.INTERNAL_ERROR_MSG)
