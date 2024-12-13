from prefect import flow, task

@task
def fetch_data():
    """Simula a busca de dados."""
    print("Buscando dados...")
    return [1, 2, 3, 4, 5]

@task
def process_data(data):
    """Processa os dados buscados."""
    print(f"Processando dados: {data}")
    processed = [x * 2 for x in data]
    return processed

@task
def save_results(results):
    """Salva os resultados processados."""
    print(f"Salvando resultados: {results}")
    with open("results.txt", "w") as f:
        f.write(str(results))
    print("Resultados salvos em 'results.txt'.")

@flow(name="Workflow Assignment")
def workflow_example():
    """Define o fluxo principal."""
    data = fetch_data()
    results = process_data(data)
    save_results(results)

if __name__ == "__main__":
    # Executa o fluxo localmente e registra no Prefect Cloud
    workflow_example()
