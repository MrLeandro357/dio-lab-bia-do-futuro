import pandas as pd

from data_loader import carregar_dados


def preparar_transacoes(transacoes):
    """
    Prepara o DataFrame de transações para os cálculos.
    """

    df = transacoes.copy()

    # Garante que os valores sejam numéricos
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce").fillna(0)

    # Padroniza o tipo da transação
    df["tipo"] = df["tipo"].astype(str).str.lower().str.strip()

    # Padroniza a categoria
    df["categoria"] = df["categoria"].astype(str).str.lower().str.strip()

    return df


def calcular_total_receitas(transacoes):
    """
    Calcula o total de receitas.
    """

    df = preparar_transacoes(transacoes)

    receitas = df[df["tipo"] == "entrada"]

    return receitas["valor"].sum()


def calcular_total_gastos(transacoes):
    """
    Calcula o total de despesas.
    """

    df = preparar_transacoes(transacoes)

    gastos = df[df["tipo"] == "saida"]

    return gastos["valor"].sum()


def calcular_saldo(transacoes):
    """
    Calcula o saldo financeiro:

    receitas - despesas
    """

    total_receitas = calcular_total_receitas(transacoes)
    total_gastos = calcular_total_gastos(transacoes)

    return total_receitas - total_gastos


def calcular_gastos_por_categoria(transacoes):
    """
    Calcula quanto foi gasto em cada categoria.
    """

    df = preparar_transacoes(transacoes)

    gastos = df[df["tipo"] == "saida"]

    resultado = (
        gastos
        .groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
    )

    return resultado


def calcular_gasto_categoria(transacoes, categoria):
    """
    Calcula o total gasto em uma categoria específica.
    """

    df = preparar_transacoes(transacoes)

    categoria = categoria.lower().strip()

    gastos = df[
        (df["tipo"] == "saida") &
        (df["categoria"] == categoria)
    ]

    return gastos["valor"].sum()


def calcular_meta_mensal(valor_meta, meses):
    """
    Calcula quanto deve ser reservado por mês
    para alcançar uma meta.

    Exemplo:
    R$ 3.000 em 10 meses = R$ 300 por mês.
    """

    if meses <= 0:
        raise ValueError("O número de meses deve ser maior que zero.")

    return valor_meta / meses


if __name__ == "__main__":

    dados = carregar_dados()

    transacoes = dados["transacoes"]

    print("===================================")
    print("      💰 BOLSO INTELIGENTE")
    print("      Cálculos Financeiros")
    print("===================================")
    print()

    total_receitas = calcular_total_receitas(transacoes)
    total_gastos = calcular_total_gastos(transacoes)
    saldo = calcular_saldo(transacoes)

    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de gastos:   R$ {total_gastos:.2f}")
    print(f"Saldo:             R$ {saldo:.2f}")

    print()
    print("Gastos por categoria:")
    print()

    gastos_categoria = calcular_gastos_por_categoria(transacoes)

    for categoria, valor in gastos_categoria.items():
        print(f"{categoria.title():20} R$ {valor:.2f}")

    print()
    print("Exemplo de análise:")
    print()

    gasto_alimentacao = calcular_gasto_categoria(
        transacoes,
        "alimentacao"
    )

    print(
        f"Gasto com alimentação: "
        f"R$ {gasto_alimentacao:.2f}"
    )

    print()
    print("Exemplo de meta financeira:")

    meta = calcular_meta_mensal(3000, 10)

    print(
        f"Para juntar R$ 3.000,00 em 10 meses: "
        f"R$ {meta:.2f} por mês"
    )