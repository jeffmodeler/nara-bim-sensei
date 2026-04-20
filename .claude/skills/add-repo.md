---
name: add-repo
description: Analisa e adiciona repositorio GitHub ao knowledge base da Nara. Ativar quando usuario compartilhar URL GitHub, mencionar nova ferramenta ou perguntar se algo se encaixa no workflow BIM.
---

# Skill: Add Repository

## Quando usar
- Usuario compartilha URL de GitHub
- Menciona ferramenta ou biblioteca nova
- Pergunta "isso se encaixa no meu workflow BIM?"

## Triagem rapida

- [ ] Ja existe algo similar no knowledge base?
- [ ] Tem manutencao ativa (commits recentes)?
- [ ] Resolve um problema real do workflow BIM atual?

## Analise estruturada

1. O que faz em uma frase?
2. Melhora o proprio Claude (comportamento, regras, skills)?
3. E util como memoria de agente (contexto persistente, skills, playbooks)?
4. Relevancia BIM: alta / media / baixa
5. Esforco de setup: baixo (<1h) / medio / alto (>8h)
6. Propor 3 casos de uso BIM concretos
7. Posicao recomendada no roadmap

## Formato de resposta

```
Analise: [nome]
O que e: [1 frase]
Melhora o Claude? [Sim/Nao/Parcial] - [motivo]
Memoria de agente? [Sim/Nao/Parcial] - [motivo]
Relevancia BIM: [Alta/Media/Baixa]

3 casos de uso BIM:
1. [caso concreto]
2. [caso concreto]
3. [caso concreto]

Recomendacao: [Adicionar agora / Estudar depois / Nao prioritario]
Para adicionar: /add-repo no assistente
```
