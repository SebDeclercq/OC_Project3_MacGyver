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
import json


class Prompt(TextOnly):
    """Class managing a prompt UI. Inherits from TextOnly instead of UI
    in order to use its interact method (same behaviour expected). Prompt
    only renders a neat screen display."""
    BLUE_BACKGROUND = '46'
    GRAY_BACKGROUND = '43;30'
    GREEN_BACKGROUND = '42'

    @classmethod
    def display(cls, json: str) -> None:
        """Class method for display management
        @param  str json Parameters in a JSON string
        @return void"""
        cls._clear_screen()
        data = cls._parseJson(json)

        legend = {
            'WALL': ['', Config.WALL_CHAR],
            'EXIT': [cls.GREEN_BACKGROUND, Config.EXIT_CHAR],
            'MACGYVER': [cls.GRAY_BACKGROUND, Config.PAWN_CHAR],
            'TOOL': [cls.BLUE_BACKGROUND, Config.TOOL_CHAR],
        }

        print('=' * 14)
        print('==  LEGEND  ==')
        for word, char in legend.items():
            print(' {:<9}: \033[{}m{}\033[0m'.format(word, *char))
        print('=' * 14, '\n\n')

        data.matrix = cls._colorize_matrix(
            data.matrix, data.new_position, cls.GRAY_BACKGROUND
        )

        for position in data.tools.values():
            if position is not None:
                data.matrix = cls._colorize_matrix(
                    data.matrix, position, cls.BLUE_BACKGROUND
                )

        data.matrix = cls._colorize_matrix(
            data.matrix, data.exit_cell, cls.GREEN_BACKGROUND
        )

        if cls.movement_count <= 1:
            print('%04d hit' % (cls.movement_count,), '\n\n')
        else:
            print('%04d hits' % (cls.movement_count,), '\n\n')

        for row in reversed(data.matrix):
            print('|' + '|'.join(row) + '|')
        for tool_type, position in data.tools.items():
            if position is None and tool_type not in cls.found_tools:
                print('MacGyver has found a %s !' % tool_type)
                cls.found_tools.append(tool_type)
        if data.new_position == data.exit_cell:
            if data.freedom:
                print(f"\033[42mMacGyver is FREEEE !\033[0m")
            else:
                print(f"\033[41mMacGyver didn't get out...\033[0m")
        cls.movement_count += 1

    @classmethod
    def _colorize_matrix(cls, matrix, position, color):
        char = matrix[position[1]][position[0]]
        new_content = '\033[%sm%s\033[0m' % (color, char)
        matrix[position[1]][position[0]] = new_content
        return matrix
