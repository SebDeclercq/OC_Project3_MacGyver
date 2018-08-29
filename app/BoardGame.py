#!/usr/bin/env python3
"""
@desc Module containing the BoardGame class
@author SDQ <sdq@afnor.org>
@version 0.0.4
@note    0.0.1 (2018-08-22) : init class
@note    0.0.2 (2018-08-24) : updating with sets + user-defined width & height
@note    0.0.3 (2018-08-24) : inverting Y axis (put 0, 0 at the bottom-left
                              instead of top-left)
@note    0.0.4 (2018-08-29) : adding an attr "matrix" displaying the boardgame
"""
import xlrd
import csv
import os
from app.Config import Config
from typing import List


class BoardGame:
    """Class defining a board for a boardgame"""
    def __init__(self) -> None:
        self.authorized_cells = set()
        self.unauthorized_cells = set()
        self.exit_cell = None
        self._parse_model_file()
        self._create_matrix_display()

    def _parse_model_file(self) -> None:
        model_dir = os.path.dirname(Config.PATH_MODEL_FILE)
        model_file = os.path.basename(Config.PATH_MODEL_FILE)
        model_ext = os.path.splitext(Config.PATH_MODEL_FILE)[1].lower()
        model_path = os.path.join(model_dir, model_file)
        if model_ext in ('.xls', '.xlsx'):
            self._parse_excel_model_file(model_path)
        elif model_ext in ('.txt', '.csv'):
            self._parse_text_model_file(model_path)
        else:
            raise ValueError('Unknown format "%s"' % model_ext)
        if self.exit_cell is None:
            raise ValueError('Exit cell "V" missing from "%s"'
                             % Config.PATH_MODEL_FILE)
        else:
            # exit_cell is obviously authorized
            self.authorized_cells.add(self.exit_cell)

        if (len(self.authorized_cells) + len(self.unauthorized_cells)
                != Config.BOARDGAME_WIDTH * Config.BOARDGAME_HEIGHT):
            raise ValueError(
                'The labyrinth has to be of %dx%d'
                % (Config.BOARDGAME_WIDTH, Config.BOARDGAME_HEIGHT)
            )

        # Frozes the sets for further use
        self.authorized_cells = frozenset(self.authorized_cells)
        self.unauthorized_cells = frozenset(self.unauthorized_cells)

    def _parse_excel_model_file(self, model_path: str) -> None:
        """Method parsing the Excel model file (path in Config class)
        @return void"""
        workbook = xlrd.open_workbook(model_path)
        sheet = workbook.sheet_by_index(0)
        # For every rows in the sheet
        for i in range(sheet.nrows):
            # And for every cells of the row
            for j in range(sheet.ncols):
                x, y = j, Config.BOARDGAME_HEIGHT - i - 1
                value = sheet.cell(i, j).value.upper()  # Get cell value
                cell = (x, y)                           # Instantiate cell
                if value == xlrd.empty_cell.value:      # If empty=>authorized
                    self.authorized_cells.add(cell)
                elif value == "X":                      # If X=>unauthorized
                    self.unauthorized_cells.add(cell)
                elif value == "V":                      # If V=>exit cell
                    self.exit_cell = cell
                else:
                    raise ValueError(
                        'Unknown value "%s" from "%s" line %d'
                        % (value, Config.PATH_MODEL_FILE, i)
                    )
            # If there's less than X cols in the row
            if sheet.ncols < Config.BOARDGAME_WIDTH:
                for j in range(Config.BOARDGAME_WIDTH - sheet.ncols):
                    x = Config.BOARDGAME_WIDTH - j - 1
                    cell = (x, y)
                    # Add authorized cells to complete because
                    # every cell is then empty
                    self.authorized_cells.add(cell)
        # If there's less than X rows
        if sheet.nrows < Config.BOARDGAME_HEIGHT:
            for y in range(Config.BOARDGAME_HEIGHT - sheet.nrows):
                for x in range(Config.BOARDGAME_WIDTH):
                    cell = (x, y)
                    # Add authorized cells to complete because
                    # every cell is then empty
                    self.authorized_cells.add(cell)

    def _parse_text_model_file(self, model_path: str) -> None:
        """Method parsing the Text model file (path in Config class).
        Reads the input file as a CSV file delimited by |
        @return void"""
        with open(model_path) as model_file:
            reader = csv.reader(model_file, delimiter='|', lineterminator='\n')
            # For every line
            for i, line in enumerate(reader):
                # For every cell *within* the line (excluding outside cells)
                for j, value in enumerate(line[1:-1]):
                    x, y = j, Config.BOARDGAME_HEIGHT - i - 1
                    value = value.upper()
                    cell = (x, y)
                    # If cell is empty => authorized
                    if value == " ":
                        self.authorized_cells.add(cell)
                    # If cell contains X => wall => unauthorized
                    elif value == Config.WALL_CHAR:
                        self.unauthorized_cells.add(cell)
                    # If cell contains V => exit cell
                    elif value == Config.EXIT_CHAR:
                        self.exit_cell = cell
                    else:
                        raise ValueError('Unknown value "%s" from "%s" line %d'
                                         % (value, Config.PATH_MODEL_FILE, i))

    def _create_matrix_display(self) -> List[List[str]]:
        """Method generating matrix display of the boardgame
        based on model file
        @return List[List[str]] The generated matrix"""
        self.matrix = []  # type: List[List[str]]
        for y in range(Config.BOARDGAME_HEIGHT):
            self.matrix.append([])
            for x in range(Config.BOARDGAME_WIDTH):
                if (x, y) == self.exit_cell:
                    cell = Config.EXIT_CHAR
                elif (x, y) in self.authorized_cells:
                    cell = ' '
                else:
                    cell = Config.WALL_CHAR
                self.matrix[y].append(cell)
        return self.matrix
