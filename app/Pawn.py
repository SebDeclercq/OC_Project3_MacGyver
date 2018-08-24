#!/usr/bin/env python3
"""
@desc Module containing the Pawn class
@author SDQ <sdq@afnor.org>
@version 0.0.1
@note    0.0.1 (2018-08-22) : initialization
"""
from app.BoardElement import BoardElement
from app.Tool import Tool
from typing import Tuple, Set
Position = Tuple[int, int]

class Pawn(BoardElement):
    """Class defining a pawn on the board"""
    def __init__(self, position: Position) -> None:
        """Constructor
        @param tuple Position(Abscissa, Ordinate)"""
        super().__init__(position)
        self.tools: Set[Tool] = set()

    def __repr__(self) -> str:
        """Method defining own way to represent (and print) an object
        @return string"""
        return ('<%s#%d position=%s>'
                % (self.__class__.__name__, id(self), self.position))

    def move(self, way: str) -> None:
        pass

    def pick_up(self, tool: Tool) -> None:
        pass
