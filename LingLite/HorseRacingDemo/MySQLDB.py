#!/usr/local/bin/python

# Copyright (c) 2018
# All rights reserved.
# Describe : save data to mysql
# Author   : Butler
# Date     : 2018-08-17

import pymysql



class MySQLDB(object):
    """save data to mysql"""

    def __init__(self, host, port, user, password, dbName, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbName = dbName
        self.charset = charset
        self.connection = None

    def __del__(self):
        if self.connection != None:
            self.connection.close()

    def GetConnection(self):
        if self.connection == None:
            self.connection = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.dbName, charset=self.charset)
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
