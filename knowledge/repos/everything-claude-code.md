---
title: everything-claude-code
tags: [high, agent-framework, skills, hooks, claude-code]
url: https://github.com/affaan-m/everything-claude-code
author: affaan-m
stars: 161000
priority: high
bim_relevance: high
use_for_claude_self: true
use_for_agent_memory: true
status: active
date_added: 2026-04-20
---

# everything-claude-code

> Sistema de performance para agentes AI — o core do [[CLAUDE]]

## O que é

Plugin instalável para Claude Code com skills, hooks, regras, comandos e configurações MCP prontas para produção. Suporta Claude Code, Cursor, Codex e OpenCode.

## Melhora o Claude?

**Sim — é o principal mecanismo.**
Regras moldam como o Claude raciocina. Instincts definem comportamentos automáticos por contexto.

## Memória de agente?

**Sim — é o core.**
Skills são capacidades reutilizáveis carregadas automaticamente. Subagentes são especialistas por tarefa com contexto isolado.

## Aplicação BIM

- Skill `ifc-parser` para extração de dados de modelos
- Skill `clash-report` para relatórios automáticos de interferência
- Skill `cobie-export` para geração de COBie a partir de IFC
- Subagente `disciplina-estrutural` com contexto especializado
- Hooks de validação automática pós-modificação de modelo

## Como instalar

```bash
/plugin marketplace add https://github.com/affaan-m/everything-claude-code
/plugin install everything-claude-code@everything-claude-code
```

## Links relacionados

- [[claude-howto]] — guia de uso com templates
- [[CLAUDE]] — identidade da Nara

## Próximos passos

- [ ] Instalar como plugin
- [ ] Criar primeira skill BIM
- [ ] Configurar hooks de sessão
