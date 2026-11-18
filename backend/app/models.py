from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Beneficiario(Base):
    __tablename__ = "beneficiarios"
    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(14), unique=True, nullable=False)
    nome = Column(String(120), nullable=False)
    recebeu_mes_atual = Column(Boolean, default=False)

class LoteEstoque(Base):
    __tablename__ = "lotes_estoque"
    id = Column(Integer, primary_key=True, index=True)
    codigo_lote = Column(String(20), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data_validade = Column(Date, nullable=False)
