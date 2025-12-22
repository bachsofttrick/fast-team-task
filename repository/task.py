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
        
        result = []
        for task in tasks:
            if task.team_id == team_id:
                result.append(task)
        
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
        for old_task in tasks:
            if old_task.id == id:
                old_task.name = task.name
                updated = True
        
        return updated

    @staticmethod
    def delete(id: int) -> bool:
        global tasks
        deleted = False
        new_tasks = []
        for old_task in tasks:
            if old_task.id != id:
                new_tasks.append(old_task)
            else:
                deleted = True
        
        tasks = new_tasks
        return deleted