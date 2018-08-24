#!/usr/bin/env python3
"""
@desc Module containing the BoardGame class
@author SDQ <sdq@afnor.org>
@version 0.0.2
@note    0.0.1 (2018-08-22) : init class
@note    0.0.2 (2018-08-24) : updating with sets + user-defined width & height
"""
import xlrd
import csv
import os
from app.Config import Config
from typing import Set, FrozenSet, Tuple, Any
Position = Tuple[int, int]

class BoardGame:
    """Class defining a board for a boardgame"""
    def __init__(self) -> None:
        self._parse_model_file()

    def _parse_model_file(self) -> None:
        self._authorized_cells: Set[Position] = set()
        self._unauthorized_cells: Set[Position] = set()

        model_dir: str = os.path.dirname(Config.PATH_MODEL_FILE)
        model_file: str = os.path.basename(Config.PATH_MODEL_FILE)
        model_ext: str = os.path.splitext(Config.PATH_MODEL_FILE)[1].lower()
        model_path: str = os.path.join(model_dir, model_file)
        if model_ext in ('.xls', '.xlsx'):
            self._parse_excel_model_file(model_path)
        elif model_ext in ('.txt', '.csv'):
            self._parse_text_model_file(model_path)
        else:
            raise ValueError('Unknown format "%s"' % Config.PATH_MODEL_FILE)
        if not hasattr(self, 'exit_cell'):
            raise ValueError('Exit cell "V" missing from "%s"'
                             % Config.PATH_MODEL_FILE)
        else:
            # exit_cell is obviously authorized
            self._authorized_cells.add(self.exit_cell)

        if (len(self._authorized_cells) + len(self._unauthorized_cells)
                != Config.BOARDGAME_WIDTH * Config.BOARDGAME_HEIGHT):
            raise ValueError(
                'The labyrinth has to be of %dx%d'
                % (Config.BOARDGAME_WIDTH, Config.BOARDGAME_HEIGHT)
            )

        # Frozes the sets for further use
        self.authorized_cells: FrozenSet[Position] = frozenset(self._authorized_cells)
        self.unauthorized_cells: FrozenSet[Position] = frozenset(self._unauthorized_cells)

    def _parse_excel_model_file(self, model_path: str) -> None:
        """Method parsing the Excel model file (path in Config class)
        @return void"""
        workbook: xlrd.book.Book = xlrd.open_workbook(model_path)
        sheet: xlrd.sheet.Sheet = workbook.sheet_by_index(0)
        # For every rows in the sheet
        for i in range(sheet.nrows):
            # And for every cells of the row
            for j in range(sheet.ncols):
                value: str = sheet.cell(i, j).value.upper()  # Get cell value
                cell: Position = (i, j)                           # Instantiate cell
                if value == xlrd.empty_cell.value:      # If empty=>authorized
                    self._authorized_cells.add(cell)
                elif value == "X":                      # If X=>unauthorized
                    self._unauthorized_cells.add(cell)
                elif value == "V":                      # If V=>exit cell
                    self.exit_cell: Position = cell
                else:
                    raise ValueError(
                        'Unknown value "%s" from "%s" line %d'
                        % (value, Config.PATH_MODEL_FILE, i)
                    )
            # If there's less than X cols in the row
            if sheet.ncols < Config.BOARDGAME_WIDTH:
                for j in range(Config.BOARDGAME_WIDTH - sheet.ncols):
                    cell = (i, j)
                    # Add authorized cells to complete because
                    # every cell is then empty
                    self._authorized_cells.add(cell)
        # If there's less than X rows
        if sheet.nrows < Config.BOARDGAME_HEIGHT:
            for i in range(Config.BOARDGAME_HEIGHT - sheet.nrows):
                i += sheet.nrows
                for j in range(Config.BOARDGAME_WIDTH):
                    cell = (i, j)
                    # Add authorized cells to complete because
                    # every cell is then empty
                    self._authorized_cells.add(cell)

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
                    value = value.upper()
                    cell = (i, j)
                    # If cell is empty => authorized
                    if value == " ":
                        self._authorized_cells.add(cell)
                    # If cell contains X => wall => unauthorized
                    elif value == "X":
                        self._unauthorized_cells.add(cell)
                    # If cell contains V => exit cell
                    elif value == "V":
                        self.exit_cell = cell
                    else:
                        raise ValueError('Unknown value "%s" from "%s" line %d'
                                         % (value, Config.PATH_MODEL_FILE, i))
