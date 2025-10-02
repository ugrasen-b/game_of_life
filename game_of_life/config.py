# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 15:44:03 2025

@author: Bob
"""

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, field_validator, ValidationError

Pattern = Literal["glider", "blinker", "block", "random"]

class SimulationConfig(BaseModel):
    rows: int  = Field(20, ge=1, le=2000, description="Number of grid rows")
    cols: int = Field(60, ge=1, le=2000, description="Number of grid columns")
    wrap: bool = Field(True, description="Wrap edges (toroidal) when True")
    steps: int = Field(200, ge=1, description="Number of simulation steps to run")
    delay: float = Field(0.08,ge=0.0,description="Delay between steps in seconds")
    pattern: Pattern = Field("glider", description="Initial pattern to place")
    seed: int | None = Field(None, description="Optional RNG seed for reproducibility")
    
    @field_validator("delay")
    @classmethod
    def clamp_deplay(cls, v: float) -> float:
        if v<0:
            raise ValueError("Delay can not be negative, unless you have a time machine")
        return max(v, 0.001)
    
    class Config:
        arbitrary_types_allowed = True