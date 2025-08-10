# app.py
from flask import Flask, jsonify
from flasgger import Swagger 
import datetime

app = Flask(__name__)

# --- CONFIGURAÇÃO DO FLASGGER ---
# Inicializa o Flasgger também add uma configuração de template para definir o título e a versão.
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

template = {
  "swagger": "2.0",
  "info": {
    "title": "API de Métricas Multicloud",
    "description": "Uma API para simular a coleta de métricas de provedores de nuvem.",
    "version": "1.0.0"
  },
}

swagger = Swagger(app, template=template, config=swagger_config)


# --- DADOS MOCKADOS ---
dados_mockados_provedores = {
    "aws": {
        "metricas": {
            "uso_cpu": 85.5,
            "billing": {"valor": 1250.70, "moeda": "USD"},
            "compliance": {"status": "Conforme", "detalhes": "Nenhuma violação encontrada."}
        }
    },
    "azure": {
        "metricas": {
            "uso_cpu": 72.0,
            "billing": {"valor": 980.50, "moeda": "USD"},
            "compliance": {"status": "Não Conforme", "detalhes": "2 políticas de segurança violadas."}
        }
    },
    "google_cloud": {
        "metricas": {
            "uso_cpu": 91.8,
            "billing": {"valor": 1530.00, "moeda": "USD"},
            "compliance": {"status": "Conforme", "detalhes": "Nenhuma violação encontrada."}
        }
    }
}


# --- ROTA DA API COM DOCUMENTAÇÃO ---
@app.route('/metrics', methods=['GET'])
def get_metrics():
    """
    Endpoint para buscar métricas consolidadas dos provedores de nuvem.
    Este docstring é lido pelo Flasgger para gerar a documentação da API.
    ---
    tags:
      - Métricas
    responses:
      200:
        description: Retorna uma lista de métricas para cada provedor.
        examples:
          application/json:
            {
              "data_coleta": "2025-08-10T14:00:00Z",
              "provedores": {
                "aws": {
                  "metricas": {
                    "uso_cpu": 85.5,
                    "billing": { "valor": 1250.70, "moeda": "USD" },
                    "compliance": { "status": "Conforme", "detalhes": "Nenhuma violação encontrada." }
                  }
                }
              }
            }
    """
    resposta = {
        "data_coleta": datetime.datetime.utcnow().isoformat() + "Z",
        "provedores": dados_mockados_provedores
    }
    return jsonify(resposta)


if __name__ == '__main__':
    app.run(debug=True)