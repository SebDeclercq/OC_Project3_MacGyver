#!/usr/bin/env python3
"""
@desc Module containing the BoardGame class
@author SDQ <sdq@afnor.org>
@version 0.0.1
@note    0.0.1 (2018-08-22) : init class
"""
import xlrd
import csv
from app.Config import Config

class BoardGame:
    """Class defining a board for a boardgame"""
    def __init__(self):
        self.authorized_cells = set()
        self.unauthorized_cells = set()
        self.exit_cell = None
        self._parse_model_file()

    def _parse_model_file(self):
        if Config.FORMAT_MODEL_FILE.lower() == 'excel':
            self._parse_excel_model_file()
        elif Config.FORMAT_MODEL_FILE.lower() == 'text':
            self._parse_text_model_file()
        else:
            raise ValueError('Unknown format "%s"' % Config.FORMAT_MODEL_FILE)
        if self.exit_cell is None:
            raise ValueError('Exit cell "V" missing from "%s"'
                             % Config.PATH_MODEL_FILE)
        else:
            self.authorized_cells.add(self.exit_cell) # exit_cell is obviously authorized

        if len(self.authorized_cells) + len(self.unauthorized_cells) != 15 * 15:
            raise ValueError('The labyrinth has to be of 15x15')

        self.authorized_cells = frozenset(self.authorized_cells)     # Frozes the sets for further use
        self.unauthorized_cells = frozenset(self.unauthorized_cells)

    def _parse_excel_model_file(self):
        """Method parsing the Excel model file (path in Config class)
        @return void"""
        workbook = xlrd.open_workbook(Config.PATH_MODEL_FILE)
        sheet = workbook.sheet_by_index(0)
        for i in range(sheet.nrows):                    # For every rows in the sheet
            for j in range(sheet.ncols):                # And for every cells of the row
                value = sheet.cell(i, j).value.upper()  # Get cell value
                cell = (i, j)                           # Instantiate Cell object
                if value == xlrd.empty_cell.value:      # If cell is empty => authorized
                    self.authorized_cells.add(cell)
                elif value == "X":                      # If Cell contains X => wall => unauthorized
                    self.unauthorized_cells.add(cell)
                elif value == "V":                      # If Cell contains V => exit cell
                    self.exit_cell = cell
                else:
                    raise ValueError('Unknown value "%s" from "%s" line %d'
                                     % (value, Config.PATH_MODEL_FILE, i))
            if sheet.ncols < 15:                        # If there's less than 15 cols in the row
                for j in range(15 - sheet.ncols):
                    cell = (i, j)
                    self.authorized_cells.add(cell)  # Add authorized cells to complete because every cell is then empty
        if sheet.nrows < 15:                            # If there's less than 15 rows
            for i in range(15 - sheet.nrows):
                for j in range(15):
                    cell = (i, j)
                    self.authorized_cells.add(cell)  # Add authorized cells to complete because every cell is then empty

    def _parse_text_model_file(self):
        """Method parsing the Text model file (path in Config class).
        Reads the input file as a CSV file delimited by |
        @return void"""
        with open(Config.PATH_MODEL_FILE) as model_file:
            reader = csv.reader(model_file, delimiter='|', lineterminator='\n')
            for i, line in enumerate(reader):              # For every line
                for j, value in enumerate(line[1:-1]):     # For every cell *within* the line (excluding outside cells)
                    value = value.upper()
                    cell = (i, j)
                    if value == " ":                        # If cell is empty => authorized
                        self.authorized_cells.add(cell)
                    elif value == "X":                      # If cell contains X => wall => unauthorized
                        self.unauthorized_cells.add(cell)
                    elif value == "V":                      # If cell contains V => exit cell
                        self.exit_cell = cell
                    else:
                        raise ValueError('Unknown value "%s" from "%s" line %d'
                                         % (value, Config.PATH_MODEL_FILE, i))
