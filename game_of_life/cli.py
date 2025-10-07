# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 07:24:31 2025

@author: Bob
"""

import argparse
from .grid import Grid
from .patterns import GLIDER, BLINKER, BLOCK, translate
from .sim import run_console

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--rows", type=int, default=20)
    p.add_argument("--cols", type=int, default=20)
    p.add_argument("--wrap", action="store_true", default=True)
    p.add_argument("--steps", type=int, default=200)
    p.add_argument("--delay", type=float, default=0.08)
    p.add_argument("--pattern", choices=['glider','blinker','block','random'], default='glider')
    args = p.parse_args()
    
    g = Grid(args.rows, args.cols, wrap = args.wrap)
    if args.pattern == "glider":
        coords = translate(GLIDER, (1,1))
        for r,c in coords:
            g.set(r,c,1)
    elif args.pattern == "blinker":
        coords = translate(BLINKER, (args.rows//2, args.cols//2 - 1))
        for r,c in coords:
            g.set(r,c,1)
    elif args.pattern == "block":
        coords = translate(BLOCK, (args.rows//2, args.cols//2))
        for r,c in coords:
            g.set(r,c,1)
    else:
        g.randomize(p_alive=0.18)
        
    run_console(g, steps=args.steps, delay=args.delay)
    
if __name__ == "__main__":
    main()