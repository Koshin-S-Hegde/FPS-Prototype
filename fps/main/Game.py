import ursina

from fps.main.game_objects.Player import Player


def update():
    pass


class Game:
    __app: ursina.Ursina
    __player: Player

    def __init__(self):
        self.__window_init()
        self.__game_objects_init()
        self.__run()

    def __window_init(self):
        self.__app = ursina.Ursina()
        ursina.window.borderless = False
        ursina.window.fps_counter.position = ursina.window.exit_button.position
        ursina.window.exit_button.visible = False

    def __run(self):
        self.__app.run()

    def __game_objects_init(self):
        self.__player = Player()


if __name__ == "__main__":
    Game()
