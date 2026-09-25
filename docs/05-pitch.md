# Pitch (3 minutos)

> [!TIP]
> O pitch apresenta o problema, a solução, uma demonstração prática do agente e seus principais diferenciais. A demonstração pode ser realizada por meio de gravação de tela utilizando a aplicação do Bolso Inteligente.

## Roteiro Sugerido

### 1. O Problema — aproximadamente 30 segundos

Muitas pessoas têm dificuldade para organizar sua vida financeira.

É comum saber quanto recebe por mês, mas não saber exatamente para onde o dinheiro está indo. Além disso, categorizar despesas, acompanhar gastos, estabelecer metas e compreender conceitos financeiros pode ser difícil, principalmente para quem está começando a organizar suas finanças.

O problema que o **Bolso Inteligente** busca resolver é justamente essa dificuldade de transformar informações financeiras do dia a dia em algo organizado, compreensível e útil para o planejamento pessoal.

---

### 2. A Solução — aproximadamente 1 minuto

O **Bolso Inteligente** é um agente de Inteligência Artificial desenvolvido com foco em **educação e organização financeira pessoal**.

O usuário pode informar suas despesas, receitas ou objetivos financeiros e conversar com o agente utilizando linguagem natural.

O agente pode:

- Categorizar despesas;
- Organizar informações financeiras;
- Analisar gastos informados pelo usuário;
- Criar e acompanhar metas financeiras;
- Calcular quanto é necessário guardar para alcançar determinado objetivo;
- Explicar conceitos como orçamento, inflação e juros compostos;
- Auxiliar na identificação de padrões de gastos.

Um dos diferenciais da solução é separar as responsabilidades entre a Inteligência Artificial e os cálculos determinísticos.

Quando existe um cálculo financeiro, como descobrir quanto guardar por mês para alcançar uma meta, o Python pode realizar o cálculo, enquanto o modelo de linguagem é utilizado para interpretar a solicitação e apresentar o resultado de forma clara.

O agente também possui regras para evitar a criação de informações que não estão disponíveis nos dados fornecidos pelo usuário.

---

### 3. Demonstração — aproximadamente 1 minuto

Durante a demonstração, será apresentada a aplicação do **Bolso Inteligente** funcionando na prática.

Serão realizados alguns exemplos de interação:

#### Demonstração 1 — Análise de gastos

Perguntar:

```text
Quanto gastei com alimentação?
```

O agente deverá consultar os dados disponíveis e apresentar o cálculo.

Com os dados atuais da demonstração:

```text
Supermercado: R$ 450,00
Restaurante:  R$ 120,00

Total: R$ 570,00
```

#### Demonstração 2 — Meta financeira

Perguntar:

```text
Quero juntar R$ 3.000 em 10 meses. Quanto preciso guardar por mês?
```

O agente deverá calcular:

```text
R$ 3.000 ÷ 10 = R$ 300 por mês
```

E explicar que esse cálculo representa uma divisão simples do valor da meta pelo número de meses, sem considerar rendimentos ou juros.

#### Demonstração 3 — Educação financeira

Perguntar:

```text
O que são juros compostos?
```

O agente deverá explicar o conceito utilizando uma linguagem simples e, quando adequado, um exemplo do cotidiano.

---

### 4. Diferencial e Impacto — aproximadamente 30 segundos

O principal diferencial do **Bolso Inteligente** é combinar Inteligência Artificial com organização financeira e educação financeira em uma interação simples e acessível.

A proposta não é substituir um profissional financeiro nem indicar investimentos específicos. O objetivo é ajudar o usuário a **entender melhor seus próprios dados, organizar seus gastos e desenvolver hábitos de planejamento financeiro**.

O projeto também foi desenvolvido considerando princípios de segurança e confiabilidade: o agente não deve inventar informações, deve solicitar dados quando forem necessários e deve deixar claras suas limitações.

O impacto esperado é facilitar o acesso à educação financeira e ajudar as pessoas a transformar informações do cotidiano em decisões mais conscientes sobre organização e planejamento financeiro.

---

## Checklist do Pitch

- [ ] Duração máxima de 3 minutos
- [ ] Problema claramente definido
- [ ] Solução apresentada
- [ ] Arquitetura ou funcionamento explicado brevemente
- [ ] Demonstração prática realizada
- [ ] Pelo menos uma análise de gastos demonstrada
- [ ] Pelo menos uma meta financeira demonstrada
- [ ] Pelo menos um conceito de educação financeira demonstrado
- [ ] Diferencial explicado
- [ ] Limitações e segurança apresentadas
- [ ] Impacto da solução apresentado
- [ ] Áudio e vídeo com boa qualidade
- [ ] Tela da aplicação legível
- [ ] Demonstração sem informações financeiras pessoais reais
- [ ] Duração final revisada antes da publicação

---

## Sugestão de Estrutura Visual

Para apoiar a gravação, podem ser utilizados aproximadamente **5 slides**:

### Slide 1 — Bolso Inteligente

**Agente de IA para Educação e Organização Financeira**

Problema → Organização → Educação → Planejamento

### Slide 2 — O Problema

- Dificuldade para organizar despesas
- Falta de visão sobre os gastos
- Dificuldade para estabelecer metas
- Dificuldade para compreender conceitos financeiros

### Slide 3 — A Solução

**Bolso Inteligente**

```text
Usuário
   ↓
Streamlit
   ↓
Agente de IA
   ├── Ollama / LLM
   ├── Python
   ├── JSON / CSV
   └── Base de conhecimento
   ↓
Resposta educativa
```

### Slide 4 — Demonstração

Mostrar a aplicação funcionando:

```text
"Quanto gastei com alimentação?"
```

↓

```text
Supermercado     R$ 450,00
Restaurante      R$ 120,00
                 ──────────
Total            R$ 570,00
```

Depois demonstrar:

```text
"Quero juntar R$ 3.000 em 10 meses."
```

↓

```text
Meta mensal: R$ 300,00
```

### Slide 5 — Diferencial e Impacto

**Bolso Inteligente**

- Educação financeira acessível
- Organização dos gastos
- Metas financeiras
- Cálculos transparentes
- Respostas baseadas nos dados disponíveis
- Sem recomendações personalizadas de investimentos
- Sem inventar informações

**Objetivo:** ajudar o usuário a compreender e organizar melhor sua vida financeira.

---

## Link do Vídeo

> Cole aqui o link do pitch após a publicação.

[Link do vídeo]

---

## Observação

O roteiro foi planejado para aproximadamente **3 minutos**, mas o tempo final pode variar de acordo com a velocidade da fala e o tempo utilizado na demonstração.

Recomenda-se realizar pelo menos uma gravação de teste antes da versão final para verificar a duração, a qualidade do áudio e a legibilidade da aplicação.
