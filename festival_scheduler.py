import numpy as np

from utils import load_csv_to_arrays
from config import Config
from typing import List
from stage import Stage

class FestivalScheduler:
    """Festival scheduling class that loads a CSV-file containing act names, start times and end times and sorts the according act in as few as possible stages.
    """
    def __init__(self) -> None:
        self.cfg = Config()
        self.act_names, self.times = load_csv_to_arrays(self.cfg.data_path)
        self.stages: List[Stage] = [Stage()]

    def schedule(self) -> None:
        """Main function for the FestivalScheduler. Sorts acts according to end time (first) and start time (second) using NumPy lexsort. 
        """
        idx = np.lexsort((self.times[:, 1], self.times[:, 0]))
        self.times = self.times[idx]
        self.act_names = [self.act_names[i] for i in idx]

        for n, (t_start, t_end) in enumerate(self.times):
            for stage in self.stages:
                if stage.is_available(t_start, t_end):
                    stage.add_act(self.act_names[n], t_start, t_end)
                    break
            else:
                new_stage = Stage()
                new_stage.add_act(self.act_names[n], t_start, t_end)
                self.stages.append(new_stage)