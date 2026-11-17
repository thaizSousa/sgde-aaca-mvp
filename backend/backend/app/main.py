sgde-aaca-mvp/
├── .github/
│   └── workflows/
│       └── ci.yml                 # Pipeline de Integração Contínua (Etapa 3)
├── backend/
│   ├── app/
│   │   ├── main.py                # Ponto de entrada FastAPI e rotas
│   │   ├── models.py              # Entidades SQLAlchemy (Beneficiario, Lote, Entrega)
│   │   ├── schemas.py             # Validações Pydantic (proteção de entradas - RNF02)
│   │   ├── crud.py                # Lógica de triagem por CPF e baixa PEPS (RF01-RF03)
│   │   ├── security.py            # Hash Argon2id e tokens JWT (RNF01)
│   │   └── database.py            # Conexão PostgreSQL / SQLite de testes
│   └── tests/
│       ├── test_unit_peps.py      # Testes unitários da regra PEPS e elegibilidade
│       └── test_integration.py    # Testes de integração das rotas da API
├── frontend/
│   ├── index.html                 # Interface PWA Mobile-First (Telas 1, 2 e 3)
│   ├── styles.css                 # Estilização WCAG AA (contraste >= 4.5:1, alvos >= 48px)
│   ├── app.js                     # Lógica de fluxo, máscaras e alertas multimodais
│   └── manifest.json              # Configuração PWA leve (< 3s em Fast 3G)
├── requirements.txt               # Dependências (fastapi, uvicorn, sqlalchemy, pytest, etc.)
└── README.md                      # Documentação técnica completa do projeto
