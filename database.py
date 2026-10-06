from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Banco SQLite
DATABASE_URL = "sqlite:///./dietas"

# Conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Sessão do banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base usada pelos Models
Base = declarative_base()


# Dependência para acessar o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()