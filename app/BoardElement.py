#!/usr/bin/env python3
"""
@desc Module containing the BoardElement abstract class
@author SDQ <sdq@afnor.org>
@version 1.0.1
@note    1.0.0 (2018-08-22) : first functional version
@note    1.0.1 (2018-08-24) : evolving because Thierry said an abstract
                              constructor was weird
"""
from abc import ABC
from typing import Tuple
Position = Tuple[int, int]

class BoardElement(ABC):
    """Abstract class defining all the elements which could be found on
    a boardgame, for instance a pawn or a tool. SHOULD NOT BE INSTANTIATED"""
    def __init__(self, position: Position) -> None:
        """Constructor defining a position for the object
        @param tuple Position(Abscissa, Ordinate)"""
        self.position: Position = position

    @property
    def x(self) -> int:
        return self.position[0]

    @property
    def y(self) -> int:
        return self.position[1]
