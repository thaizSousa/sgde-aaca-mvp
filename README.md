# SGDE | AACA — Sistema de Gestão de Doações e Estoque (MVP)

Aplicação web progressiva (**PWA Mobile-First**) desenvolvida para a **Associação de Apoio à Criança e ao Adolescente (AACA)** com o objetivo de eliminar entregas duplicadas de cestas básicas às 120 famílias atendidas e reduzir perdas de alimentos por vencimento por meio do controle automatizado **PEPS/FIFO** (Primeiro que Entra, Primeiro que Sai), alinhado à **Meta 2.1 do ODS 2**.

## Stack Tecnológica
- **Backend:** Python 3.12, FastAPI, SQLAlchemy ORM, Pydantic
- **Banco de Dados:** PostgreSQL (Supabase) / SQLite (ambiente de testes)
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), PWA Mobile-First
- **Qualidade & DevOps:** Pytest, GitHub Actions (CI)

## Requisitos Atendidos no MVP
- **RF01:** Identificação e consulta de elegibilidade do beneficiário por CPF.
- **RF02:** Bloqueio automático de entregas duplicadas no mesmo mês civil.
- **RF03:** Baixa automática de estoque priorizando o lote com validade mais próxima (PEPS).
- **RNF01 / RNF02:** Autenticação segura (Argon2id/JWT) e sanitização de entradas contra OWASP Top 10.
- **RNF03:** Desempenho otimizado para dispositivos móveis de entrada (< 3s em Fast 3G).
- **RNF04:** Acessibilidade WCAG 2.1 AA (contraste mínimo 4.5:1, botões >= 48x48px e alertas multimodais).

## Como Executar Localmente
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie a API: `uvicorn backend.app.main:app --reload`
3. Execute os testes automatizados: `pytest`

