import csv
import numpy as np
from pathlib import Path
from typing import Tuple, List
from numpy.typing import NDArray

def load_csv_to_arrays(file_name: str) -> Tuple[List, NDArray]:
    """Loads input data from a CSV file. 

    Args:
        file_name (str): name of the CSV-file. Full path is not required.

    Returns:
        act_names (List): List containing act names.
        times (NDArray): Array of size (N,2) containing start and end times.
    """
    act_names = []
    times = []
    data_dir = Path(__file__).resolve().parent / 'data'
    file_path = data_dir / file_name

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            act_names.append(row['act_name'])
            times.append([int(row['t_start']), int(row['t_end'])])

        times = np.array(times)
        validate_data(times, act_names)
    
    return act_names, times

def validate_data(times, act_names):
    """Validates output data for most common errors.

    Args:
        times (NDArray): (N,2) array of start and end times.
        act_names (List): list of string act names.

    Raises:
        ValueError: If times and act names are not of the same length.
        ValueError: If end times are not always after start times.
    """
    if (nt:=len(times)) != (na:=len(act_names)):
        raise ValueError(f'Times and act names should have the same length. Found {nt} times and {na} act names.')
    for n, (t_start, t_end) in enumerate(times):
        if t_end <= t_start:
            raise ValueError(f'End times cannot be before start times. Check act {n}: {act_names[n]}')