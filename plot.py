import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from stage import Stage
from typing import List
from matplotlib.axes import Axes

# Set Seaborn style
sns.set(style="whitegrid")

def plot_stages(stages: List[Stage]) -> None:
    """Plots multiple Stage objects as broken bar plots with act names and different colors for each block.
    
    Args:
        stages (List[Stage]): List of Stage instances to be plotted.
    """
    _, ax = plt.subplots(figsize=(12, len(stages) * 1.8))  # Adjusted figsize for better proportions
    y_positions = np.arange(len(stages))
    height = 0.95
    cmap = sns.color_palette('pastel', len(stages))  # Use a soft pastel color palette
    
    for idx, stage in enumerate(reversed(stages)):  # Reversed to number stages from top to bottom
        acts = stage.acts
        times = stage.times
        
        for bar_idx, (act_name, (t_start, t_end)) in enumerate(zip(acts, times)):
            color = cmap[bar_idx % len(cmap)]
            ax.broken_barh([(t_start, t_end - t_start + 1)], (idx - height / 2, height),
                           facecolor=color, edgecolor='black', linewidth=0.8)
            
            add_name_text(ax, act_name, t_start, t_end, idx) 
    
    ax.set_yticks(y_positions)
    ax.set_yticklabels([f'Stage {i+1}' for i in reversed(y_positions)], fontsize=12)
    ax.set_xlabel('Time (hr)', fontsize=14)
    ax.set_title('Stage Schedule', fontsize=16, fontweight='bold')
    
    ax = hide_axes(ax)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey')
    
    plt.tight_layout()
    plt.show()

def hide_axes(ax: Axes) -> Axes:
    """Hides plot axes.
    
    Args:
        ax (Axes): Matplotlib Axes object
    
    Returns:
        Axes: Matplotlib Axes with hidden axes
    """
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    return ax

def add_name_text(ax: Axes, act_name: str, t_start: int, t_end: int, idx: int) -> Axes:
    """_summary_

    Args:
        ax (Axes): Axes object to place the text on
        act_name (str): Act name
        t_start (int): Start time (for width calculation)
        t_end (int): End time 
        idx (int): _description_

    Returns:
        Axes: _description_
    """
    available_width = t_end - t_start
    font_size = min(10, 10 * (available_width / len(act_name)))
    font_size = max(font_size, 6)

    ax.text(t_start + available_width / 2, idx,
        act_name, va='center', ha='center',
        fontsize=font_size, color='black', fontweight='bold', clip_on=True)
    
    return ax