# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 07:16:37 2025

@author: Bob
"""

import time
from .grid import Grid
from typing import Iterable, Tuple

def run_console(grid: Grid, steps: int =50, delay: float = 0.12, clear_screen: bool = True) -> None:
    import os
    for i in range(steps):
        if clear_screen:
            os.system('cls' if os.name == 'nt' else 'clear')
        print(grid)
        print(f"\nstep {i+1}/{steps} - alive: {len(grid.alive_cells())}")
        grid.step()
        time.sleep(delay)