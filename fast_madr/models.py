from sqlalchemy.orm import Mapped, mapped_column, registry, sessionmaker
from sqlalchemy import create_engine


reg = registry()

engine = create_engine(
    "postgresql+psycopg://app_user:app_password@localhost:5433/app_madr",
)


@reg.mapped_as_dataclass
class User:
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]


Session = sessionmaker(engine)
reg.metadata.create_all(engine)


# funcao de controle da sessao
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
