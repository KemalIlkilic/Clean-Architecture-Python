import datetime
from datetime import datetime, timedelta, timezone

from services.task_priority_calculator import TaskPriorityCalculator
from entities.task import Task
from value_objects import Deadline, Priority

# Create a new task
task = Task(
    title="Complete project proposal",
    description="Draft and review the proposal for the new client project",
    priority=Priority.HIGH,
    due_date= Deadline(
        datetime.now(timezone.utc) + timedelta(days=7)
        )
)

asd = TaskPriorityCalculator.calculate_priority(task)

