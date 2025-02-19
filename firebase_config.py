import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("ruta/a/tu/clave.json")
firebase_admin.initialize_app(cred)
