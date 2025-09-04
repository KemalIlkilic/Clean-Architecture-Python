#“This abstract class defines the contract for task persistence without specifying any implementation details

from abc import ABC, abstractmethod
from todo_app.domain.entities.task import Task
class TaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task):
        pass
    @abstractmethod
    def get(self, task_id: str) -> Task:
        pass