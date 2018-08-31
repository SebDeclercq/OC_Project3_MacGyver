#!/usr/bin/env python3
"""
@desc Module containing the UI class for prompt display
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    0.0.1 (2018-08-29) : initialization
@note    1.0.0 (2018-08-29) : first functional version
"""
from ui.TextOnly import TextOnly
from app.Constants import Constants
from app.Config import Config
from typing import List, Tuple
import json


class Prompt(TextOnly):
    """Class managing a prompt UI. Inherits from TextOnly instead of UI
    in order to use its interact method (same behaviour expected). Prompt
    only renders a neat screen display."""
    TOOL_BACKGROUND = '46'
    PAWN_BACKGROUND = '43;30'
    EXIT_BACKGROUND = '42'

    @classmethod
    def display(cls, json: str) -> None:
        """Class method for display management
        @param  str json Parameters in a JSON string
        @return void"""
        cls._clear_screen()
        data = cls._parseJson(json)

        legend = {
            'WALL': ['', Config.WALL_CHAR],
            'EXIT': [cls.EXIT_BACKGROUND, Config.EXIT_CHAR],
            'MACGYVER': [cls.PAWN_BACKGROUND, Config.PAWN_CHAR],
            'TOOL': [cls.TOOL_BACKGROUND, Config.TOOL_CHAR],
        }

        # Prints legend as help for the player
        print('=' * 14)
        print('==  LEGEND  ==')
        for word, char in legend.items():
            print(' {:<9}: \033[{}m{}\033[0m'.format(word, *char))
        print('=' * 14, '\n\n')

        # Adds colors to the pawn
        data.matrix = cls._colorize_matrix(
            data.matrix, data.new_position, cls.PAWN_BACKGROUND
        )

        # Adds colors to all the tools
        for position in data.tools.values():
            if position is not None:
                data.matrix = cls._colorize_matrix(
                    data.matrix, position, cls.TOOL_BACKGROUND
                )

        # Adds colors to exit_cell
        data.matrix = cls._colorize_matrix(
            data.matrix, data.exit_cell, cls.EXIT_BACKGROUND
        )

        # Displays a hit counter
        if cls.movement_count <= 1:
            print('%04d hit' % (cls.movement_count,), '\n\n')
        else:
            print('%04d hits' % (cls.movement_count,), '\n\n')

        # Displays collected tools
        tools = ['\033[%sm%s\033[0m ' % (cls.TOOL_BACKGROUND, type)
                 for type, position in data.tools.items() if position is None]
        print('Tools : ', ''.join(tools), '\n\n')

        # Displays the matrix in reverse (to put the 0 abscissa at the bottom)
        for row in reversed(data.matrix):
            print('|' + '|'.join(row) + '|')

        # Prints interactive messages based on MacGyver's actions
        print('\n')
        for tool_type, position in data.tools.items():
            if position is None and tool_type not in cls.found_tools:
                print('MacGyver has found a %s !\n' % tool_type)
                cls.found_tools.append(tool_type)
        if data.new_position == data.exit_cell:
            if data.freedom:
                print(f"\033[42mMacGyver is FREEEE !\033[0m")
            else:
                print(f"\033[41mMacGyver didn't get out...\033[0m")
            print('\n')
        cls.movement_count += 1

    @classmethod
    def _colorize_matrix(cls,
                         matrix: List[List[str]],
                         position: Tuple[int, int],
                         color: str) -> List[List[str]]:
        """Class method colorizing elements on the boardgame
        @param  List[List[str]] matrix   The matrix representing the boardgame
        @param  Tuple[int, int] position The position to colorize
        @param  str             color    Prompt color string
        @return List[List[str]] matrix"""
        char = matrix[position[1]][position[0]]            # Gets current value
        new_content = '\033[%sm%s\033[0m' % (color, char)  # Adds color code
        matrix[position[1]][position[0]] = new_content     # Change value
        return matrix
