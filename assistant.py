#!/usr/bin/env python3
"""
Nara — BIM Sensei
Professora de IA especialista em BIM.
Assistente, curadora de conhecimento e guia de aprendizado.

Uso: python assistant.py
Deps: pip install anthropic python-dotenv
Config: crie .env com ANTHROPIC_API_KEY=sk-ant-...
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("\n  Instale: pip install anthropic python-dotenv\n")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

ROOT        = Path(__file__).parent
KNOWLEDGE   = ROOT / "knowledge"
REPOS_INDEX = KNOWLEDGE / "repos" / "index.json"
DOCS_DIR    = ROOT / "docs"
SKILLS_DIR  = ROOT / ".claude" / "skills"
CLAUDE_MD   = ROOT / "CLAUDE.md"

client = Anthropic()

BANNER = """
╔══════════════════════════════════════════════════════════╗
║  Nara — BIM Sensei  ·  v0.1.0                           ║
║  Professora de IA  ·  Especialista BIM  ·  Claude API   ║
║  /help para ver todos os comandos                       ║
╚══════════════════════════════════════════════════════════╝
"""


def load_system_prompt() -> str:
    parts = []
    if CLAUDE_MD.exists():
        parts.append(CLAUDE_MD.read_text())
    if REPOS_INDEX.exists():
        data = json.loads(REPOS_INDEX.read_text())
        active = [r for r in data["repos"] if r["status"] == "active"]
        section = "\n## Repositórios ativos no knowledge base\n"
        for r in active:
            c = "✓" if r["use_for_claude_self"] else "✗"
            a = "✓" if r["use_for_agent_memory"] else "✗"
            section += f"\n- **{r['id']}** ({r['priority']}) | Claude: {c} | Agente: {a}"
            if r.get("notes"):
                section += f" — {r['notes']}"
        parts.append(section)
    if SKILLS_DIR.exists():
        skills = list(SKILLS_DIR.glob("*.md"))
        if skills:
            parts.append("\n## Skills disponíveis\n" + "\n".join(f"- `{s.stem}`" for s in skills))
    ns = DOCS_DIR / "next-steps.md"
    if ns.exists():
        parts.append("\n## Próximos passos\n" + ns.read_text())
    return "\n\n---\n\n".join(parts)


def load_history() -> list:
    f = ROOT / ".session.json"
    if f.exists():
        try:
            return json.loads(f.read_text())
        except Exception:
            return []
    return []

def save_history(h: list):
    (ROOT / ".session.json").write_text(json.dumps(h, ensure_ascii=False, indent=2))

def clear_history():
    f = ROOT / ".session.json"
    if f.exists():
        f.unlink()


def cmd_help():
    print("""
╭─ Comandos da Nara ──────────────────────────────────────────╮
│  /help           Este menu                                  │
│  /repos          Lista repositórios no knowledge base       │
│  /add-repo       Wizard para adicionar novo repositório     │
│  /learn [tema]   Próximo passo de aprendizado               │
│  /save           Salva sessão em docs/                      │
│  /clear          Limpa histórico da sessão                  │
│  /status         Estado atual do projeto                    │
╰─────────────────────────────────────────────────────────────╯
""")

def cmd_repos():
    if not REPOS_INDEX.exists():
        print("  knowledge base nao encontrado.\n")
        return
    data = json.loads(REPOS_INDEX.read_text())
    print(f"\n  {'ID':<32} {'PRIO':<8} {'CLAUDE':<8} {'AGENTE':<8} BIM")
    print("  " + "─" * 64)
    for r in data["repos"]:
        c = "✓" if r["use_for_claude_self"] else "✗"
        a = "✓" if r["use_for_agent_memory"] else "✗"
        b = {"high":"●","medium":"◐","low":"○"}.get(r["bim_relevance"],"?")
        print(f"  {r['id']:<32} {r['priority']:<8} {c:<8} {a:<8} {b} {r['bim_relevance']}")
    print(f"\n  Total: {len(data['repos'])} repos . Atualizado: {data['last_updated']}\n")

def cmd_status():
    repos  = json.loads(REPOS_INDEX.read_text())["repos"] if REPOS_INDEX.exists() else []
    skills = list(SKILLS_DIR.glob("*.md")) if SKILLS_DIR.exists() else []
    docs   = list(DOCS_DIR.glob("session-*.md")) if DOCS_DIR.exists() else []
    key_ok = "✓ configurada" if os.environ.get("ANTHROPIC_API_KEY") else "✗ ausente (.env)"
    print(f"""
  Nara BIM Sensei — Status
  Repositorios:    {len(repos)}
  Skills:          {len(skills)}
  Sessoes salvas:  {len(docs)}
  API key:         {key_ok}
""")

def cmd_add_repo():
    print("\n  Adicionar repositorio ao knowledge base")
    url   = input("  URL do GitHub: ").strip()
    name  = input("  ID (kebab-case): ").strip()
    prio  = input("  Prioridade (high/medium/low) [medium]: ").strip() or "medium"
    notes = input("  Nota rapida: ").strip()
    if not name or not url:
        print("  URL e ID sao obrigatorios.\n")
        return
    data = json.loads(REPOS_INDEX.read_text())
    if any(r["id"] == name for r in data["repos"]):
        print(f"  '{name}' ja existe.\n")
        return
    data["repos"].append({
        "id": name, "url": url,
        "author": url.split("/")[-2] if "/" in url else "",
        "stars": None, "category": "new", "priority": prio,
        "use_for_claude_self": False, "use_for_agent_memory": False,
        "bim_relevance": "medium", "tags": [], "bim_use_cases": [],
        "status": "active", "notes": notes
    })
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    REPOS_INDEX.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    md = KNOWLEDGE / "repos" / f"{name}.md"
    md.write_text(f"# {name}\n\n**URL**: {url}\n**Adicionado**: {datetime.now().strftime('%Y-%m-%d')}\n\n## O que e\n\n## Aplicacao BIM\n\n## Melhora o Claude?\n\n## Memoria de agente?\n")
    print(f"  '{name}' adicionado.\n  knowledge/repos/{name}.md criado.\n  git commit -m 'knowledge: add {name}'\n")

def cmd_save(history: list):
    if not history:
        print("  Sem historico para salvar.\n")
        return
    DOCS_DIR.mkdir(exist_ok=True)
    date = datetime.now().strftime("%Y-%m-%d-%H%M")
    f = DOCS_DIR / f"session-{date}.md"
    content = f"# Sessao {date}\n\n"
    for m in history:
        role = "**Voce**" if m["role"] == "user" else "**Nara**"
        content += f"### {role}\n{m['content']}\n\n"
    f.write_text(content)
    print(f"  Sessao salva em docs/session-{date}.md\n")

def handle_command(cmd: str, history: list) -> bool:
    c = cmd.strip()
    if c == "/help":      cmd_help();    return True
    if c == "/repos":     cmd_repos();   return True
    if c == "/status":    cmd_status();  return True
    if c == "/add-repo":  cmd_add_repo(); return True
    if c == "/clear":     clear_history(); print("  Sessao limpa.\n"); return True
    if c == "/save":      cmd_save(history); return True
    if c.startswith("/learn"):
        topic = c.replace("/learn", "").strip() or "proximo passo geral"
        history.append({"role": "user", "content": f"Como minha professora de IA e BIM, sugira meu proximo passo de aprendizado sobre: {topic}. Leve em conta os repositorios disponiveis e o contexto atual do projeto."})
        return False
    return False


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\n  ANTHROPIC_API_KEY nao encontrada.\n  Crie .env com: ANTHROPIC_API_KEY=sk-ant-...\n")
        sys.exit(1)
    print(BANNER)
    system  = load_system_prompt()
    history = load_history()
    if history:
        print(f"  Sessao anterior carregada ({len(history)} mensagens)\n")
    while True:
        try:
            user_input = input("voce > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Ate logo! - Nara\n")
            save_history(history)
            break
        if not user_input:
            continue
        if user_input.startswith("/"):
            if handle_command(user_input, history):
                continue
        else:
            history.append({"role": "user", "content": user_input})
        try:
            resp = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=4096,
                system=system,
                messages=history
            )
            msg = resp.content[0].text
            history.append({"role": "assistant", "content": msg})
            save_history(history)
            print(f"\nNara > {msg}\n")
        except Exception as e:
            print(f"\n  Erro na API: {e}\n")

if __name__ == "__main__":
    main()
