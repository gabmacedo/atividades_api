from flask import Flask
from controllers.pessoa_controller import pessoa_bp
from database.db import init_db

app = Flask(__name__)
app.register_blueprint(pessoa_bp)

if __name__ == '__main__':
    init_db()
    app.run(port=5002, debug=True)