from database.database import Base
from sqlalchemy import Column, Integer, String

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Cliente(id={self.id}, nome='{self.nome}', cpf='{self.cpf}', email='{self.email}', telefone='{self.telefone}', idade={self.idade})>"