import os
import yaml
import traceback
from flask import Flask, request, jsonify
from sqlalchemy import text
from app.common.db import db, ma
from app.routes import register_routes
from flasgger import Swagger


def load_config():
    """Завантаження конфігурації з файлу app.yml"""
    path = os.path.join(os.path.dirname(__file__), "config", "app.yml")
    print("Looking for config at:", path)
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    print("Loaded config:", config)
    return config


def create_app():
    """Створення Flask додатку з усіма налаштуваннями"""
    config = load_config()
    app = Flask(__name__)

    # ---- DATABASE CONFIG ----
    db_conf = config.get("database")
    if not db_conf:
        raise ValueError("Database config is missing in app.yml")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{db_conf['user']}:{db_conf['pass']}"
        f"@{db_conf['host']}:{db_conf['port']}/{db_conf['name']}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = config.get("secret_key", "change_me")

    # ---- INIT EXTENSIONS ----
    db.init_app(app)
    ma.init_app(app)

    # ---- SWAGGER ----
    Swagger(app)

    with app.app_context():
        # Імпорт моделей (важливо для SQLAlchemy)
        from app.user.domain import models  # noqa: F401

        # Тест підключення до MySQL
        try:
            with db.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("MySQL підключився!")
        except Exception as e:
            print("Помилка підключення:", e)

    # ---- REGISTER ROUTES ----
    register_routes(app)

    # ---- HOME ROUTE ----
    @app.route("/")
    def home():
        """
        Home endpoint
        ---
        get:
          description: Перевірка роботи сервера
          responses:
            200:
              description: Сервер працює
        """
        return "Сервер Flask працює"

    # ---- LOG REQUESTS ----
    @app.before_request
    def log_request():
        print(f"\n[REQUEST] {request.method} {request.url}")
        if request.method in ["POST", "PUT", "PATCH"]:
            try:
                print("Request JSON:", request.get_json())
            except Exception as e:
                print("Cannot parse JSON:", e)

    # ---- GLOBAL ERROR HANDLER ----
    @app.errorhandler(Exception)
    def handle_exception(e):
        print("\n[ERROR]")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

    # ---- FAVICON ----
    @app.route("/favicon.ico")
    def favicon():
        return "", 204

    return app


# Створюємо додаток
app = create_app()

if __name__ == "__main__":
    # Використовуємо debug=True, щоб бачити повні traceback
    app.run(host="0.0.0.0", port=5000, debug=True)
