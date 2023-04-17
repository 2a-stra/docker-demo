import os
from app import app

APP_PORT = os.environ["APP_PORT"]

if __name__ == "__main__":
    app.run(debug = False, host = "0.0.0.0", port = APP_PORT)
