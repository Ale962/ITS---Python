
def check_key(key: str, dict: dict):

    if key in dict:
        return True
    else:
        return False


class TaskManager:

    def __init__(self, task: dict[str, dict[str, str|bool]] = {}) -> None:
        self.__task: dict[str, dict[str, str|bool]] = task
    
    def createTask(self, task_id: str, descrizione: str) -> dict[str, str|bool]|str:

        if self.__task:
            if not check_key(task_id, self.__task):
                task_dict: dict[str, str|bool] = {
                    'descrizione': descrizione,
                    'compleatato': False
                }
                self.__task[task_id] = task_dict
                return self.__task[task_id]
            else:
                return 'Errore task esiste già'
        else:
            task_dict: dict[str, str|bool] = {
                'descrizione': descrizione,
                'compleatato': False
            }
            self.__task[task_id] = task_dict
            return self.__task[task_id]

    def completeTask(self, task_id: str) -> dict[str, dict[str, str|bool]]|str:
        
        if check_key(task_id, self.__task):
            self.__task[task_id]['completato'] = True
            return {task_id: self.__task[task_id]}
        else:
            return 'Task non presente'
        
    def updateDescription(self, task_id: str, nuova_descrizione: str) -> dict[str, dict[str, str|bool]]|str:

        if check_key(task_id, self.__task):
            self.__task[task_id]['descrizione'] = nuova_descrizione
            return {task_id: self.__task[task_id]}
        else:
            return 'Task non presente'
        
    def removeTask(self, task_id: str) -> dict[str, dict[str, str|bool]]|str:

        if check_key(task_id, self.__task):
            value = self.__task.pop(task_id)
            return {task_id: value}
        else:
            return 'Task non presente'
        
    def listTask(self) -> list[str]:

        list_key: list[str] = [key for key in self.__task]
        return list_key
    
    def getTask(self, task_id: str) -> dict[str, dict[str, str|bool]]|str:

        if check_key(task_id, self.__task):
            return {task_id: self.__task[task_id]}
        else:
            return 'Task non presente'