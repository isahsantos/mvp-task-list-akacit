# Decisões Técnicas do Projeto

## Linguagem do backend
Foi escolhido Python por ser simples, e por eu já ter um prévio conhecimento de uma pós full stack em que fiz uma api similar para outras finalidades .

## Framework
Foi utilizado FastAPI pela rapidez no desenvolvimento e pela documentação automática via Swagger.

## Banco de dados
SQLite foi escolhido por ser leve e suficiente para um MVP acadêmico e já está previamente instalado e configurado na minha máquina.

## Arquitetura
Foi adotada arquitetura em camadas conforme o sugerido nas videos aulas:
- Controller
- Service
- Repository
- Database

Essa abordagem facilita manutenção, testes e organização do código.

## IA Generativa
A IA foi simulada por uma função local para evitar dependência de APIs externas, custos e necessidade de chave. A estrutura foi preparada para futura integração com OpenAI ou Gemini.

## Testes
Foram utilizados testes unitários com pytest para validar os endpoints principais da API.

## Frontend
Foi utilizado Angular para consumo da API e construção da interface do usuário, devido já ter conhecimento sólido com este framework.