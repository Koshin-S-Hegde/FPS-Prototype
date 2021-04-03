import ursina

from fps.main.game_objects.Ground import Ground
from fps.main.game_objects.Player import Player
from fps.main.game_objects.gun.Gun import Gun


def update():
    pass


class Game:
    __app: ursina.Ursina
    __player: Player
    __gun: Gun

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
        Ground()
        self.__gun = Gun()
        self.__player = Player()
        self.__gun.billboard = True
        self.__gun.reparent_to(self.__player)
        self.__gun.position = (1, 2, 1)


if __name__ == "__main__":
    Game()
