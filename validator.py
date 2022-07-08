
from db import dba
import base64
from validate_email import validate_email
from dataclasses import asdict

class Validator():
    
    def __init__(self):
        pass
    
    def validar_producto(self,dicc):
        datosFinales={}
        errores={}
        for x,y in dicc.items():
            datosFinales[x]=y.strip()  
        if datosFinales['marca']=='':
            errores['marca']='Campo marca vacio'
            print(errores)
        elif datosFinales['modelo']=='':
            errores['modelo']='Campo modelo vacio'
            print(errores)
        elif datosFinales['proveedor']=='':
            errores['proveedor']='Campo proveedor vacio'
            print(errores)
        elif datosFinales['numero']=='':
            errores['numero']='Campo numero vacio'
            print(errores)
        elif datosFinales['numero'].isdigit()==False:
            errores['numero']='El numero contiene un caracter'
            print(errores)
        elif errores=={}:
            sql='SELECT * FROM celular where numero = %s'
            val=(datosFinales['numero'],)
            dba.get_cursor().execute(sql,val)
            dba.get_conexion().commit
            dba.get_cursor().fetchone()
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['numero']='El numero existe en el sistema'
                print(errores)
            else:
                return True
        else:
            return True
    
    def validar_usuario(self,dicc):
        datosFinales={}
        errores={}
        # caracteresEspeciales=['$','@','#','%']       
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        if datosFinales['nombre']=='':
            errores['nombre']='Campo nombre vacio'
            print(errores)
        if datosFinales['mail']=='':
            errores['mail']='Campo mail vacio'
            print(errores)
        elif validate_email(datosFinales['mail'])==False:
            errores['mail']='No tiene formato de mail'
            print(errores)
        if datosFinales['password']=='':
            errores['password']='Campo password vacio'
            print(errores)
        elif len(datosFinales['password'])<6:
            errores['password']='La password debe tener al menos 6 caracteres'
            print(errores)
        # elif not any(i.isupper() for i in datosFinales['password']):
        #     errores['password']='La password debe tener al menos 1 caracter con mayuscula'
        # elif not any(i.islower() for i in datosFinales['password']):
        #     errores['password']='La password debe tener al menos 1 caracter con minuscula'
        # elif not any(i in caracteresEspeciales  for i in datosFinales['password']):
        #     errores['password']='La password debe tener al menos 1 caracter especial'
        elif datosFinales['password']!=datosFinales['cpassword']:
            errores['password']='la password no coincide'
            print(errores)
        else:
            return True

    def validar_login(self,dicc):
        
        datosFinales={}
        errores={}
        
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        
        sql="select * from usuarios where mail=%s"
        val=(datosFinales['mail'],)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit
        
        result=dba.get_cursor().fetchone()
        
        # print(base64.decodebytes(result[0].encode("UTF-8")).decode('utf-8'))
        
        if result is None:
            errores['mail']="el mail ingresado no existe en la base"
            print(errores)
            return errores
        
        elif base64.decodebytes(result[3].encode("UTF-8")).decode('utf-8')!=datosFinales['password']:
            errores['password']="la password es incorrecta"
            print(errores)
        else:
            return result
        # else:
        #     return True
            
        


vali=Validator()
        
        
            
        
            