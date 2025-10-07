# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 07:09:45 2025

@author: Bob
"""

from typing import List, Tuple

Coord = Tuple[int, int]

GLIDER: List[Coord] = [(0,1), (1,2), (2,0), (2,1),(2,2)]
BLINKER: List[Coord] = [(0,0),(0,1), (0,2)]
BLOCK: List[Coord] = [(0,0), (0,1), (1,0), (1,1)]

def translate(pattern: List[Coord], top_left: Coord) -> List[Coord]:
    r0, c0 = top_left
    return [(r0 + dr, c0 + dc) for dr, dc in pattern]

