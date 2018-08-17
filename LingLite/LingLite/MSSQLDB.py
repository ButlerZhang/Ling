#!/usr/local/bin/python

# Copyright (c) 2018
# All rights reserved.
# Describe : save data to mssql
# Author   : Butler
# Date     : 2018-08-17

import pymssql



class MSSQLDB(object):
    """save data to mssql"""

    def __init__(self, host, user, password, dbName):
        self.host = host
        #self.port = port
        self.user = user
        self.password = password
        self.dbName = dbName
        #self.charset = charset
        self.connection = None

    def __del__(self):
        if self.connection != None:
            self.connection.close()

    def GetConnection(self):
        if self.connection == None:
            self.connection = pymssql.connect(host=self.host,user=self.user,password=self.password,database=self.dbName)
        return self.connection

    def Execute(self, SQLString):
        if self.connection != None:
            self.connection.cursor().execute(SQLString)
            return True
        return False

    def WriteToDB(self, SQLCommand, SQLValue, isPrintSQL=False):
        SQLString = (SQLCommand % SQLValue).encode('utf-8')
        if isPrintSQL:
            print(SQLString)

        if self.connection != None:
            self.connection.cursor().execute(SQLString)
            self.connection.commit()

        return SQLString
