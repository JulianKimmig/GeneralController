from typing import Set, Any

from arduino_controller.basicboard.board import ArduinoBoard

try:
    import Controller as ctrl
except:
    import basic_controller.controller as ctrl


class Controller_GeneralController(ctrl.MetaController, ctrl.SerialController):
    required_boards = ["AnyBoard"]

    def __init__(self):
        super().__init__()
        self.serial_boards: Set[ArduinoBoard] = set()

    def board_added(self, board):
        self.link_board(board)


if __name__ == "__main__":
    a = Controller_GeneralController()
