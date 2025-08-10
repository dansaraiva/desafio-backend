# Desafio de Backend - Coletor de Métricas Multicloud

Este projeto é uma API RESTful desenvolvida em Python que simula a coleta e exposição de métricas de uso (CPU, billing, compliance) de múltiplos provedores de nuvem.

O projeto foi criado para um desafio técnico e inclui documentação interativa com Swagger (OpenAPI) para fácil visualização e teste dos endpoints.

## 🛠️ Tecnologias Utilizadas
* **Python 3.10+**
* **Flask**: Microframework web para a criação da API.
* **Flasgger**: Biblioteca para geração de documentação OpenAPI (Swagger) para aplicações Flask.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar a aplicação em seu ambiente local.

**1. Clone o repositório ou descompacte os arquivos em uma pasta.**

**2. Crie e ative um ambiente virtual:**
* No macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
* No Windows:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate

**3. Instale as dependências necessárias:**
  ```bash 
  pip install -r requirements.txt
  ```
**4. Inicie o servidor da API:**
  ```bash
  flask run
  ```
O servidor estará disponível em http://127.0.0.1:5000. Por padrão, o comando flask run ativa o modo de produção. Para desenvolvimento com recarregamento automático, você pode executar com flask --app app --debug run.

**5. Acesse os endpoints:**

* API de Métricas: Para ver a resposta JSON com os dados dos provedores.

  * http://127.0.0.1:5000/metrics

* Documentação Interativa (Swagger UI): Para explorar a API e testá-la diretamente do navegador.

  * http://127.0.0.1:5000/docs

## 📁 Estrutura do Projeto

desafio-multicloud/
├── venv/                 # Ambiente virtual do Python (ignorado pelo Git)
├── app.py                # Código-fonte principal da aplicação Flask
├── requirements.txt      # Lista de dependências para instalação
└── README.md             # Este arquivo de documentação


## 👨‍💻 Autor
**Daniel dos Santos Saraiva**
* [LinkedIn](https://www.linkedin.com/in/danielssaraiva/)
* [GitHub](https://github.com/dansaraiva/desafio-backend)