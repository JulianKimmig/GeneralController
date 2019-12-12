import json

import basic_controller.controller as ctrl
from functools import partial


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
                    func=partial(self.get_board_fields, position=i)
                ),
            )
        # ctrl.controllefunction(requirement=0, level=ctrl.EDITOR, visible=False)
        # def call_i():

        # partial(self.get_board_fields, position = i))

    def possible_controller_added(self, controller):
        print("HERE", self.possible_controller)

    @ctrl.controllefunction(level=ctrl.LEVEL["NONE"])
    def get_board_fields(self, position):
        controller = self.get_linked_controller(position)
        if controller is None:
            return
        return controller.get_html_controller()

    def get_html(self, level=ctrl.LEVEL["NONE"]):
        data = super().get_html(level=level)
        if level < ctrl.LEVEL["VIEWER"]:
            return data

        container_subs = []
        for position in range(len(self.required_controller)):
            boardcontroller = self.get_linked_controller(position)
            if boardcontroller is not None:
                controller_subs = []

                controller_subs.append(
                    ctrl.gen_html_json(
                        node_type="div",
                        attributes={"class": "boardcontroller_title"},
                        text=str(boardcontroller),
                    )
                )

                input_subs = []
                for title, input in boardcontroller.get_controller_webfunctions(
                    level=level, as_html=False
                ).items():
                    input_subs.append(
                        ctrl.gen_html_json(
                            node_type="div",
                            subnodes=[
                                ctrl.gen_html_json(
                                    node_type="label",
                                    subnodes=[
                                        ctrl.gen_html_json(text=title + " ("),
                                        ctrl.gen_html_json(
                                            node_type="span", text=input.values[0]
                                        ),
                                        ctrl.gen_html_json(text=")"),
                                    ],
                                )
                            ]
                            + input.html_controller()
                            + [
                                ctrl.gen_html_json(
                                    node_type="button",
                                    text="set",
                                    attributes={
                                        "class": [
                                            "btn",
                                            "btn-primary",
                                            "board_var_set_button",
                                        ],
                                        "controller_id": "{{controller_id}}",
                                        "position": position,
                                    },
                                )
                            ],
                            attributes={
                                "class": ["form-group", "controller_input_group"]
                            },
                        )
                    )

                controller_subs.append(
                    ctrl.gen_html_json(
                        node_type="div",
                        subnodes=input_subs,
                        attributes={"class": "boardcontroller_inputs"},
                    )
                )

                container_subs.append(
                    ctrl.gen_html_json(
                        node_type="div",
                        subnodes=controller_subs,
                        attributes={"class": "general_boardcontroller_set"},
                    )
                )

        json_html = ctrl.gen_html_json(
            node_type="div",
            subnodes=container_subs,
            attributes={"class": "general_boardcontroller_container"},
        )

        data["json_html"] = json_html
        return data

    def set_value(self, name, value, position):
        board_controller = self.get_linked_controller(position)
        if board_controller is not None:
            board_controller.set_value(name, value)


if __name__ == "__main__":
    a = Controller_GeneralController()
