#!/usr/bin/env python3
"""
@desc Module containing the Tool class
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    1.0.0 (2018-08-22) : first functional version
"""
from app.BoardElement import BoardElement

class Tool(BoardElement):
    """Class defining a tool on the board"""
    def __init__(self, position):
        """Constructor
        @param tuple Position(Abscissa, Ordinate)"""
        super().__init__(position)
