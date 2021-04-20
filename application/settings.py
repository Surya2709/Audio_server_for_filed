from environs import Env

env = Env()

env.read_env()

DATABASE_URL = env.str("DATABASE")
DB_PORT = env.str("DB_PORT")
ENV = env.str("FLASK_ENV")


