from pathlib import Path
import json
import csv


# Localização da pasta data/
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def carregar_json(nome_arquivo):
    """
    Carrega um arquivo JSON da pasta data/.
    """
    caminho = DATA_DIR / nome_arquivo

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_csv(nome_arquivo):
    """
    Carrega um arquivo CSV da pasta data/.
    """
    caminho = DATA_DIR / nome_arquivo

    with open(caminho, "r", encoding="utf-8-sig") as arquivo:
        return list(csv.DictReader(arquivo))


def carregar_dados():
    """
    Carrega todos os dados utilizados pelo Bolso Inteligente.
    """

    dados = {
        "categorias": carregar_json("categorias_despesas.json"),
        "conceitos": carregar_json("conceitos_financeiros.json"),
        "historico": carregar_csv("historico_atendimento.csv"),
        "perfil": carregar_json("perfil_usuario.json"),
        "transacoes": carregar_csv("transacoes.csv"),
    }

    return dados


if __name__ == "__main__":
    dados = carregar_dados()

    print("Dados carregados com sucesso!")
    print()

    print(f"Categorias: {len(dados['categorias'])}")
    print(f"Conceitos: {len(dados['conceitos'])}")
    print(f"Histórico: {len(dados['historico'])}")
    print(f"Transações: {len(dados['transacoes'])}")

    print()
    print("Perfil:")
    print(dados["perfil"]["nome"])

    print()
    print("Primeira transação:")
    print(dados["transacoes"][0])
