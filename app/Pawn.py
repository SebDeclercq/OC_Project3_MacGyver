#!/usr/bin/env python3
"""
@desc Module containing the Pawn class
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    1.0.0 (2018-08-22) : first functional version
"""
from app.BoardElement import BoardElement

class Pawn(BoardElement):
    """Class defining a pawn on the board"""
    def __init__(self, position):
        """Constructor
        @param tuple Position(Abscissa, Ordinate)"""
        super().__init__(position)
        self.tools = []

    def move(self, way):
        pass

    def pick_up(self, tool):
        pass
