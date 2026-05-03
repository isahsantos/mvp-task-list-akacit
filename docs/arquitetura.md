# Arquitetura do Projeto

A aplicação segue o padrão em camadas:

Client (Angular)
↓
Controller (FastAPI)
↓
Service (regras de negócio)
↓
Repository (acesso ao banco)
↓
Database (SQLite)

A camada de IA é chamada dentro do Service.