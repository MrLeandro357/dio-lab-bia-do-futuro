from pathlib import Path
import json
import pandas as pd


# Localização da raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Pasta onde estão os dados
DATA_DIR = BASE_DIR / "data"


def carregar_json(nome_arquivo):
    """Carrega um arquivo JSON da pasta data."""

    caminho = DATA_DIR / nome_arquivo

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_csv(nome_arquivo):
    """Carrega um arquivo CSV da pasta data."""

    caminho = DATA_DIR / nome_arquivo

    return pd.read_csv(caminho)


def carregar_dados():
    """Carrega todos os dados utilizados pelo Bolso Inteligente."""

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

    print("===================================")
    print("      💰 BOLSO INTELIGENTE")
    print("   Agente de Educação Financeira")
    print("===================================")
    print()
    print("Dados carregados com sucesso!!!")
    print()

    print(f"Categorias: {len(dados['categorias'])}")
    print(f"Conceitos: {len(dados['conceitos'])}")
    print(f"Histórico: {len(dados['historico'])}")
    print(f"Transações: {len(dados['transacoes'])}")

    print()
    print("Perfil:")
    print(f"Nome: {dados['perfil']['nome']}")
    print(f"Renda mensal: R$ {dados['perfil']['renda_mensal']:.2f}")

    print()
    print("Primeiras transações:")

    print(dados["transacoes"].head())