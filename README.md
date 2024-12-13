# prefect-stock-workflow-starter
Código inicial para projeto de desenvolvimento de fluxo de trabalho para ações utilizando a biblioteca prefect.


# Workflow Assignment

Neste assignment, você criará um workflow usando a biblioteca Prefect para realizar tarefas automatizadas, como:
- Buscar dados de uma API ou fonte de dados.
- Processar e analisar os dados.
- Salvar os resultados.

## Tarefas
1. Complete o código no arquivo `main.py` preenchendo as funções de `fetch_data`, `process_data` e `save_results`.
2. Adicione um teste simples para verificar a execução do workflow.

## Requisitos
- Python 3.8 ou superior
- Prefect (instale via `pip install prefect`)

## Como rodar o projeto
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute o workflow: `python main.py`.

Neste assignment, você criará e executará um workflow no **Prefect Cloud**.

## Configuração

### 1. Criar uma conta no Prefect Cloud
- Acesse [Prefect Cloud](https://app.prefect.io/) e crie uma conta.
- Obtenha sua **API Key**:
  - Vá para **Account Settings** > **API Keys** > **Create API Key**.
  - Copie a chave gerada.

### 2. Configurar o Prefect no seu ambiente local
- No terminal, faça login no Prefect Cloud:
  ```bash
  prefect cloud login
  ```
  - Insira sua API Key quando solicitado.

Bom trabalho!
