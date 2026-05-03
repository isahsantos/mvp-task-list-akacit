import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of } from 'rxjs';
import { TasksComponent } from './tasks';
import { TaskService } from '../../services/task';

describe('TasksComponent', () => {
  let component: TasksComponent;
  let fixture: ComponentFixture<TasksComponent>;
  let taskServiceMock: jasmine.SpyObj<TaskService>;

  beforeEach(async () => {
    taskServiceMock = jasmine.createSpyObj('TaskService', [
      'getTasks',
      'createTask',
      'deleteTask',
      'completeTask',
      'generateAI',
    ]);

    taskServiceMock.getTasks.and.returnValue(of([]));

    await TestBed.configureTestingModule({
      imports: [TasksComponent],
      providers: [
        {
          provide: TaskService,
          useValue: taskServiceMock,
        },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(TasksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('deve criar o componente', () => {
    expect(component).toBeTruthy();
  });

  it('deve carregar tarefas ao iniciar', () => {
    expect(taskServiceMock.getTasks).toHaveBeenCalled();
  });

  it('deve criar uma tarefa', () => {
    component.title = 'Estudar Angular';
    component.description = 'Criar frontend do MVP';
    component.priority = 'alta';

    taskServiceMock.createTask.and.returnValue(
      of({
        id: 1,
        title: 'Estudar Angular',
        description: 'Criar frontend do MVP',
        status: 'pendente',
        priority: 'alta',
        completed: false,
        created_at: new Date().toISOString(),
      })
    );

    component.createTask();

    expect(taskServiceMock.createTask).toHaveBeenCalledWith({
      title: 'Estudar Angular',
      description: 'Criar frontend do MVP',
      priority: 'alta',
      status: 'pendente',
      completed: false,
    });

    expect(component.feedbackMessage).toBe('Tarefa criada com sucesso!');
  });

  it('deve gerar sugestão com IA', () => {
    component.title = 'Criar apresentação do MVP';

    taskServiceMock.generateAI.and.returnValue(
      of({
        description: 'Descrição gerada pela IA',
        priority: 'alta',
        subtasks: ['Criar slides', 'Preparar demo'],
      })
    );

    component.generateAI();

    expect(taskServiceMock.generateAI).toHaveBeenCalledWith(
      'Criar apresentação do MVP'
    );
    expect(component.description).toBe('Descrição gerada pela IA');
    expect(component.priority).toBe('alta');
    expect(component.aiResult).toContain('Criar slides');
  });

  it('deve concluir uma tarefa', () => {
    taskServiceMock.completeTask.and.returnValue(
      of({
        id: 1,
        title: 'Tarefa teste',
        description: 'Descrição',
        status: 'concluida',
        priority: 'media',
        completed: true,
        created_at: new Date().toISOString(),
      })
    );

    component.completeTask(1);

    expect(taskServiceMock.completeTask).toHaveBeenCalledWith(1);
    expect(component.feedbackMessage).toBe('Tarefa concluída!');
  });

  it('deve excluir uma tarefa', () => {
    taskServiceMock.deleteTask.and.returnValue(
      of({
        message: 'Tarefa excluída com sucesso',
      })
    );

    component.deleteTask(1);

    expect(taskServiceMock.deleteTask).toHaveBeenCalledWith(1);
    expect(component.feedbackMessage).toBe('Tarefa excluída!');
  });

  it('deve mostrar erro se tentar criar sem título', () => {
    component.title = '';

    component.createTask();

    expect(component.errorMessage).toBe('Informe o título da tarefa.');
    expect(taskServiceMock.createTask).not.toHaveBeenCalled();
  });

  it('deve mostrar erro se tentar gerar IA sem título', () => {
    component.title = '';

    component.generateAI();

    expect(component.errorMessage).toBe('Digite um título para gerar com IA.');
    expect(taskServiceMock.generateAI).not.toHaveBeenCalled();
  });
});