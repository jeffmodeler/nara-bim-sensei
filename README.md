# Nara — BIM Sensei

> Professora de IA especialista em BIM. Assistente, curadora de conhecimento e guia de aprendizado.

```
"Antes de responder, deixa eu te mostrar o contexto na norma..."
                                              — Nara, BIM Sensei
```

## 🌐 Acesso

**→ [https://jeffmodeler.github.io/nara-bim-sensei](https://jeffmodeler.github.io/nara-bim-sensei)**

Senha de acesso: `nara2026`

---

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)](https://python.org)
[![Claude](https://img.shields.io/badge/Claude-Sonnet_4.6-teal?style=flat-square)](https://anthropic.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Site](https://img.shields.io/badge/Site-GitHub_Pages-violet?style=flat-square)](https://jeffmodeler.github.io/nara-bim-sensei)

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
├── assistant.py                  # 🤖 Loop de conversa principal (CLI)
│
├── knowledge/
│   ├── repos/
│   │   ├── index.json            # 📚 Banco de dados de repositórios
│   │   └── *.md                  # Análise individual por repo (Obsidian vault)
│   ├── bim/                      # Notas técnicas BIM
│   └── learning/
│       └── anthropic-learn.md    # Cursos Anthropic Academy
│
├── .obsidian/                    # Configuração do vault Obsidian
│   ├── app.json
│   └── graph.json                # Graph view com colorização por prioridade
│
├── .claude/
│   ├── skills/
│   │   ├── bim-clash-report.md   # 🛠 Skill: relatório de clash
│   │   └── add-repo.md           # 🛠 Skill: analisar e adicionar repo
│   └── commands/                 # Slash commands customizados
│
├── scripts/
│   └── update_knowledge.py       # 🔧 CLI para gerenciar knowledge base
│
└── docs/
    ├── next-steps.md
    └── decisions/
```

---

## Setup em 5 minutos (CLI local)

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

> **Nota sobre API key:** o `assistant.py` (modo CLI local) usa a API da Anthropic, que é paga por uso.
> O **site** (`jeffmodeler.github.io/nara-bim-sensei`) funciona 100% sem API key — o dashboard, os cards,
> o Anthropic Academy tracker e o add-repo funcionam sem custo. O chatbot no site só precisa de API key
> se você quiser respostas com IA real; sem ela, redireciona para os recursos do próprio site.

---

## Usando como Vault Obsidian

Abra a pasta clonada diretamente no Obsidian:

1. Obsidian → "Open folder as vault"
2. Selecione a pasta `nara-bim-sensei/`
3. Acesse Graph View para ver as conexões entre os repositórios

Os arquivos `knowledge/repos/*.md` têm frontmatter YAML e `[[wikilinks]]` prontos.

---

## Comandos disponíveis (CLI)

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

## Roadmap

### ✅ Fase 1 — Base
- [x] Estrutura e CLAUDE.md com personalidade da Nara
- [x] Knowledge base com 7 repositórios analisados
- [x] Dashboard web com login, cards, filtros e matrix
- [x] Anthropic Academy tracker (cursos + disciplinas BIM)
- [x] Chatbot Nara com API key configurável
- [x] Vault Obsidian com wikilinks e graph view
- [x] Add-repo form no dashboard

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
