#!/usr/bin/env python3
"""
@desc Module containing the BoardElement abstract class
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    1.0.0 (2018-08-22) : first functional version
"""
from abc import ABC, abstractmethod

class BoardElement(ABC):
    """Abstract class defining all the elements which could be found on a boardgame,
    for instance a pawn or a tool"""
    @abstractmethod
    def __init__(self, x, y):
        """Abstract constructor defining a position for the object
        @param int x Abscissa
        @param int y Ordinate"""
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
