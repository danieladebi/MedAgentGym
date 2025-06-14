from .base import AbstractEHRTask

instruction = """You are an biomedical expert in handling EHR data and answer questions accordingly. 
Please answer the following multiple-choice questions."""

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
        if self.task_list is None:
            task_file = 'medxpertqa_mm_input.jsonl'
            task_path = os.path.join(self.data_path, task_file)
            self.task_list = []
            with open(task_path, 'r') as f:
                for line in f:
                    self.task_list.append(json.loads(line))

        task_data = self.task_list[self.task_id]
        self.question = task_data["question"]
        self.id = task_data["id"]
        self.label = task_data["label"][0]
        self.medical_task = task_data["medical_task"]
        self.body_system = task_data["body_system"]
        self.question_type = task_data["question_type"]
        self.options = task_data["options"]
        self.images = task_data["images"]

        goal, info = self.setup_goal()

        return goal, info

     def setup_goal(self) -> tuple[str, dict]:
        """
        Set up the goal and info for the task

        Parameters:
        -----------------
        data_path: str
            Path to the data directory
        """
        self.goal = self.question
        info = {
            "id": self.id,
            "medical_task": self.medical_task,
            "body_system": self.body_system,
            "question_type": self.question_type,
            "options": self.options,
            "images": self.images
        }
        return goal, info
        
    def _get_obs(self) -> dict:
        obs = {}
        obs["type"] = "initial_observation"
        obs["info"] = {}
        

        raise NotImplementedError

    def validate(self, chat_messages, obs):

        raise NotImplementedError
    


    