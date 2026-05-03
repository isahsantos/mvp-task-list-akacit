# Decisões Técnicas do Frontend

## Escolha do Angular

O Angular foi escolhido para o frontend por ser um framework do qual eu já utilizo e tenho como stackprincipal no fornt.

A escolha também foi motivada pela familiaridade com componentização, services, rotas e integração com APIs REST.

## Componentes Standalone

Foram utilizados componentes standalone para simplificar a estrutura do projeto e reduzir a necessidade de módulos tradicionais.

Essa abordagem é recomendada nas versões mais recentes do Angular e deixa o projeto mais direto para um MVP.

## Uso do HttpClient

O HttpClient foi utilizado para realizar a comunicação entre o frontend Angular e a API FastAPI.

Com ele, a aplicação consegue:
- listar tarefas;
- criar tarefas;
- concluir tarefas;
- excluir tarefas;
- chamar o endpoint de IA generativa.

## Escolha do Tailwind CSS

O Tailwind CSS foi escolhido para acelerar a criação da interface visual.

A principal vantagem foi permitir construir uma tela responsiva, moderna e consistente diretamente no HTML, usando classes utilitárias.

Isso ajudou a reduzir a criação de CSS manual e facilitou ajustes rápidos no layout durante o desenvolvimento do MVP.

## Design Responsivo

A interface foi planejada para funcionar em telas maiores e menores.

Foi utilizado grid responsivo para separar:
- formulário de criação de tarefas;
- lista de tarefas cadastradas.

## Estados Visuais

Foram adicionados estados de carregamento e mensagens de feedback para melhorar a experiência do usuário.

A aplicação mostra:
- loading ao carregar tarefas;
- loading ao criar tarefa;
- loading ao gerar sugestão com IA;
- mensagem de sucesso;
- mensagem de erro;
- estado vazio quando não existem tarefas.

## IA no Frontend

O frontend não executa a IA diretamente.

Ele apenas envia o título da tarefa para o backend por meio do endpoint:

POST /tasks/generate-ai

O backend retorna:
- descrição sugerida;
- prioridade;
- subtarefas.

Esses dados são exibidos e preenchidos automaticamente no formulário.