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

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks(): void {
    this.taskService.getTasks().subscribe((tasks) => {
      this.tasks = tasks;
    });
  }

  createTask(): void {
    if (!this.title.trim()) {
      alert('Informe o título da tarefa');
      return;
    }

    this.taskService.createTask({
      title: this.title,
      description: this.description,
      priority: this.priority,
      status: 'pendente',
      completed: false,
    }).subscribe(() => {
      this.title = '';
      this.description = '';
      this.priority = 'media';
      this.aiResult = '';
      this.loadTasks();
    });
  }

  generateAI(): void {
    if (!this.title.trim()) {
      alert('Digite um título para gerar com IA');
      return;
    }

    this.taskService.generateAI(this.title).subscribe((response) => {
      this.description = response.description;
      this.priority = response.priority;
      this.aiResult = response.subtasks.join('\n');
    });
  }

  completeTask(id: number): void {
    this.taskService.completeTask(id).subscribe(() => {
      this.loadTasks();
    });
  }

  deleteTask(id: number): void {
    this.taskService.deleteTask(id).subscribe(() => {
      this.loadTasks();
    });
  }

}
