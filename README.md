# Nara — BIM Sensei

> Professora de IA especialista em BIM. Assistente, curadora de conhecimento e guia de aprendizado.

```
"Antes de responder, deixa eu te mostrar o contexto na norma..."
                                              — Nara, BIM Sensei
```

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)](https://python.org)
[![Claude](https://img.shields.io/badge/Claude-Sonnet_4.6-teal?style=flat-square)](https://anthropic.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## O que é a Nara

Um agente Claude com **personalidade definida** e **contexto persistente** que serve como:

| Papel | O que faz |
|-------|-----------|
| 🏗 **Assistente BIM** | Responde dúvidas técnicas, analisa IFC, gera relatórios de clash, cita normas ISO 19650 |
| 📚 **Curadora de ferramentas** | Mantém knowledge base de repos GitHub com análise de uso para BIM |
| 🎓 **Professora de IA** | Explica o porquê antes do como, sugere próximo passo, conecta conceitos |

A diferença de um chat comum: a Nara **sabe o contexto do seu projeto**, **lembra das decisões anteriores** e **cresce com você**.

---

## Personalidade

- **Jovem e direta** — sem formalidade excessiva, sem rodeios
- **Sênior de verdade** — aprofunda quando necessário, não simplifica o que é complexo
- **Entusiasta de IA** — genuinamente animada com ferramentas novas, compartilha opinião
- **Especialista BIM** — domina ISO 19650, IFC, CDE, EIR, BEP, LOD/LOI

Como a Nara fala:
> *"Isso que você descreveu é exatamente o §5.3 da ISO 19650-2. Vou traduzir para o seu caso."*
> *"Honestamente? Para esse caso eu usaria LlamaIndex, não LangChain. Te explico por quê."*

---

## Estrutura do projeto

```
nara-bim-sensei/
│
├── CLAUDE.md                     # 🧠 Identidade e contexto persistente da Nara
├── assistant.py                  # 🤖 Loop de conversa principal
│
├── knowledge/
│   ├── repos/
│   │   ├── index.json            # 📚 Banco de dados de repositórios
│   │   └── *.md                  # Análise individual por repo
│   ├── bim/                      # Notas técnicas BIM
│   └── learning/                 # Notas de aprendizado
│
├── .claude/
│   ├── skills/
│   │   ├── bim-clash-report.md   # 🛠 Skill: relatório de clash
│   │   └── add-repo.md           # 🛠 Skill: analisar e adicionar repo
│   ├── agents/                   # Subagentes por disciplina (fase 2)
│   └── commands/                 # Slash commands customizados (fase 2)
│
├── scripts/
│   └── update_knowledge.py       # 🔧 CLI para gerenciar knowledge base
│
└── docs/
    ├── next-steps.md
    ├── skills-created.md
    └── decisions/
```

---

## Setup em 5 minutos

```bash
git clone https://github.com/jeffmodeler/nara-bim-sensei.git
cd nara-bim-sensei
pip install anthropic python-dotenv
```

Crie um `.env` na raiz:
```
ANTHROPIC_API_KEY=sk-ant-...
```

Rode:
```bash
python assistant.py
```

---

## Comandos disponíveis

| Comando | O que faz |
|---------|-----------|
| `/help` | Lista todos os comandos |
| `/repos` | Lista repositórios no knowledge base |
| `/add-repo` | Wizard para adicionar novo repositório |
| `/learn [tema]` | Nara sugere próximo passo de estudo |
| `/save` | Salva insights da sessão em `docs/` |
| `/clear` | Limpa histórico da sessão |
| `/status` | Estado atual do projeto |

---

## Como adicionar um novo repositório

```
# Via conversa com a Nara
você › analise https://github.com/usuario/repo

# Via wizard interativo
você › /add-repo

# Commit
git commit -m "knowledge: add nome-do-repo"
```

---

## Roadmap

### ✅ Fase 1 — Base
- [x] Estrutura e CLAUDE.md com personalidade da Nara
- [x] Knowledge base com 6 repositórios analisados
- [x] Loop de conversa com contexto persistente
- [x] Skills: clash-report, add-repo
- [ ] Configurar API key e primeiro teste

### 🔜 Fase 2 — Skills BIM (semana 2-4)
- [ ] Instalar `everything-claude-code` como plugin
- [ ] Skill: ifc-parser com ifcopenshell
- [ ] Subagentes por disciplina

### 🔜 Fase 3 — RAG (mês 2)
- [ ] LlamaIndex para consultas semânticas
- [ ] Indexar ISO 19650 e documentação do escritório

### 🔜 Fase 4 — Orquestração (mês 3)
- [ ] Maestro para agentes paralelos
- [ ] Playbooks de coordenação BIM

---

## Licença

MIT — use, modifique, expanda. O knowledge base é seu.
