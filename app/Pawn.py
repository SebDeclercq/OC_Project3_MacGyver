#!/usr/bin/env python3
"""
@desc Module containing the Pawn class
@author SDQ <sdq@afnor.org>
@version 0.0.1
@note    0.0.1 (2018-08-22) : initialization
"""
from app.BoardElement import BoardElement
from app.Tool import Tool
from typing import Tuple


class Pawn(BoardElement):
    """Class defining a pawn on the board"""
    def __init__(self, position: Tuple[int, int]) -> None:
        """Constructor
        @param tuple Position(Abscissa, Ordinate)"""
        super().__init__(position)
        self.tools = []

    def __repr__(self) -> str:
        """Method defining own way to represent (and print) an object
        @return string"""
        return ('<%s#%d position=%s>'
                % (self.__class__.__name__, id(self), self.position))

    def move(self, way: str) -> bool:
        pass

    def pick_up(self, tool: Tool) -> bool:
        pass
