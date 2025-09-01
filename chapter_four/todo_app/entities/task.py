from dataclasses import dataclass, field
from entities.entity import Entity
from value_objects import Deadline, TaskStatus, Priority

@dataclass
class Task(Entity):
    title : str
    description : str
    due_date: Deadline | None = None
    priority : Priority = Priority.MEDIUM
    status : TaskStatus = field(default= TaskStatus.TODO, init=False)

    def start(self) -> None:
        if self.status != TaskStatus.TODO:
            raise ValueError("Only tasks with 'TODO' status can be started")
        self.status = TaskStatus.IN_PROGRESS
    def complete(self) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Task is already completed")
        self.status = TaskStatus.DONE
    def is_overdue(self) -> bool:
        return self.due_date is not None and self.due_date.is_overdue()

# Usage
# Create a new task
task = Task(
    title="Complete project proposal",
    description="Draft and review the proposal for the new client project",
    priority=Priority.HIGH
)
# Check task properties
print(task.title) # "Complete project proposal"
print(task.priority) # Priority.HIGH
print(task.status) # TaskStatus.TODO”

