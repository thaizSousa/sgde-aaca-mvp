from sqlalchemy.orm import Session
from . import models

def consultar_elegibilidade(db: Session, cpf: str):
    beneficiario = db.query(models.Beneficiario).filter_by(cpf=cpf).first()
    if not beneficiario:
        return {"elegivel": False, "motivo": "CPF nao localizado no cadastro"}
    if beneficiario.recebeu_mes_atual:
        return {"elegivel": False, "motivo": "Bloqueio: entrega ja realizada neste mes"}
    return {"elegivel": True, "beneficiario": beneficiario.nome}

def obter_lote_peps(db: Session):
    return db.query(models.LoteEstoque).filter(
        models.LoteEstoque.quantidade > 0
    ).order_by(models.LoteEstoque.data_validade.asc()).first()
