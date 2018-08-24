#!/usr/bin/env python3
"""
@desc Module containing the Game class
@author SDQ <sdq@afnor.org>
@version 0.0.1
@note    0.0.1 (2018-08-22) : initialization
"""
from app.BoardGame import BoardGame
from app.Constants import Constants
from app.Config import Config
from app.Pawn import Pawn
from app.Tool import Tool
import random
from typing import FrozenSet


class Game:
    """Master class for the entire project, which will pilot all operations
    throughout the game"""
    def __init__(self) -> None:
        self.boardgame = BoardGame()
        self.tools = set()
        self._randomly_place_board_elements()

    def play(self) -> None:
        """Method defining the entire game process"""
        result = self._start_game()
        if result:
            print('You win :-)')
        else:
            print('You die :-(')
        # self._quit_game() # Is it useful ?

    def _randomly_place_board_elements(self) -> None:
        """Method defining all four elements required on the boardgame :
        MacGyver, a needle, a syringe and a bottle of ether
        @return void"""
        # Extract four distinct authorized positions
        random_positions = random.sample(self.boardgame.authorized_cells, 4)
        self.macgyver = Pawn(random_positions.pop(0))
        for i, typ in enumerate(('needle', 'syringe', 'ether')):
            self.tools.add(Tool(random_positions[i], typ))
        # Frozes the set for further use
        self.tools = frozenset(self.tools)

    def _start_game(self) -> bool:
        """Method managing user interaction
        @return bool True => success / False => failure"""

        print(self.boardgame.authorized_cells)
        print('MacGyver is here : %s !' % (self.macgyver.position,))
        print(self.boardgame.exit_cell)
        while True:
            freedom = False
            way = None
            command = input('> ').lower()
            if command in ('q', 'quit', 'exit'):
                break
            elif command in ('h', 'help'):
                pass
            elif command in ('l', 'left'):
                way = Constants.MOVE_LEFT
            elif command in ('r', 'right'):
                way = Constants.MOVE_RIGHT
            elif command in ('u', 'up'):
                way = Constants.MOVE_UP
            elif command in ('d', 'down'):
                way = Constants.MOVE_DOWN
            else:
                pass
            if way is not None:
                self.macgyver.move(self.boardgame.authorized_cells, way)
                if self.macgyver.has_moved:
                    print(
                        'MacGyver has moved from %s to %s'
                        % (self.macgyver.old_position, self.macgyver.position)
                    )
                    tools_positions = (tool.position for tool in self.tools)
                    if self.macgyver.position in tools_positions:
                        pass
                    if self.macgyver.position == self.boardgame.exit_cell:
                        freedom = True
                        break
                        self._allow_exit()
                else:
                    print("Even MacGyver cannot pass through brick walls !")
            way = None
        return freedom

    def _allow_exit(self) -> bool:
        pass

    def _quit_game(self) -> None:
        """Is it useful ???"""
        pass
