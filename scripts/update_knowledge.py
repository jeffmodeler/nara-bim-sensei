#!/usr/bin/env python3
"""
update_knowledge.py - Gerencia o knowledge base da Nara.
Uso:
  python scripts/update_knowledge.py --list
  python scripts/update_knowledge.py --repo everything-claude-code
  python scripts/update_knowledge.py --validate
"""
import json
import argparse
import sys
from pathlib import Path

ROOT        = Path(__file__).parent.parent
REPOS_INDEX = ROOT / "knowledge" / "repos" / "index.json"
REPOS_DIR   = ROOT / "knowledge" / "repos"

def list_repos():
    data = json.loads(REPOS_INDEX.read_text())
    print(f"\n  {'ID':<32} {'PRIO':<8} {'CLAUDE':<8} {'AGENTE':<8} BIM")
    print("  " + "-" * 66)
    for r in data["repos"]:
        c = "S" if r["use_for_claude_self"] else "N"
        a = "S" if r["use_for_agent_memory"] else "N"
        print(f"  {r['id']:<32} {r['priority']:<8} {c:<8} {a:<8} {r['bim_relevance']}")
    print(f"\n  Total: {len(data['repos'])} | Atualizado: {data['last_updated']}\n")

def show_repo(repo_id: str):
    data = json.loads(REPOS_INDEX.read_text())
    repo = next((r for r in data["repos"] if r["id"] == repo_id), None)
    if not repo:
        print(f"  Repositorio '{repo_id}' nao encontrado.")
        sys.exit(1)
    print(json.dumps(repo, ensure_ascii=False, indent=2))
    analysis = REPOS_DIR / f"{repo_id}.md"
    if analysis.exists():
        print(f"\n{'-'*60}\n{analysis.read_text()}")

def validate():
    data = json.loads(REPOS_INDEX.read_text())
    errors = []
    required = ["id","url","category","priority","use_for_claude_self","use_for_agent_memory","bim_relevance","tags","status"]
    for r in data["repos"]:
        for field in required:
            if field not in r:
                errors.append(f"[{r.get('id','?')}] Campo ausente: {field}")
        if not (REPOS_DIR / f"{r['id']}.md").exists():
            errors.append(f"[{r['id']}] Arquivo .md ausente")
    if errors:
        print(f"\n  {len(errors)} problema(s):")
        for e in errors: print(f"    - {e}")
    else:
        print(f"\n  OK - {len(data['repos'])} repos validos\n")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--list",     action="store_true")
    p.add_argument("--repo",     type=str)
    p.add_argument("--validate", action="store_true")
    args = p.parse_args()
    if args.list:       list_repos()
    elif args.repo:     show_repo(args.repo)
    elif args.validate: validate()
    else:               p.print_help()

if __name__ == "__main__":
    main()
