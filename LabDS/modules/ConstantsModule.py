# -*- coding: utf-8 -*-

import datetime

def constant(f):
    """docstring for getter and setter"""

    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)

class MongoConstants:

    #construct
    def __init__(self):
        
        self.mongoHost = "localhost"
        self.mongoPort = 27017

        self.DATABASE = "LabDdS"
        self.COLLECTION_PROFILES = "profiles"
        self.COLLECTION_BOOKS = "books"
        self.COLLECTION_STATUS =  "status"

        self.DOCUMENT_FIELD_EMAIL = "email"
        self.DOCUMENT_FIELD_DOCUMENTID = "documentId"
        self.DOCUMENT_FIELD_ROLE = "role"
        self.DOCUMENT_FIELD_NAME = "name"
        self.DOCUMENT_FIELD_LASTNAME = "lastName"
        self.DOCUMENT_FIELD_SCHOOL = "school"
        self.DOCUMENT_FIELD_PWD = "pwd"


        self.MONGO_OPERATOR_OR = "$or"
        self.MONGO_OPERATOR_GREATER_THAN = "$gt"
        self.MONGO_OPERATOR_PUSH = "$push"
        self.MONGO_OPERATOR_SET = "$set"


class MessagesConstants:

    #construct
    def __init__(self):
        