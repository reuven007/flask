from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Definir o modelo da tabela
class Contatos(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

# Caminho para o banco de dados
database_path = r'C:\Users\MBM\Desktop\Flask_web\instance\database.db'
engine = create_engine(f'sqlite:///{database_path}')
Session = sessionmaker(bind=engine)
session = Session()

# Excluir registros por ID
try:
    # ids_para_excluir = [6]  # IDs que deseja excluir
    excluidos = session.query(Contatos).filter(Contatos.id.between(1,8)).delete(synchronize_session=False)
    session.commit()
    print(f"Os IDs {excluidos} excluídos com sucesso!")
except Exception as e:
    print(f"Erro ao excluir registros: {e}")
