#!/usr/bin/env python3
from app.Game import Game
from app.Config import Config
def main():
    game = Game(model=Config.PATH_MODEL_FILE)
    print(game.__dict__)
    game.play()

if __name__ == '__main__':
    main()
