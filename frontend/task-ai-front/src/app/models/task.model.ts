export interface Task {
  id: number;
  title: string;
  description?: string;
  status: string;
  priority: string;
  completed: boolean;
  created_at: string;
}

export interface TaskCreate {
  title: string;
  description?: string;
  status?: string;
  priority?: string;
  completed?: boolean;
}

export interface AIGenerateResponse {
  description: string;
  priority: string;
  subtasks: string[];
}