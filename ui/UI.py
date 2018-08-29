#!/usr/bin/env python3
"""
@desc Module containing the abstract class parent of all UI classes
      and a "private" class _Data
@author SDQ <sdq@afnor.org>
@version 1.0.1
@note    0.0.1 (2018-08-28) : initialization
@note    1.0.0 (2018-08-29) : first functional version
@note    1.0.1 (2018-08-29) : adding a class method to clear screen
"""
from abc import ABC, abstractmethod
from typing import Any
import platform
import json
import os


class _Data:
    '''"Private" class formatting JSON data in an object form'''
    def __init__(self, data: str) -> None:
        """Constructor parsing JSON
        @param str data The JSON to parse"""
        data = json.loads(data)
        for attr, value in data.items():
            setattr(self, attr, value)


class UI(ABC):
    """Abstract class, parent of all UI classes"""
    @abstractmethod
    def interact(cls) -> Any:
        """Abstract class method for user interaction management"""
        pass

    @abstractmethod
    def display(cls, json: str) -> None:
        """Abstract class method for display management"""
        pass

    @classmethod
    def _parseJson(cls, json: str) -> _Data:
        """Class method parsing JSON input in a _Data object"""
        data = _Data(json)
        return data

    @classmethod
    def _clear_screen(cls) -> None:
        """Class method clearing screen based on OS type"""
        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')
