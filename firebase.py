from msilib.schema import AdminExecuteSequence

#Importamos el modulo oficial de firebase
import firebase_admin
#Importamos el modulo credential para pasarle el certificado de firebase(generado)
from firebase_admin import credentials
#importamos el modulo db que nos permite trabajar directamente con las funciones
# de una base de datos
from firebase_admin import db


#Cargamos el certificado del proyecto tomado de firebase realtime database
firebase_sdk = credentials.Certificate('memeteam-226f9-firebase-adminsdk-v9kor-c92ac1dff2.json')

#referenciamos a la base de datos en tiempo real(obtenido desde firebase)
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://memeteam-226f9-default-rtdb.firebaseio.com/'})
'''
#Creamos una categoria(colección) dentro de DB
#ref = db.reference('/UserSocial')
#guardamos los siguientes campos y atributos
#ref.push({'Nombre':'Horacio','Apellido':'Herrera','Sexo':'H','Frase':'Esto es un comentario en la red social',})
'''
'''
#actualiza un dato con referencia directa al hijo en la colección
ref = db.reference('UserSocial')
usuario_ref = ref.child('-NAc6IQyIuheJEeyKH23')
usuario_ref.update({'Frase':'Comentario modificado'})
'''
'''
#nuevo registro de coleccion ya creada, pero asigna nuevo id(subnivel)
ref = db.reference('UserSocial')
usuario_new = {'Nombre':'Elias','Apellido':'Rodriguez','Sexo':'H','Frase':'Esto es un comentario de Elias'}
usuario_ref = ref.push(usuario_new)
'''

#modificando varios usuarios
ref = db.reference('UserSocial')

ref.update({

    #con referencia a la coleccion
    '-NAc6IQyIuheJEeyKH23/Frase':'Esto es un comentario Horacio update',
    '-NAcFkhADlABZAGn4APS/Frase':'Esto es un comentario de Elias update'
})

