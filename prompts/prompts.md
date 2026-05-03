
---

# 🤖 6. DOCUMENTAÇÃO DOS PROMPTS

---

## Prompt 1

`prompts/01-criacao-api.md`

```md
# Prompt 01 — Criação da API

Crie uma API REST em Python usando FastAPI para um CRUD de tarefas.

Requisitos:
- criar tarefa
- listar tarefas
- atualizar tarefa
- excluir tarefa
- marcar como concluída

A entidade deve ter:
id, title, description, status, priority, completed, created_at

Use SQLite, SQLAlchemy e Pydantic.



# Prompt 02 — Arquitetura

Refatore a API para arquitetura em camadas:

- Controller
- Service
- Repository

Fluxo:
Client → Controller → Service → Repository → Database

Manter código organizado e desacoplado.  

# Prompt 03 — IA Generativa

Adicione um endpoint:

POST /tasks/generate-ai

Entrada:
title

Saída:
description, priority, subtasks

Simular a IA com função local.

# Prompt 04 — Testes

Crie testes unitários com pytest para:

- criação
- listagem
- atualização
- exclusão
- IA

Validar status e resposta.