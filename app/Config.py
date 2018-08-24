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
    PATH_MODEL_FILE: str = 'models/model.xlsx'
    BOARDGAME_WIDTH: int = 15
    BOARDGAME_HEIGHT: int = 15
