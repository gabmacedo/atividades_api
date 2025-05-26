from flask import Flask
from controllers.atividade_controller import atividade_bp
from database.db import init_db

app = Flask(__name__)
app.register_blueprint(atividade_bp)

if __name__ == "__main__":
    init_db()
    app.run(port=5001, debug=True)
