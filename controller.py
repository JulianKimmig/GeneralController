from basic_controller.controller import MetaController, SerialController


class Controller_GeneralController(MetaController, SerialController):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    a = Controller_GeneralController()
    print(a.required_boards, a.required_controller)
