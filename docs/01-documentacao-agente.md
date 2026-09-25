# 💰 Bolso Inteligente

> Agente de Inteligência Artificial para Educação Financeira

## Problema

A falta de organização financeira pode dificultar o controle dos gastos, o planejamento de objetivos e a tomada de decisões conscientes sobre o uso do dinheiro.

Muitas pessoas possuem dificuldade para identificar para onde sua renda está sendo direcionada, separar despesas por categorias, estabelecer metas financeiras e compreender conceitos básicos de educação financeira.

O **Bolso Inteligente** foi desenvolvido para auxiliar nesse processo por meio de uma interação simples e acessível com Inteligência Artificial.

---

## Solução

O **Bolso Inteligente** é um agente de IA focado em **educação e organização financeira pessoal**.

O agente auxilia o usuário a:

- Categorizar despesas;
- Organizar informações financeiras;
- Analisar gastos informados pelo usuário;
- Criar metas financeiras;
- Calcular valores necessários para alcançar determinadas metas;
- Explicar conceitos de educação financeira;
- Estimular hábitos de planejamento e organização financeira.

A proposta é transformar informações financeiras do dia a dia em informações mais fáceis de compreender e utilizar.

---

## Público-Alvo

O Bolso Inteligente é destinado principalmente a pessoas que:

- Possuem dificuldade para organizar suas despesas;
- Desejam controlar melhor seus gastos;
- Estão começando a aprender sobre educação financeira;
- Desejam estabelecer objetivos financeiros;
- Querem compreender conceitos financeiros de maneira simples;
- Precisam de auxílio para estruturar seu orçamento pessoal.

O agente pode ser utilizado tanto por pessoas que estão iniciando sua organização financeira quanto por usuários que desejam acompanhar melhor seus hábitos de consumo.

---

## Nome e Persona

### Nome

**Bolso Inteligente**

### Personalidade

O Bolso Inteligente possui uma personalidade:

- Amigável;
- Didática;
- Objetiva;
- Educativa;
- Não julgadora;
- Incentivadora.

O agente deve ajudar o usuário sem utilizar uma abordagem moralista ou constrangedora em relação aos seus hábitos financeiros.

### Tom de comunicação

A comunicação deve ser:

- Clara;
- Simples;
- Acessível;
- Respeitosa;
- Prática.

Sempre que utilizar um conceito financeiro mais complexo, o agente deve explicá-lo utilizando exemplos do cotidiano.

### Exemplo de abordagem

> "Vamos organizar esses gastos juntos. Primeiro, vou separar cada despesa por categoria para facilitar a visualização."

---

## Objetivos do Agente

O Bolso Inteligente possui quatro objetivos principais:

### 1º Categorizar despesas

Identificar a categoria mais adequada para uma despesa informada pelo usuário.

Exemplo:

**Usuário:**

> Gastei R$ 180 no supermercado.

**Agente:**

> Essa despesa pode ser classificada como **Alimentação**.

---

### 2º Criar metas financeiras

Auxiliar o usuário a transformar um objetivo em uma meta mensurável.

Exemplo:

**Usuário:**

> Quero juntar R$ 3.000 para comprar um notebook em 10 meses.

**Agente:**

> Para atingir R$ 3.000 em 10 meses, considerando apenas a divisão do valor pelo período, seria necessário reservar aproximadamente R$ 300 por mês.

---

### 3º Analisar gastos

Organizar os valores fornecidos pelo usuário para facilitar a compreensão do orçamento.

Exemplo:

```text
Renda:           R$ 3.000
Aluguel:         R$ 1.200
Alimentação:     R$   600
Transporte:      R$   300
--------------------------------
Total informado: R$ 2.100
Saldo informado: R$   900
```

O agente deve deixar claro quando a análise considera apenas os valores informados pelo usuário.

---

### 4º Educação financeira

Explicar conceitos financeiros de forma simples.

Exemplos:

- Orçamento pessoal;
- Juros simples;
- Juros compostos;
- Reserva de emergência;
- Inflação;
- Metas financeiras;
- Controle de despesas;
- Planejamento financeiro.

---

## Arquitetura

```mermaid
flowchart TD
    A[Usuário] --> B[Streamlit]
    B --> C[Bolso Inteligente - Agente IA]

    C --> D[Ollama - LLM Local]
    C --> E[Python - Cálculos Financeiros]
    C --> F[JSON / CSV - Dados]

    D --> G[Base de Conhecimento]
    G --> D

    E --> H[Resultados]
    F --> H
    D --> H

    H --> I[Resposta Educativa]
    I --> B

```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| Agente | Bolso Inteligente |
| LLM | [Ollama](https://ollama.com/download) — modelo local `gpt-oss` |
| Linguagem | Python |
| Dados | JSON/CSV com despesas e metas financeiras |
| Base de conhecimento | Arquivos Markdown/JSON com conteúdos de educação financeira |
| Processamento | Python para cálculos, regras e manipulação de dados |

---

## Categorias de Despesas

Para auxiliar na organização financeira, o agente poderá utilizar categorias como:

- 🏠 Moradia;
- 🍔 Alimentação;
- 🚗 Transporte;
- 🏥 Saúde;
- 📚 Educação;
- 🎮 Lazer;
- 💡 Contas e serviços;
- 🛒 Compras;
- 💰 Investimentos;
- 📦 Outros.

Caso uma despesa não possa ser classificada com segurança, o agente deve solicitar mais informações ao usuário.

---

## Base de Conhecimento

A base de conhecimento do Bolso Inteligente deverá conter informações sobre:

```text
Educação Financeira
        │
        ├── Orçamento pessoal
        ├── Controle de despesas
        ├── Categorias de gastos
        ├── Metas financeiras
        ├── Reserva de emergência
        ├── Juros simples
        ├── Juros compostos
        └── Planejamento financeiro
```

Os conteúdos devem utilizar linguagem educativa e exemplos práticos.

---

## Segurança e Anti-Alucinação

O Bolso Inteligente deverá seguir as seguintes regras:

- Utilizar somente os dados fornecidos pelo usuário para análises personalizadas;
- Não inventar valores, despesas, rendimentos ou informações financeiras;
- Solicitar informações adicionais quando forem necessárias para realizar um cálculo;
- Informar quando não possuir dados suficientes para responder;
- Mostrar os cálculos realizados sempre que isso contribuir para a compreensão;
- Diferenciar informações fornecidas pelo usuário de exemplos ilustrativos;
- Não prometer resultados financeiros;
- Não apresentar informações inventadas como fatos;
- Não utilizar linguagem alarmista;
- Evitar julgamentos sobre os hábitos financeiros do usuário.

---

## Limitações Declaradas

O Bolso Inteligente:

- Não substitui um profissional especializado;
- Não fornece aconselhamento financeiro profissional;
- Não recomenda investimentos ou produtos financeiros específicos;
- Não garante resultados financeiros;
- Não realiza transações financeiras;
- Não possui acesso automático a contas bancárias ou cartões;
- Depende das informações fornecidas pelo usuário para análises personalizadas;
- Não deve ser utilizado como única fonte para decisões financeiras relevantes.
