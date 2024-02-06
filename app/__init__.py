
from flask import Flask

#crea el objeto principal
app = Flask (__name__)

from app import routes

#llamar las rutas definidas
if __name__ == "__main__":
    app.run()