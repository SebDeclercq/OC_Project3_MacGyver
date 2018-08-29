#!/usr/bin/env python3
"""
@desc Module containing the Config class
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    1.0.0 (2018-08-22) : first functional version
"""


class Config:
    """Config class, intended to be used as a class only, containing all
    central variables used throughout the project"""
    PATH_MODEL_FILE = 'models/model.xlsx'
    BOARDGAME_WIDTH = 15
    BOARDGAME_HEIGHT = 15
    USER_INTERFACE = 'text'  # Should be text, prompt or pygame
    # Characters representing the elements in
    # model files and in display matrix
    WALL_CHAR = 'X'
    EXIT_CHAR = 'V'
    PAWN_CHAR = 'P'
    TOOL_CHAR = 'T'
