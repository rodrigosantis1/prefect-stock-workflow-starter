from prefect import flow, task

@task
def fetch_data():
    # TODO: Adicione lógica para buscar dados de uma fonte (exemplo: Yahoo Finance).
    pass

@task
def process_data(data):
    # TODO: Implemente o processamento dos dados.
    pass

@task
def save_results(results):
    # TODO: Salve os resultados em um arquivo ou banco de dados.
    pass

@flow
def workflow_example():
    data = fetch_data()
    results = process_data(data)
    save_results(results)

if __name__ == "__main__":
    workflow_example()