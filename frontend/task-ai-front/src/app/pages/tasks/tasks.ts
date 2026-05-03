import { Component } from '@angular/core';
import { TaskService } from '../../services/task';
import { Task } from '../../models/task.model';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-tasks',
  imports: [CommonModule, FormsModule 
  ],
  templateUrl: './tasks.html',
  styleUrl: './tasks.scss',

})
export class TasksComponent {
tasks: Task[] = [];

  title = '';
  description = '';
  priority = 'media';
  aiResult = '';

  isLoadingTasks = false;
  isCreating = false;
  isGeneratingAI = false;
  feedbackMessage = '';
  errorMessage = '';

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks(): void {
    this.isLoadingTasks = true;

    this.taskService.getTasks().subscribe({
      next: (tasks) => {
        this.tasks = tasks;
        this.isLoadingTasks = false;
      },
      error: () => {
        this.errorMessage = 'Erro ao carregar tarefas.';
        this.isLoadingTasks = false;
      },
    });
  }

  createTask(): void {
    if (!this.title.trim()) {
      this.errorMessage = 'Informe o título da tarefa.';
      return;
    }

    this.isCreating = true;
    this.feedbackMessage = '';
    this.errorMessage = '';

    this.taskService
      .createTask({
        title: this.title,
        description: this.description,
        priority: this.priority,
        status: 'pendente',
        completed: false,
      })
      .subscribe({
        next: () => {
          this.title = '';
          this.description = '';
          this.priority = 'media';
          this.aiResult = '';
          this.feedbackMessage = 'Tarefa criada com sucesso!';
          this.isCreating = false;
          this.loadTasks();
        },
        error: () => {
          this.errorMessage = 'Erro ao criar tarefa.';
          this.isCreating = false;
        },
      });
  }

  generateAI(): void {
    if (!this.title.trim()) {
      this.errorMessage = 'Digite um título para gerar com IA.';
      return;
    }

    this.isGeneratingAI = true;
    this.feedbackMessage = '';
    this.errorMessage = '';

    this.taskService.generateAI(this.title).subscribe({
      next: (response) => {
        this.description = response.description;
        this.priority = response.priority;
        this.aiResult = response.subtasks.join('\n');
        this.feedbackMessage = 'Sugestão gerada com IA!';
        this.isGeneratingAI = false;
      },
      error: () => {
        this.errorMessage = 'Erro ao gerar sugestão com IA.';
        this.isGeneratingAI = false;
      },
    });
  }

  completeTask(id: number): void {
    this.taskService.completeTask(id).subscribe(() => {
      this.feedbackMessage = 'Tarefa concluída!';
      this.loadTasks();
    });
  }

  deleteTask(id: number): void {
    this.taskService.deleteTask(id).subscribe(() => {
      this.feedbackMessage = 'Tarefa excluída!';
      this.loadTasks();
    });
  }
}
