#!/usr/bin/env python3
"""
@desc Module factorying UIs based on types
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    0.0.1 (2018-08-28) : initialization
@note    1.0.0 (2018-08-29) : first functional version
@note    1.0.1 (2018-08-29) : adding a Prompt UI
@note    1.0.2 (2018-08-30) : adding a PyGame UI
"""
from ui.UI import UI
from ui.TextOnly import TextOnly
from ui.Prompt import Prompt
from ui.PyGame import PyGame


class UIFactory:
    """Simple factory class for UIs"""

    @staticmethod
    def factory(type: str) -> UI:
        """Static method instantiating UIs
        @param  str type Wished type of UI
        @return UI  ui   The generated UI"""
        type = type.lower()
        if type == 'text':
            ui = TextOnly()
        elif type == 'prompt':
            ui = Prompt()
        elif type == 'gui':
            ui = PyGame()
        else:
            raise ValueError('Unkown type "%s" for UIs' % type)
        if not isinstance(ui, UI):
            raise TypeError('UI "%s" does\'nt implement UI "interface"' % type)
        else:
            return ui
