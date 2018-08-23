#!/usr/bin/env python3
"""
@desc Module containing the Game class
@author SDQ <sdq@afnor.org>
@version 0.0.1
@note    0.0.1 (2018-08-22) : initialization
"""
from app.GameBoard import GameBoard
from app.Config import Config
from app.Pawn import Pawn
from app.Tool import Tool
import random

class Game:
    """Master class for the entire project, which will pilot all operations
    throughout the game"""
    def __init__(self):
        self.gameboard = GameBoard()
        self._randomly_place_board_elements()
        ...

    def play(self):
        pass

    def _randomly_place_board_elements(self):
        random_positions = random.sample(self.gameboard.authorized_cells, 4)
        self.macgyver = Pawn(random_positions[0])
        for i, attr in enumerate(('needle', 'tube', 'ether')):
            setattr(self, attr, Tool(random_positions[i + 1]))

    def _start_game(self):
        pass

    def _allow_exit(self):
        pass

    def _quit_game(self):
        pass
