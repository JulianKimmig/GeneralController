from typing import Set, Any

from modular_arduino_controller.board.board import ArduinoBoard

import basic_controller.controller as ctrl


class Controller_GeneralController(ctrl.MetaController):
    required_boards = []

    def __init__(self):
        super().__init__()
        self.serial_boards: Set[ArduinoBoard] = set()


if __name__ == "__main__":
    a = Controller_GeneralController()
