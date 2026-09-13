from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseEngine(ABC):
    def __init__(self, job_id: int, aoi_id: int, dam_id: int, breach_params: Dict[str, Any]):
        self.job_id = job_id
        self.aoi_id = aoi_id
        self.dam_id = dam_id
        self.breach_params = breach_params

    @abstractmethod
    def prepare_inputs(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def parse_outputs(self):
        pass
