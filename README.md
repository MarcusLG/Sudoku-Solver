# Sudoku-Solver
A simple command line-based sudoku solver using backtracking

## Overview
The programme accepts input in the command-line and can be easily repurposed to run in background. The input goes in according to a row-
by-row basis, where each empty tiles is representede with a non-numerical symbol, ideally '-' for the sake of standardization.

## Background
The puzzle is solved by first mapping the entire input puzzle, where it is mapped to a separate matrix where the empty slots are recorded.
Then a tracking matrix of value 1 for each of the empty slots is created. By going in with a incremental manner, the first empty slot that
the tracker encounters will be assigned with the value in the tracking matrix, after which checkings is done by feeding the partially-
filled matrix to a checker. Should no violation of game rules is found, the tracker proceed to the next empty slot. In a scenario where
the rules are violated, the tracking matrix will be increased with a +1 value. Should the tracking matrix reached a value of 9, it will be
set to 1, where the tracker will be set to the previous empty slot, increasing the current tracker slot with +1 value, thus the namesake
of the algorithm.
