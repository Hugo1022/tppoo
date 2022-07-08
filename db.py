

import mysql.connector

conf={
      'host':'localhost',
      'user':'root',
      'password':''}
    #   'database':'test'}

class DB():
    
    def __init__(self):
        self.__conexion=mysql.connector.Connect(**conf)
        self.__cursor=self.__conexion.cursor()
    
    def get_cursor(self):
        return self.__cursor
    
    def get_conexion(self):
        return self.__conexion

dba=DB()






