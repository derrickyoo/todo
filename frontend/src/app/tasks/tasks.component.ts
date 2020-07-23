import { Component, OnInit } from '@angular/core';

import { ITask } from '../core';
import { TaskService } from './task.service';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
})
export class TasksComponent implements OnInit {
  tasks: ITask[];

  constructor(private taskService: TaskService) {}

  ngOnInit() {
    this.taskService
      .getTasks()
      .subscribe((tasks: ITask[]) => (this.tasks = tasks));
  }
}
