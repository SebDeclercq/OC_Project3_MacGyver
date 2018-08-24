#!/usr/bin/env python3
"""
@desc Module containing the Pawn class
@author SDQ <sdq@afnor.org>
@version 0.0.1
@note    0.0.1 (2018-08-22) : initialization
"""
from app.BoardElement import BoardElement
from app.Constants import Constants
from app.Tool import Tool
from typing import Tuple, FrozenSet


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

    def move(self, authorized_cells: FrozenSet[Tuple[int, int]],
             way: int) -> bool:
        self.has_moved = False
        if way == Constants.MOVE_LEFT:
            next_position = (self.x - 1, self.y)
        elif way == Constants.MOVE_RIGHT:
            next_position = (self.x + 1, self.y)
        elif way == Constants.MOVE_UP:
            next_position = (self.x, self.y + 1)
        elif way == Constants.MOVE_DOWN:
            next_position = (self.x, self.y - 1)
        else:
            raise ValueError('Unkwnown command "%s"' % (str(way),))

        if next_position in authorized_cells:
            self.old_position = self.position
            self.position = next_position
            self.has_moved = True

        return self.has_moved


    def pick_up(self, tool: Tool) -> bool:
        pass
