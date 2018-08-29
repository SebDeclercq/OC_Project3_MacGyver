#!/usr/bin/env python3
"""
@desc Module containing the UI class for text-only display
@author SDQ <sdq@afnor.org>
@version 1.0.1
@note    0.0.1 (2018-08-28) : initialization
@note    1.0.0 (2018-08-29) : first functional version
@note    1.0.1 (2018-08-29) : better screen display
"""
from ui.UI import UI
from app.Constants import Constants
import json


class TextOnly(UI):
    """Class managing a text-only UI"""
    movement_count = 0
    found_tools = []

    @classmethod
    def interact(cls) -> int:
        """Class method for user interaction management
        @return int A constant from Constants class"""
        way = None
        command = input('> ').lower()
        if command in ('q', 'quit', 'e', 'exit'):
            print('Bye !')
            exit()
        elif command in ('l', 'left'):
            way = Constants.MOVE_LEFT
        elif command in ('r', 'right'):
            way = Constants.MOVE_RIGHT
        elif command in ('u', 'up'):
            way = Constants.MOVE_UP
        elif command in ('d', 'down'):
            way = Constants.MOVE_DOWN
        return way

    @classmethod
    def display(cls, json: str) -> None:
        """Class method for display management
        @param  str json Parameters in a JSON string
        @return void"""
        cls._clear_screen()
        data = cls._parseJson(json)

        if cls.movement_count <= 1:
            print('%04d hit' % (cls.movement_count,), '\n\n')
        else:
            print('%04d hits' % (cls.movement_count,), '\n\n')

        print('MacGyver is here : %s !' % (data.new_position,))
        print('Tools are here : ', list(data.tools.values()))
        print('Exit cell is here : %s' % (data.exit_cell,))

        if data.old_position == data.new_position:
            if cls.movement_count > 0:
                print("Even MacGyver cannot pass through brick walls !")
        else:
            print(
                'MacGyver has moved from %s to %s'
                % (data.old_position, data.new_position)
            )
            for tool_type, position in data.tools.items():
                if position is None and tool_type not in cls.found_tools:
                    print('MacGyver has found a %s !' % tool_type)
                    cls.found_tools.append(tool_type)
            if data.new_position == data.exit_cell:
                print('MacGyver has reached the guardian... '
                      'Will he get free ?')
                if data.freedom:
                    print(f"\033[42mMacGyver is FREEEE !\033[0m")
                else:
                    print(f"\033[41mMacGyver didn't get out...\033[0m")
        cls.movement_count += 1
