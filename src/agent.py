"""
Agente principal do Bolso Inteligente.

Responsável por integrar:
- carregamento dos dados;
- cálculos financeiros;
- prompts;
- modelo de IA através do Ollama.
"""

import ollama

from data_loader import carregar_dados
from calculations import (
    calcular_total_receitas,
    calcular_total_gastos,
    calcular_saldo,
    calcular_gastos_por_categoria,
    calcular_gasto_categoria,
    calcular_meta_mensal,
)
from prompts import SYSTEM_PROMPT, criar_prompt_usuario


# Modelo utilizado pelo agente
MODELO = "qwen3:4b"

def identificar_intencao(pergunta):
    """
    Identifica de forma simples a intenção da pergunta.
    """

    pergunta = pergunta.lower().strip()

    if "quanto" in pergunta and "aliment" in pergunta:
        return "gasto_categoria"

    if "quanto" in pergunta and "gasto" in pergunta:
        return "total_gastos"

    if "saldo" in pergunta:
        return "saldo"

    if "categoria" in pergunta and (
        "gasto" in pergunta or "despesa" in pergunta
    ):
        return "gastos_categoria"

    if "meta" in pergunta or "juntar" in pergunta:
        return "meta"

    if "juros" in pergunta:
        return "educacao"

    if "inflação" in pergunta or "inflacao" in pergunta:
        return "educacao"

    return "geral"

def executar_calculo(intencao, transacoes):
    """
    Executa o cálculo correspondente à intenção identificada.
    """

    if intencao == "gasto_categoria":

        valor = calcular_gasto_categoria(
            transacoes,
            "alimentacao"
        )

        return (
            f"O gasto com alimentação foi de "
            f"R$ {valor:.2f}."
        )

    if intencao == "total_gastos":

        valor = calcular_total_gastos(transacoes)

        return (
            f"O total de gastos registrados foi de "
            f"R$ {valor:.2f}."
        )

    if intencao == "saldo":

        valor = calcular_saldo(transacoes)

        return (
            f"O saldo calculado com base nas transações "
            f"registradas é de R$ {valor:.2f}."
        )

    if intencao == "gastos_categoria":

        gastos = calcular_gastos_por_categoria(
            transacoes
        )

        resultado = "Gastos por categoria:\n"

        for categoria, valor in gastos.items():

            resultado += (
                f"- {categoria.title()}: "
                f"R$ {valor:.2f}\n"
            )

        return resultado

    return None

class BolsoInteligente:
    """
    Classe principal do agente Bolso Inteligente.
    """

    def __init__(self):
        """
        Inicializa o agente e carrega os dados.
        """

        self.dados = carregar_dados()

        self.transacoes = self.dados["transacoes"]
        self.perfil = self.dados["perfil"]
        self.categorias = self.dados["categorias"]
        self.conceitos = self.dados["conceitos"]

    def obter_resumo_financeiro(self):
        """
        Calcula um resumo financeiro da base.
        """

        total_receitas = calcular_total_receitas(
            self.transacoes
        )

        total_gastos = calcular_total_gastos(
            self.transacoes
        )

        saldo = calcular_saldo(
            self.transacoes
        )

        gastos_categoria = calcular_gastos_por_categoria(
            self.transacoes
        )

        return {
            "total_receitas": total_receitas,
            "total_gastos": total_gastos,
            "saldo": saldo,
            "gastos_categoria": gastos_categoria,
        }

    def criar_contexto_financeiro(self):
        """
        Cria um contexto resumido para o modelo de IA.
        """

        resumo = self.obter_resumo_financeiro()

        contexto = f"""
PERFIL DO USUÁRIO

Nome: {self.perfil.get("nome", "Não informado")}
Renda mensal: R$ {self.perfil.get("renda_mensal", 0):.2f}

RESUMO FINANCEIRO

Total de receitas:
R$ {resumo["total_receitas"]:.2f}

Total de gastos:
R$ {resumo["total_gastos"]:.2f}

Saldo:
R$ {resumo["saldo"]:.2f}

GASTOS POR CATEGORIA
"""

        for categoria, valor in resumo["gastos_categoria"].items():

            contexto += (
                f"\n{categoria.title()}: "
                f"R$ {valor:.2f}"
            )

        return contexto

    def responder(self, pergunta):
        """
        Processa a pergunta do usuário e decide
        se deve utilizar um cálculo ou o modelo de IA.
        """

        intencao = identificar_intencao(pergunta)

        resultado = executar_calculo(
            intencao,
            self.transacoes
        )

        # Se Python conseguiu calcular,
        # envia o resultado para o modelo explicar.
        if resultado:

            contexto = f"""
    RESULTADO CALCULADO PELO SISTEMA:

    {resultado}
    """

        else:

            contexto = self.criar_contexto_financeiro()

        prompt = criar_prompt_usuario(
            pergunta,
            contexto
        )

        resposta = ollama.chat(
            model=MODELO,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return resposta["message"]["content"]


if __name__ == "__main__":
    print("===================================")
    print("      💰 BOLSO INTELIGENTE")
    print("       Agente de IA Financeira")
    print("===================================")
    print()
    print("Agente inicializado com sucesso!")
    print()
    print("Digite sua pergunta financeira.")
    print("Digite 'sair' para encerrar.")
    print()

    agente = BolsoInteligente()

    while True:
        pergunta = input("Você: ").strip()

        if pergunta.lower() == "sair":
            print()
            print("Bolso Inteligente: Até logo! 👋")
            break

        if not pergunta:
            continue

        print()
        resposta = agente.responder(pergunta)

        print("Bolso Inteligente:")
        print(resposta)
        print()