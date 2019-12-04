from functools import partial
from typing import Set, Any

from modular_arduino_controller.board.board import ArduinoBoard

import basic_controller.controller as ctrl


class Controller_GeneralController(ctrl.MetaController):
    def __init__(self):
        super().__init__()
        self.required_controller = [
            "BoardController",
            "BoardController",
            "BoardController",
        ]

        for i in range(len(self.required_controller)):
            self.add_controller_function(
                f"get_board_fields_{i}",
                ctrl.ControllerFunction(
                    func=partial(self.get_board_fields, position=i), visible=False
                ),
            )

        print(self.get_controller_functions())

    def possible_controller_added(self, controller):
        print("HERE", self.possible_controller)

    @ctrl.controllefunction(level=ctrl.LEVEL["NONE"], visible=False)
    def get_board_fields(self, position):
        controller = self.get_linked_controller(position)
        if controller is None:
            return
        return controller.get_html_controller()

    def get_html(self, level=ctrl.LEVEL["NONE"]):
        print("BBBBB", level)
        return {}


if __name__ == "__main__":
    a = Controller_GeneralController()
