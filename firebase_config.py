import os
import json
import firebase_admin
from firebase_admin import credentials

# Cargar la ruta desde una variable de entorno
firebase_cred_path = os.getenv("FIREBASE_CREDENTIALS")

# Cargar las credenciales desde la variable
if firebase_cred_path and os.path.exists(firebase_cred_path):
    with open(firebase_cred_path) as f:
        cred_data = json.load(f)
    cred = credentials.Certificate(cred_data)
    firebase_admin.initialize_app(cred)
else:
    raise Exception("Las credenciales de Firebase no se encuentran.")
