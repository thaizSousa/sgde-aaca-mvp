from datetime import date

def selecionar_lote_peps(lotes):
    disponiveis = [l for l in lotes if l["quantidade"] > 0]
    return sorted(disponiveis, key=lambda x: x["validade"])[0]

def test_priorizacao_lote_mais_proximo_vencimento():
    lotes = [
        {"codigo": "Lote #05", "quantidade": 10, "validade": date(2026, 12, 20)},
        {"codigo": "Lote #04", "quantidade": 5, "validade": date(2026, 11, 25)},
    ]
    selecionado = selecionar_lote_peps(lotes)
    assert selecionado["codigo"] == "Lote #04"
