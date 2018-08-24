#!/usr/bin/env python3
"""
@desc Module containing the Game class
@author SDQ <sdq@afnor.org>
@version 0.0.1
@note    0.0.1 (2018-08-22) : initialization
"""
from app.BoardGame import BoardGame
from app.Config import Config
from app.Pawn import Pawn
from app.Tool import Tool
import random

class Game:
    """Master class for the entire project, which will pilot all operations
    throughout the game"""
    def __init__(self):
        self.boardgame = BoardGame()
        self.tools = set()
        self._randomly_place_board_elements()

    def play(self):
        """Method defining the entire game process"""
        result = self._start_game()
        if result:
            print('You win :-)')
        else:
            print('You die :-(')
        # self._quit_game() # Is it useful ?

    def _randomly_place_board_elements(self):
        """Method defining all four elements required on the boardgame :
        MacGyver, a needle, a syringe and a bottle of ether
        @return void"""
        random_positions = random.sample(self.boardgame.authorized_cells, 4) # Extract four distinct authorized positions
        self.macgyver = Pawn(random_positions.pop(0))
        for i, typ in enumerate(('needle', 'syringe', 'ether')):
            self.tools.add(Tool(random_positions[i], typ))
        self.tools = frozenset(self.tools)                                   # Frozes the set for further use

    def _start_game(self):
        """Method managing user interaction
        @return bool True => success / False => failure"""
        return random.choice((True, False)) # FOR DEV

    def _allow_exit(self):
        pass

    def _quit_game(self):
        """Is it useful ???"""
        pass
