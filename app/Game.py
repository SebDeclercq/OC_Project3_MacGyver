#!/usr/bin/env python3
"""
@desc Module containing the Game class
@author SDQ <sdq@afnor.org>
@version 1.0.0
@note    0.0.1 (2018-08-22) : initialization
@note    0.0.2 (2018-08-24) : game is handled from start to end (text-only)
@note    0.0.3 (2018-08-29) : game has a first functional UI
@note    1.0.0 (2018-08-31) : project's first complete version
"""
from app.BoardGame import BoardGame
from app.Config import Config
from app.Pawn import Pawn
from app.Tool import Tool
from app.UIFactory import UIFactory as UI
from typing import FrozenSet, List
import random
import json
import copy


class Game:
    """Master class for the entire project, which will pilot all operations
    throughout the game"""
    def __init__(self) -> None:
        self.boardgame = BoardGame()
        self.tools = set()
        self._randomly_place_board_elements()
        # Generating appropriated UI
        self.ui = UI.factory(Config.USER_INTERFACE)

    def play(self) -> bool:
        """Method managing the gameplay
        @return bool (useless)"""
        freedom = False
        way = None
        data = self._get_json_for_ui(freedom)
        self.ui.display(data)         # Display for the first time
        while True:                   # Until pawn has reached exit_cell
            way = self.ui.interact()  # Interact with player
            # If a move instruction is received
            if way is not None:
                self.macgyver.move(self.boardgame.authorized_cells, way)
                # If MacGyver is authorized to move that way and has moved
                if self.macgyver.has_moved:
                    for tool in self.tools:
                        # If MacGyver is at a tool position, he picks it up
                        if self.macgyver.position == tool.position:
                            self.macgyver.pick_up(tool)
                            tool.position = None
                    # If MacGyver is in front of the guardian
                    if self.macgyver.position == self.boardgame.exit_cell:
                        freedom = self._allow_exit()
                        data = self._get_json_for_ui(freedom)
                        self.ui.display(data)
                        break  # End of game
            data = self._get_json_for_ui(freedom)  # Format JSON for UI
            self.ui.display(data)                  # UI display
        return freedom

    def _randomly_place_board_elements(self) -> None:
        """Method defining all four elements required on the boardgame :
        MacGyver, a needle, a syringe and a bottle of ether
        @return void"""
        if len(self.boardgame.authorized_cells) <= 4:
            raise ValueError('BoardGame must at least have 4 free cells')
        # Extract four distinct authorized positions
        random_positions = random.sample(self.boardgame.authorized_cells, 4)
        while self.boardgame.exit_cell in random_positions:
            random_positions = random.sample(self.boardgame.authorized_cells, 4)
        self.macgyver = Pawn(random_positions.pop(0))
        for i, typ in enumerate(('needle', 'syringe', 'ether')):
            self.tools.add(Tool(random_positions[i], typ))
        # Frozes the set for further use
        self.tools = frozenset(self.tools)

    def _allow_exit(self) -> bool:
        """Check if MacGyver has all three tools.
        @return bool If True, he can take the guardian down
                     and get free ! If False, he dies..."""
        if self.tools == frozenset(self.macgyver.tools):
            return True
        else:
            return False

    def _get_json_for_ui(self, freedom: bool) -> str:
        """Method generating JSON string for UI config
        @param  bool freedom Has MacGyver got free ?
        @return str          The generated JSON"""
        return json.dumps({
            'matrix': self._get_current_boardgame_matrix(),
            'old_position': self.macgyver.old_position,
            'new_position': self.macgyver.position,
            'tools': {
                tool.type: tool.position for tool in self.tools
            },
            'exit_cell': self.boardgame.exit_cell,
            'freedom': freedom
        })

    def _get_current_boardgame_matrix(self) -> List[List[str]]:
        """Method generating a display matrix of game current stage
        @return List[List[str]] The generated matrix"""
        matrix = copy.deepcopy(self.boardgame.matrix)  # Copy init stage
        matrix[self.macgyver.y][self.macgyver.x] = Config.PAWN_CHAR  # Add Pawn
        for tool in self.tools:
            if tool.position is not None:
                matrix[tool.y][tool.x] = Config.TOOL_CHAR  # Add Tools if any
        return matrix
