# Base de Conhecimento

## Dados Utilizados

A base de conhecimento do **Bolso Inteligente** utiliza arquivos estruturados em formato CSV e JSON para armazenar informações relacionadas à organização financeira e à educação financeira.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e acompanhar o histórico de atendimentos |
| `perfil_usuario.json` | JSON | Personalizar análises, metas e orientações de acordo com as informações do usuário |
| `conceitos_financeiros.json` | JSON | Consultar e explicar conceitos de educação financeira de forma simples e didática |
| `transacoes.csv` | CSV | Analisar receitas, despesas, categorias e padrões de gastos informados pelo usuário |
| `categorias_despesas.json` | JSON | Classificar e organizar despesas de acordo com categorias financeiras predefinidas |

---

## Adaptações nos Dados

Os dados disponibilizados originalmente foram adaptados para atender ao objetivo do **Bolso Inteligente**, que é auxiliar na educação e organização financeira pessoal.

As principais adaptações realizadas foram:

- Substituição do arquivo `perfil_investidor.json` por `perfil_usuario.json`, removendo informações relacionadas à classificação de perfil de investidor e mantendo informações úteis para organização financeira e definição de metas.
- Substituição do conteúdo de `produtos_financeiros.json` por `conceitos_financeiros.json`, direcionando a base de conhecimento para conceitos de educação financeira.
- Inclusão do arquivo `categorias_despesas.json`, contendo categorias utilizadas para auxiliar na classificação e organização das despesas.
- Manutenção do arquivo `transacoes.csv` para permitir análises de receitas, despesas e padrões de gastos.
- Adaptação dos dados para que possam ser utilizados como exemplos durante as interações com o agente.

Os dados utilizados no projeto possuem finalidade educacional e de demonstração. O agente não utiliza essas informações para recomendar produtos financeiros específicos ou realizar transações.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV da pasta `data` são utilizados como fontes estruturadas de informação para o agente.

Durante a execução da aplicação, os dados necessários podem ser carregados pelo código Python e organizados de acordo com a tarefa solicitada pelo usuário.

Por exemplo:

- `transacoes.csv` é utilizado para análises de receitas e despesas;
- `categorias_despesas.json` auxilia na classificação dos gastos;
- `perfil_usuario.json` fornece informações para contextualizar metas e objetivos;
- `conceitos_financeiros.json` fornece informações para explicações de educação financeira;
- `historico_atendimento.csv` pode fornecer contexto sobre interações anteriores.

A utilização dos dados é feita de acordo com a necessidade da solicitação, evitando incluir informações desnecessárias no contexto do agente.

### Como os dados são usados no prompt?

Os dados relevantes são selecionados de acordo com a intenção identificada na solicitação do usuário e utilizados como contexto para a geração da resposta.

O agente deve priorizar as informações disponíveis na base de conhecimento e os dados fornecidos pelo próprio usuário.

A arquitetura separa as responsabilidades entre o modelo de linguagem e o processamento realizado em Python:

```text
Usuário
   │
   ▼
Identificação da solicitação
   │
   ├──► Educação financeira
   │        └──► conceitos_financeiros.json
   │
   ├──► Classificação de despesa
   │        └──► categorias_despesas.json
   │
   ├──► Análise de gastos
   │        └──► transacoes.csv
   │
   └──► Metas e perfil
            └──► perfil_usuario.json
                     │
                     ▼
              Contexto relevante
                     │
                     ▼
                Agente IA
                     │
                     ▼
              Resposta educativa
```

Os cálculos financeiros que dependem de operações matemáticas devem ser realizados por Python sempre que possível. O modelo de linguagem é utilizado principalmente para interpretar a solicitação, organizar as informações e apresentar os resultados de maneira clara e educativa.

---

## Exemplo de Contexto Montado

A seguir, um exemplo simplificado de como informações dos arquivos podem ser organizadas antes de serem apresentadas ao agente:

```text
Contexto do Usuário:

Nome: Usuário Exemplo
Renda mensal: R$ 5.000,00
Objetivo principal: Organização financeira

Metas financeiras:
- Completar reserva de emergência: R$ 15.000,00
- Entrada do apartamento: R$ 50.000,00

Últimas transações:
- 02/10: Aluguel - R$ 1.200,00 - Moradia
- 03/10: Supermercado - R$ 450,00 - Alimentação
- 05/10: Netflix - R$ 55,90 - Lazer
- 07/10: Farmácia - R$ 89,00 - Saúde
- 10/10: Restaurante - R$ 120,00 - Alimentação
- 12/10: Uber - R$ 45,00 - Transporte

Categorias disponíveis:
- Moradia
- Alimentação
- Transporte
- Saúde
- Educação
- Lazer
- Contas e Serviços
- Compras
- Investimentos
- Outros

Solicitação do usuário:
"Quero saber quanto estou gastando com alimentação."

Contexto utilizado pelo agente:
- Supermercado: R$ 450,00
- Restaurante: R$ 120,00

Resultado do cálculo:
- Total em Alimentação: R$ 570,00

Orientação:
Apresentar o resultado ao usuário de forma clara, informando que o cálculo considera apenas as transações disponíveis na base de dados.
```

---

## Regras para Utilização da Base

O agente deve seguir algumas regras para utilização dos dados:

- Utilizar somente informações disponíveis na base ou fornecidas pelo usuário;
- Não inventar transações, valores, metas ou informações pessoais;
- Informar quando os dados disponíveis forem insuficientes para realizar uma análise;
- Identificar claramente quando um exemplo for apenas ilustrativo;
- Utilizar Python para cálculos financeiros sempre que possível;
- Utilizar `categorias_despesas.json` como referência para classificação das despesas;
- Utilizar `conceitos_financeiros.json` como fonte de apoio para explicações de educação financeira;
- Não transformar os dados da base em recomendações de investimentos;
- Não realizar transações financeiras;
- Preservar a finalidade educacional e de organização financeira do projeto.

## Objetivo da Base de Conhecimento

A base de conhecimento tem como objetivo fornecer ao **Bolso Inteligente** informações estruturadas para auxiliar na organização financeira pessoal, permitindo que o agente:

- Analise despesas;
- Organize gastos por categoria;
- Acompanhe metas financeiras;
- Explique conceitos de educação financeira;
- Identifique padrões de gastos;
- Apresente cálculos de forma transparente;
- Forneça orientações educativas baseadas nos dados disponíveis.

A base funciona como fonte de contexto para o agente, enquanto o processamento realizado em Python é responsável pelas regras e cálculos que exigem maior precisão.
