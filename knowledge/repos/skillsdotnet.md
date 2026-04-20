---
title: skillsdotnet
tags: [low, library, csharp, dotnet, mcp]
url: https://github.com/PederHP/skillsdotnet
author: PederHP
priority: low
bim_relevance: medium
use_for_claude_self: false
use_for_agent_memory: true
status: active
date_added: 2026-04-20
---

# skillsdotnet

> Skills em C# via MCP — integração nativa Revit/Navisworks com [[everything-claude-code]]

## O que é

Biblioteca C# para implementar agent skills com integração MCP. Distribui SKILL.md via skill:// URI com carregamento progressivo de contexto.

## Melhora o Claude?

**Não.** Biblioteca de integração — impacto indireto.

## Memória de agente?

**Sim.**
Permite que agentes em ambientes .NET carreguem skills de forma eficiente via MCP.

## Aplicação BIM

- Add-in Revit que expõe parâmetros como MCP resources
- BIM Manager com acesso direto à API Revit
- Integração Navisworks: skills de clash em C#
- Catalog de skills BIM distribuível por times

## Links relacionados

- [[everything-claude-code]] — skills distribuídas via este pacote
- [[maestro]] — agentes que consomem as skills
