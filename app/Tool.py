#!/usr/bin/env python3
"""
@desc Module containing the Tool class
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    1.0.0 (2018-08-24) : first functional version
"""
from app.BoardElement import BoardElement
from typing import Tuple


class Tool(BoardElement):
    """Class representing tools disposed on the BoardGame"""
    allowed_types = ('needle', 'syringe', 'ether')

    def __init__(self, position: Tuple[int, int], type: str) -> None:
        """Constructor
        @param tuple Position(Abscissa, Ordinate)"""
        super().__init__(position)
        if type in Tool.allowed_types:
            self.type = type
        else:
            raise ValueError('Tool needs to be of type "%s", "%s" or "%s"'
                             % Tool.allowed_types)

    def __repr__(self) -> str:
        """Method defining own way to represent (and print) an object
        @return string"""
        return (
            '<%s#%d position=%s, type=%s>'
            % (self.__class__.__name__, id(self), self.position, self.type)
        )
