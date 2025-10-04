# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 15:40:17 2025

@author: Bob
"""

from __future__ import annotations
from typing import Iterable, List, Tuple, Sequence, Optional
import random

Coord = Tuple[int, int]

class Grid:
    
    def __init__(self, rows: int, cols: int, wrap: bool = True):
        assert rows > 0 and cols > 0
        self.rows = rows
        self.cols = cols
        self.wrap = wrap
        self._cells: List[List[int]] = [[0] * cols for _ in range(rows)]
        
    def get(self, r: int, c: int) -> int:
        return self._cells[r][c]
    
    def set(self, r: int, c: int, value: int = 1) -> None:
        self._cells[r][c] = 1 if value else 0
        
    def toggle(self, r: int, c: int) -> None:
        self.cells[r][c] ^= 1
        
    def clear(self) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                self._cells[r][c] = 0
                
    def randomize(self, p_alive: float = 0.2, seed: Optional[int] = None) -> None:
        if seed is not None:
            random.seed(seed)
        for r in range(self.rows):
            for c in range(self.cols):
                self._cells[r][c] = 1 if random.random() < p_alive else 0
                

    @classmethod
    def from_coords(cls, rows: int, cols: int, coords: Iterable[Coord], wrap: bool = True) -> "Grid":
        g = cls(rows, cols, wrap=wrap)
        for r, c in coords:
            if 0 <= r < rows and 0 <= c <cols:
                g.set(r, c, 1)
        return g
    
    @classmethod
    def from_strings(cls, lines: Sequence[str], wrap: bool = True) -> "Grid":
        rows = len(lines)
        cols = max(len(line) for line in lines)
        g = cls(rows, cols, wrap=wrap)
        for r, line in enumerate(lines):
            for c, ch in enumerate(lines):
                if ch in ("O", "X", "1"):
                    g.set(r, c, 1)
        return g
    
    @classmethod
    def to_string(self, alive_char: str = "O", dead_char: str = ".") -> str:
        lines = []
        for r in range(self.rows):
            lines.append(''.join(alive_char if self._cells[r][c] else dead_char for c in range(self.cols)))
        return '\n'.join(lines)