# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pymongo import errors as mongoerrors
import logging
import datetime

from ConstantsModule import *

mongoConstants = MongoConstants()


logging.basicConfig(filename="/var/log/LabDdS", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class DataManager:

    def __init__(self):
		try:

			print ("connecting to mongo....")
			self.mongoClient = MongoClient(mongoConstants.mongoHost, mongoConstants.mongoPort)
			self.db = self.mongoClient.LabDdS

		except Exception as e:
			print(e)
        
    
    def createAccount(self, name, last_name, email, document_id, pwd,school):
		try:
			self.db.insert({})
		except Exception as e:


        return "created account"

    '''
    def findUser(self,email): 

    def updateUser(self):

    def createOrder(self):

    def updateOrder(self):

    def deleteOrder(self):
        '''
        
    