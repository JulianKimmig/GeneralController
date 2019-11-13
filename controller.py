from typing import Set, Any

from modular_arduino_controller.board.board import ArduinoBoard

import basic_controller.controller as ctrl


class Controller_GeneralController(ctrl.MetaController):
    def __init__(self):
        super().__init__()
        self.required_controller = ctrl.AyWT("BoardController")

    def possible_controller_added(self,controller):
        print("HERE",self.possible_controller)

if __name__ == "__main__":
    a = Controller_GeneralController()
