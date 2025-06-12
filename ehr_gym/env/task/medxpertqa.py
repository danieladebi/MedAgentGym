from .base import AbstractEHRTask

class MedXpertQATask(AbstractEHRTask):
    # TODO: complete this
    permitted_actions = ['request_info', 'validate_code', 'debug']
    def __init__(
        self,
        task_id: int,
        data_path: str = None,
        debugger_config: dict = None,
        mode: str = "test",
    ) -> None:
        super().__init__(task_id=task_id)
        self.task_id = task_id
        self.task_list = None
        self.data_path = data_path
        self.debugger_config = debugger_config
        self.mode = mode

    @classmethod
    def get_task_id(cls):
        # Get the class name and remove the word 'Task' from the end if it exists
        class_name = cls.__name__.replace("Task", "")
        # Convert CamelCase to hyphen-separated format
        formatted_name = "".join(
            ["-" + c.lower() if c.isupper() else c for c in class_name]
        ).lstrip("-")
        return f"EHRGym.medxpertqa.{formatted_name}"

    def setup(self) -> tuple[str, dict]:
        """
        Set up the task

        Parameters:
        -----------------
        data_path: str
            Path to the data directory
        """
        raise NotImplementedError

     def setup_goal(self) -> tuple[str, dict]:
        """
        Set up the goal and info for the task

        Parameters:
        -----------------
        data_path: str
            Path to the data directory
        """
        raise NotImplementedError
        
    def _get_obs(self) -> dict:
        raise NotImplementedError
        
    


    