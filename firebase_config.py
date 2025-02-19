import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("D:\JuanM\Downloads\pagina\miweb\config\fb.json")
firebase_admin.initialize_app(cred)
