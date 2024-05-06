# API FEITA EM FLASK POR VINICIUS INZAURRALDE

Esse projeto é resultado de um test code.


Principais bibliotecas usadas:
1. Flask.
2. Flask-RESTful.

Estrutura do projeto:
```
.
├── README.md
├── app.py
├── config
│   └── logger.db
├── endpoints
│   ├── __init__.py
│   ├── resource
│   │   ├── consulta_cartao_resource.py
│   │   └── inserir_cartao_resource.py
│   │   └── inserir_lote_resource.py
│   │   └── login_resource.py
│   └── service
│       ├── consulta_cartao_service.py
│       └── insere_cartao_service.py
│       └── insere_lote_service.py
│       └── login_service.py
├── infra
│   └── helper.py
├── instance
│   └── data.db
├── mocks
├── models
│   └── model.py
├── schema
| 	├── inseri_cartao_schema.py
|	└── login_schema.py
├── utils
│   └── enum
|        └── token_enum.py
│   ├── responses
| 	| 	├── messages.py
|   |   ├── response_model_abstract.py
|   |   ├── response_models.py
|   |   └── utilitarios
└──	└── utilitarios.py
```

* resource - Camada de resource estão alocados todos os endpoints
* app.py   - Aplicação Flask configuração para inicialização
* service  - Camada responsavel pelas aplicações das regras do negócio
* infra    - Camada responsavel por armazenar as regras de autenticação da API
* models   - Camada responsavel por definir a modelagem das entidades e iteração no DB
* schema   - Camada responsavel pela validação dos dados de entrada dos endpoints
* utils    - Camada responsavel por metodos e classes auxiliares 

## Iniciando a API

1. Clone o repositório ou extraia o arquivo.
2. pip install -r requirements.txt
3. insira o seguinte comando no console:
    1. python app.py
4. Espere a inicialização do servidor

## Usando a API

BASE_URL http://127.0.0.1:5000/

ATENÇÃO
* Antes de fazer as requisições nos endpoints leia os contratos de requisição (PDF)
* Todos os logs das requições são armazenas em um arquivo .log na raiz do diretório principal
* A chave secret da autenticação esta disposnivel em code para facilitar a execução local, mas é recomendavel configurar em uma variavel de ambiente
* Um usuário default sera injetado no inicio da aplicação para facilitar o teste do time hyperativa