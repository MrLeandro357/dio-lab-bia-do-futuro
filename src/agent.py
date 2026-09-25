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
        Envia uma pergunta ao modelo de IA.
        """

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

    agente = BolsoInteligente()

    print("Agente inicializado com sucesso!")
    print()

    pergunta = "Quanto gastei com alimentação?"

    print(f"Usuário: {pergunta}")
    print()

    resposta = agente.responder(pergunta)

    print("Bolso Inteligente:")
    print()
    print(resposta)