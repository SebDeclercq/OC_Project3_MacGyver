#!/usr/bin/env python3
"""
@desc Script launching the game
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    0.0.1 (2018-08-21) : initialization
@note    1.0.0 (2018-08-31) : added an errors capture
                              + project's first complete version
"""
from app.Game import Game


def main():
    try:
        game = Game()
        game.play()
    except Exception as e:
        print('\n\033[41mAn error (%s) has occurred : %s\033[0m\n'
              % (e.__class__.__name__, str(e)))


if __name__ == '__main__':
    main()
