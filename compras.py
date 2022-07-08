from db import dba

class Compras():
    def __init__(self,usuario_id,producto_id):
        self.__ids=0
        self.__usuario_id=usuario_id
        self.__producto_id=producto_id
    
    def get_usuario_id(self):
        return self.__usuario_id
    
    def get_producto_id(self):
        return self.__producto_id
    
    def set_usuario_id(self,usuario_id):
        self.__usuario_id=usuario_id
    
    def set_producto_id(self,producto_id):
        self.__producto_id=producto_id

    def get_id(self):
        return self.__ids
    
    def set_id(self,ids):
        self.__ids=ids
    
    def save(self):
        sql=' insert into Compras (usuario_id, producto_id) values(%s,%s)'
        val=(self.__usuario_id,self.__producto_id)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)