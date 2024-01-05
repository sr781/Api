"""Entry point to the application"""


import os
from app.factory import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, debug=True)
