from models.task import Task

tasks = []
count = 1

task1 = Task(id=1, title='test task')
tasks.append(task1)

class TaskRepo():
    @staticmethod
    def getByTeamId(team_id: int | None = None) -> list[Task]:
        if team_id is None:
            return tasks
        
        result = [task for task in tasks if task.team_id == team_id]        
        return result

    @staticmethod
    def get(id: int) -> Task:
        # This is like FirstOrDefault of C# or find of JS
        result = next((task for task in tasks if task.id == id), None)
        return result

    @staticmethod
    def getAll() -> list[Task]:
        return tasks

    @staticmethod
    def add(task: Task) -> int:
        global count
        count += 1
        task.id = count
        tasks.append(task)
        return count

    @staticmethod
    def update(id: int, task: Task) -> bool:
        updated = False
        result = next((task for task in tasks if task.id == id), None)
        if result is not None:
            result.name = task.name
            updated = True
        
        return updated

    @staticmethod
    def delete(id: int) -> bool:
        global tasks
        new_tasks = [task for task in tasks if task.id != id]
        deleted = len(new_tasks) != len(task)
        tasks = new_tasks
        return deleted