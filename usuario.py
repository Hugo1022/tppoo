import base64
from db import dba

class Usuario():
    
    def __init__(self, nombre, mail, password):
        self.__ids=0
        self.__nombre=nombre
        self.__mail=mail
        self.set_password(password)


    def get_id(self):
        return self.__ids

    def set_id(self, ids):
        self.__ids=ids


    def get_nombre(self):
        return self.__nombre
    
    def get_mail(self):
        return self.__mail
    
    def get_password(self):
        return self.__password
    
    def set_nombre(self,nombre):
        self.__nombre=nombre

    def set_mail(self,mail):
        self.__mail=mail

    def set_password(self,password):
        self.__password=self.encriptarPass(password)
    
    def encriptarPass(self, password):
        return base64.encodebytes(bytes(password, 'utf-8')).decode('utf-8')
    
    def desencriptarPass(self,password):
        return base64.decodebytes(password.encode("UTF-8")).decode('utf-8')
    
    def save(self):
        sql='insert into Usuarios (nombre,mail,password) values (%s,%s,%s)'
        val=(self.get_nombre(),self.get_mail(),self.get_password())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)        
    
    def update_nombre(self, nombre):
        sql='update Usuarios set nombre=%s where UsuarioID=%s '
        val=(nombre, self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
    
    def update_mail(self, mail):
        sql='update Usuarios set mail=%s where UsuarioID=%s '
        val=(mail, self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update_password(self,password):
        sql='update Usuarios set password=%s where UsuarioID=%s '
        val=(password,self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    def mostrar_datos_comprador(self):
        sql= "select * from Usuarios where mail=%s"
        val= (self.get_mail())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
