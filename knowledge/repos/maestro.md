---
title: maestro
tags: [medium, orchestrator, multi-agent, playbooks]
url: https://github.com/its-maestro-baby/maestro
author: its-maestro-baby
priority: medium
bim_relevance: medium
use_for_claude_self: false
use_for_agent_memory: true
status: active
date_added: 2026-04-20
---

# maestro

> Orquestrador multi-agente — Bloomberg Terminal para [[everything-claude-code]]

## O que é

Desktop app (Tauri/Rust) para orquestrar múltiplos agentes CLI em paralelo. Bloomberg Terminal para agentes com playbooks, remote mobile e sessões longas autônomas.

## Melhora o Claude?

**Não.** Orquestrador externo — não modifica o comportamento interno do Claude.

## Memória de agente?

**Sim.**
Playbooks persistem workflows. Worktrees isolados por disciplina. Histórico completo.

## Aplicação BIM

- 3 agentes paralelos: estrutural, MEP, arquitetura
- Playbook de coordenação semanal automatizado
- Sessões overnight para processar modelo completo
- Group Chat para decisões de coordenação entre disciplinas

## Links relacionados

- [[everything-claude-code]] — agentes gerenciados pelo Maestro
- [[llm-engineer-toolkit]] — stack dos agentes orquestrados
