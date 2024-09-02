import numpy as np
from config import Config

class Stage:
    """Class to store and check acts on a stage.
    """
    def __init__(self) -> None:
        self.cfg = Config()
        self.acts = []
        self.times = []
        self.occupied = np.zeros(self.cfg.festival_length, int)

    def add_act(self, act_name: str, t_start: int, t_end: int) -> None:
        """Adds an act to the stage.

        Args:
            act_name (str): act name
            times (List): schedule of the act [t_end, t_start] 
        """
        if self.is_available(t_start, t_end):
           self.acts.append(act_name)
           self.times.append([t_start, t_end])
           self.occupied[t_start: t_end + 1] = 1

        else:
            raise ValueError(f'This stage is occupied from {t_start} until {t_end}')

    def is_available(self, t_start, t_end) -> bool:
        """Check if stage is available between start and end time. Returns True if available, else False.

        Args:
            t_start (int): start time of the act
            t_end (int): end time of the act

        Returns:
            bool: whether the scheduling succeeded. True if successful.
        """
        for t in range(t_start, t_end + 1):
            if self.occupied[t]:
                return False
            
        return True
    
    def __repr__(self) -> str:
        d = [n for n, o in enumerate(self.occupied) if o]
        return f'Stage \n Acts: {self.acts} \n Occupied times: {d}'