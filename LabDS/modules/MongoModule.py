# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pymongo import errors as mongoerrors
import logging
import datetime

from ConstantsModule import MongoConstants as mConstants

mongoConstants = mConstants()


logging.basicConfig(filename="/var/log/LabDdS", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class DataManager:

	def __init__(self):
		try:
			self.mongoClient = MongoClient(mongoConstants.mongoHost, mongoConstants.mongoPort)
			self.db = self.mongoClient.LabDdS
			self.collection_prof = self.db.profiles

		except Exception as e:
			print(e)
        
    
	def createAccount(self,data):
		try:
			if data["role"] == 'student' or data["role"] == 'admin':
				self.collection_prof.insert_one({mongoConstants.DOCUMENT_FIELD_NAME:data["name"], 
										mongoConstants.DOCUMENT_FIELD_LASTNAME:data["last_name"],
										mongoConstants.DOCUMENT_FIELD_EMAIL:data["email"],
										mongoConstants.DOCUMENT_FIELD_DOCUMENTID:data["document_id"],
										mongoConstants.DOCUMENT_FIELD_SCHOOL:data["school"],
										mongoConstants.DOCUMENT_FIELD_ROLE:data["role"]})
				return True
			else:
				raise 
		except Exception as e:
			#logging.errors("Error - " + e)
			print (e)

	'''def findUser(self,email): 

    def updateUser(self):

    def createOrder(self):

    def updateOrder(self):

    def deleteOrder(self):'''
    
	
        
    