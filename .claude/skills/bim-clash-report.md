---
name: bim-clash-report
description: Gera relatorio estruturado de clash detection. Ativar quando usuario mencionar clash, interferencia, colisao ou relatorio de disciplina.
---

# Skill: BIM Clash Report

## Quando usar
- Usuario menciona clash, interferencia ou colisao entre disciplinas
- Ha dados de clash em formato texto, CSV ou lista
- Pedido de relatorio de coordenacao BIM

## Como executar

1. Identificar disciplinas envolvidas (estrutural, MEP, arquitetura)
2. Categorizar por severidade: critico / alto / medio / baixo
3. Agrupar por zona (pavimento, bloco, area tecnica)
4. Gerar tabela: ID, disciplinas, localizacao, severidade, responsavel, acao
5. Recomendar acao para cada clash critico/alto
6. Sumario executivo em 3-5 linhas

## Template de saida

```
# Relatorio de Clash Detection
Data: [data] | Projeto: [nome] | Modelo: [versao IFC]

Sumario
- Total: X | Criticos: X | Altos: X | Medios: X | Baixos: X

Clashes criticos e altos
| ID | Disc. A | Disc. B | Local | Severidade | Responsavel | Acao |
```

## Notas
- Referenciar ISO 19650-3 para gestao de informacao em clash
- Sugerir criacao de BCF para cada clash critico
- Se severidade nao informada: perguntar antes de classificar
