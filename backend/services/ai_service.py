def generate_task_with_ai(title: str):
    return {
        "description": f"Descrição gerada automaticamente para a tarefa: {title}",
        "priority": "alta",
        "subtasks": [
            f"Pesquisar sobre {title}",
            f"Organizar os passos para {title}",
            f"Executar a tarefa {title}",
            "Revisar o resultado final"
        ]
    }