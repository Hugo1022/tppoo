
from dataclasses import asdict
from validator import vali
from usuario import Usuario
from compras import Compras
from db import dba


dba.get_cursor().execute("DROP DATABASE if exists eecomerce")
dba.get_conexion().commit()

dba.get_cursor().execute("CREATE DATABASE eecomerce")
dba.get_conexion().commit()

dba.get_cursor().execute("USE eecomerce")
dba.get_conexion().commit()

dba.get_cursor().execute("CREATE TABLE Usuarios (UsuarioID INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nombre VARCHAR (50), mail VARCHAR(50), password VARCHAR(50))")
dba.get_conexion().commit()

dba.get_cursor().execute("CREATE TABLE Productos (ProductoID INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nombre VARCHAR (50), marca VARCHAR(50), precio FLOAT)")
dba.get_conexion().commit()

dba.get_cursor().execute("CREATE TABLE Compras (CompraID INT PRIMARY KEY AUTO_INCREMENT NOT NULL, Usuario_id INT, FOREIGN KEY (Usuario_id) REFERENCES Usuarios(UsuarioID), Producto_id INT, FOREIGN KEY (Producto_id) REFERENCES Productos(ProductoID))")
dba.get_conexion().commit()

sql = "INSERT INTO Productos (nombre, marca, precio) VALUES (%s, %s, %s)"
val = ("TV", "SANYO", 100)
dba.get_cursor().execute(sql, val)
dba.get_conexion().commit()

sql = "INSERT INTO Productos (nombre, marca, precio) VALUES (%s, %s, %s)"
val = ("CELULAR", "IPHONE", 200)
dba.get_cursor().execute(sql, val)
dba.get_conexion().commit()

sql = "INSERT INTO Productos (nombre, marca, precio) VALUES (%s, %s, %s)"
val = ("PC", "APPLE", 300)
dba.get_cursor().execute(sql, val)
dba.get_conexion().commit()

sql = "INSERT INTO Productos (nombre, marca, precio) VALUES (%s, %s, %s)"
val = ("MOUSE", "RAZOR", 50)
dba.get_cursor().execute(sql, val)
dba.get_conexion().commit()

# dba.get_cursor().execute("USE eecomerce")
# dba.get_conexion().commit()

def menu_principal():
    print("Bienvenido a la aplicacion. \n")
    print("Elija una opcion. \n")
    print("1. Registrarse.")
    print("2. Iniciar Sesion.")
    print("3. Salir de la aplicacion.")
    opcion = int(input("Ingrese una opcion. \n"))
    if opcion == 1:
        registro()
    elif opcion == 2:
        login()
    else:
        quit()

def registro():
    usuario={}
    usuario['nombre']=input('Ingrese nombre: \n')
    usuario['mail']=input('Ingrese mail: \n')
    usuario['password']=input('Ingrese password: \n')
    usuario['cpassword']=input('Repita la password: \n')
    if vali.validar_usuario(usuario) == True:
        del usuario['cpassword']
        usuario1=Usuario(**usuario)
        usuario1.save()
        print('Su usuario se agrego exitosamente.')
        return usuario1 and menu_principal()

def login():
    login={}
    login['mail']=input('Ingrese su email: \n')
    login['password']=input('Ingrese su password: \n')
    result = vali.validar_login(login)
    if type(result)==tuple:
        print("El usuario se logeo correctamente.")
        usuario1= Usuario(result[1],result[2],result[3])
        usuario1.set_id(result[0])
        menu_usuario(usuario1)
    else: 
        print(result)

def menu_usuario(usuario1):
    print("Elija una opcion: \n")
    print("1. Modificar datos de usuario.")
    print("2. Comprar un producto.")
    print("3. Cerrar Sesion.")
    print("4. Cerrar la aplicacion.")
    opcion = int(input("Ingrese una opcion. \n"))
    if opcion == 1:
        print("Elija que dato desea modificar.")
        print("1. Editar nombre.")
        print("2. Editar mail.")
        print("3. Editar password.")
        print("4. Eliminar usuario.")
        opcion=int(input("Elija una opcion. \n"))
        if opcion == 1:
            new=input("Ingrese el nuevo nombre: \n")
            usuario1.update_nombre(new)
            print("Su nombre ha sido modificado con exito.")
            menu_usuario(usuario1)
        elif opcion == 2:
            new=input("Ingrese el nuevo mail: \n")
            usuario1.update_mail(new)
            print("Su mail ha sido modificado con exito.")
            menu_usuario(usuario1)
        elif opcion == 3:
            new=input("Ingrese la nueva password: \n")
            usuario1.update_password(new)
            print("Su password ha sido modificado con exito.")
            menu_usuario(usuario1)
        elif opcion== 4:
            sql="delete from usuarios where mail = %s"
            val=(login["mail"],)
            dba.get_cursor().execute(sql,val)
            dba.get_conexion().commit()
            print("El usuario ha sido eliminado con exito.")
            menu_principal()
        else:
            print("La opcion es incorrecta.")
            menu_usuario(usuario1)
    elif opcion == 2:
        dba.get_cursor().execute("select * from productos")
        dba.get_conexion().commit
        result = dba.get_cursor().fetchall()
        for x in result:
            print(x)
        opcion = int(input("Elija un producto: \n"))
        i = False
        while not i == True:
            compras={}
            compras["usuario_id"] = usuario1.get_id()
            compras["producto_id"] = opcion
            compra1=Compras(**compras)
            compra1.save()
            print("Su compra se ha realizado con exito.")
            i = True
            menu_usuario(usuario1)
    elif opcion == 3:
        menu_principal()
    elif opcion ==4:
        quit()
    else:
        print("La opcion es incorrecta.")
        menu_usuario(usuario1)


menu_principal()
