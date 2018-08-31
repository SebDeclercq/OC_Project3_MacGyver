#!/usr/bin/env python3
"""
@desc Module containing the UI class for pygame GUI display
@author SDQ <sdq@afnor.org>
@version 1.0.1
@note    0.0.1 (2018-08-30) : initialization
@note    1.0.0 (2018-08-30) : first functional version
@note    1.0.1 (2018-08-31) : corrected typing for _update_position()
                              + added a "toolbar" showing collected tools
                              + added a function to print text (bye, won, lost)
"""
from ui.UI import UI
from app.Constants import Constants
from app.Config import Config
import pygame
from typing import Dict, Tuple
import json
import os


class PyGame(UI):
    """Class managing a GUI with PyGame"""
    BOARDGAME_COLOR = (0, 0, 0)
    TOOLBAR_COLOR = (30, 30, 30)
    WIN_COLOR = (34, 139, 34)
    LOSE_COLOR = (220, 20, 60)
    FONT_COLOR = (0, 0, 0)
    IMGS_DIR = 'resources'
    PAWN_IMG = 'MacGyver.png'
    WALL_IMG = 'Brick_wall.jpg'
    GUARDIAN_IMG = 'Guardian.png'
    NEEDLE_IMG = 'Needle.png'
    SYRINGE_IMG = 'Syringe.png'
    ETHER_IMG = 'Ether.png'
    CELL_SIDE_SIZE = 35
    WAIT_TIME = 2000
    found_tools = {}

    @classmethod
    def interact(cls) -> int:
        """Class method for user interaction management
        @return int A constant from Constants class"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cls.display(json.dumps({}), quit=True)
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_l):
                    return Constants.MOVE_LEFT
                elif event.key in (pygame.K_RIGHT, pygame.K_r):
                    return Constants.MOVE_RIGHT
                elif event.key in (pygame.K_UP, pygame.K_u):
                    return Constants.MOVE_UP
                elif event.key in (pygame.K_DOWN, pygame.K_d):
                    return Constants.MOVE_DOWN
                elif event.key == pygame.K_a:  # == q (because QWERTY KEYBOARD)
                    cls.display(json.dumps({}), quit=True)
                    exit()

    @classmethod
    def display(cls, json: str, quit=False) -> None:
        """Class method for display management
        @param  str  json Parameters in a JSON string
        @param  bool quit If true, quits (OPTIONAL)
        @return void"""
        data = cls._parseJson(json)
        pygame.init()
        # Displays background with filling color
        boardgame = pygame.display.set_mode(
            cls._pixel_position((
                Config.BOARDGAME_WIDTH + 1, # + 1 for the "toolbar"
                Config.BOARDGAME_HEIGHT
            ))
        )
        boardgame.fill(cls.BOARDGAME_COLOR)

        if quit:
            cls._print_message('Bye !', boardgame, (255, 255, 255))
            return None

        # Tests if pawn has reached the exit_cell and if he's authorized
        # to get free
        if data.new_position == data.exit_cell:
            if data.freedom:
                cls._print_message('Won !', boardgame, cls.WIN_COLOR)
            else:
                cls._print_message('Lost...', boardgame, cls.LOSE_COLOR)
            return None

        # Display walls on the boardgame, by parsing the matrix backwards
        # to place them well in pygame
        wall = cls._create_board_element(cls.WALL_IMG)
        for y, row in enumerate(reversed(data.matrix)):
            for x, cell in enumerate(row):
                if cell == Config.WALL_CHAR:
                    boardgame.blit(wall, cls._pixel_position((x, y)))

        guardian = cls._create_board_element(cls.GUARDIAN_IMG)
        data.exit_cell = cls._update_position(data.exit_cell)
        boardgame.blit(guardian, cls._pixel_position(data.exit_cell))

        pawn = cls._create_board_element(cls.PAWN_IMG)
        data.new_position = cls._update_position(data.new_position)
        boardgame.blit(pawn, cls._pixel_position(data.new_position))

        # Displays the "toolbar" on the left (receptacle for collected tools)
        # Hint: pygame.Rect(left, top, width, height)
        rect_pos = ((Config.BOARDGAME_WIDTH + 0.5) * cls.CELL_SIDE_SIZE,
                    0, cls.CELL_SIDE_SIZE / 4,
                    Config.BOARDGAME_HEIGHT * cls.CELL_SIDE_SIZE)
        pygame.draw.rect(boardgame, cls.TOOLBAR_COLOR,
                         pygame.Rect(rect_pos), 35)

        # Displays the tools on the boardgame if not picked up
        for tool_type, position in data.tools.items():
            if tool_type == 'needle':
                tool = cls._create_board_element(cls.NEEDLE_IMG)
            elif tool_type == 'syringe':
                tool = cls._create_board_element(cls.SYRINGE_IMG)
            elif tool_type == 'ether':
                tool = cls._create_board_element(cls.ETHER_IMG)
            if position is None:  # Tool collected
                if tool_type not in cls.found_tools:
                    cls.found_tools[tool_type] = tool
                continue
            position = cls._update_position(position)
            boardgame.blit(tool, cls._pixel_position(position))

        # Displays the collected tools in the "toolbar"
        for i, tool in enumerate(cls.found_tools.values()):
            position = (Config.BOARDGAME_WIDTH,
                        Config.BOARDGAME_HEIGHT - 1 - i)
            position = cls._update_position(position)
            boardgame.blit(tool, cls._pixel_position(position))

        pygame.display.flip()

    @classmethod
    def _create_board_element(cls, img: str) -> pygame.Surface:
        """Class method creating an instance of BoardElement class,
        by loading and scaling its image
        @param  str            img     Name of the image to use
        @return pygame.Surface element The generated element"""
        element = pygame.image.load(
            os.path.join(cls.IMGS_DIR, img)
        ).convert_alpha()
        element = pygame.transform.scale(
            element,
            (cls.CELL_SIDE_SIZE, cls.CELL_SIDE_SIZE)
        )
        return element

    @classmethod
    def _update_position(cls, position: Tuple[int, int]) -> Tuple[int, int]:
        """Class method inverting Y axis for position, because PyGame
        puts origin (0, 0) at top-left corner
        @param  Tuple[int, int] position Classic X, Y position
        @return Tuple[int, int]          Inverted Y position"""
        return (
            position[0], Config.BOARDGAME_HEIGHT - 1 - position[1]
        )

    @classmethod
    def _pixel_position(cls, position: Tuple[int, int]) -> Tuple[int, int]:
        """Class method converting matrix position into a pixelated
        representation of it
        @param  Tuple[int, int] position Position to update
        @return Tuple[int, int]          Updated position"""
        return (
            position[0] * cls.CELL_SIDE_SIZE,
            position[1] * cls.CELL_SIDE_SIZE
        )

    @classmethod
    def _print_message(cls,
                       message: str,
                       boardgame: pygame.Surface,
                       background_color: Tuple[int, int, int]):
        """Class method displaying a message on a filled background
        @param  str                  message          Message to print
        @param  pygame.Surface       boardgame        Major Surface
        @param  Tuple[int, int, int] background_color RGB
        @return void
        """
        myfont = pygame.font.SysFont('monospace', 25)
        myfont.set_bold(True)
        text = myfont.render(message, 1, cls.FONT_COLOR)
        boardgame.fill(background_color)
        boardgame.blit(text, (0, 0))
        pygame.display.flip()
        pygame.time.wait(cls.WAIT_TIME)
