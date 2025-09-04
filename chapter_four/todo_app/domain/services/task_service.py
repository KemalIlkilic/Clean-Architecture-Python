#This TaskService demonstrates how domain logic can interact with the persistence abstraction without knowing anything about the actual storage mechanism.
#The concrete implementation of the TaskRepository would reside in an outer layer, such as the Infrastructure layer:

from todo_app.domain.entities.task import Task
from todo_app.domain.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository
        
    def create_task(self, title: str, description: str) -> Task:
        task = Task(title, description)
        self.task_repository.save(task)
        return task
    
    def mark_task_as_complete(self, task_id: str) -> Task:
        task = self.task_repository.get(task_id)
        task.complete()
        self.task_repository.save(task)
        return task