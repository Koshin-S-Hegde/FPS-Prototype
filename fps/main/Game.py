import ursina

from fps.main.game_objects.Ground import Ground
from fps.main.game_objects.Player import Player
from fps.main.game_objects.gun.Gun import Gun
from fps.main.input_handler.KeybordInput import KeyboardInput


class Game:
    __app: ursina.Ursina
    __player: Player
    __gun: Gun
    __ground: Ground
    __keyboard_input: KeyboardInput

    def __init__(self):
        self.__window_init()
        self.__game_objects_init()
        self.__input_handler_init()

    def __window_init(self):
        self.__app = ursina.Ursina()
        ursina.window.borderless = False
        ursina.window.fps_counter.position = ursina.window.exit_button.position
        ursina.window.exit_button.visible = False

    def run(self):
        self.__app.run()

    def __game_objects_init(self):
        self.__ground = Ground()
        self.__gun = Gun()
        self.__player = Player(self.__ground)
        self.__gun.billboard = True
        self.__gun.reparent_to(self.__player)
        self.__gun.position = (1, 2, 1)

    def update_object(self):
        self.__ground.update_object()
        self.__player.update_object(self.__keyboard_input.is_right_mouse_pressed())
        self.__gun.update_object()

    def __input_handler_init(self):
        self.__keyboard_input = KeyboardInput()

    def update_input_handlers(self, key: str):
        self.__keyboard_input.update_object(key)


if __name__ == "__main__":
    game = Game()


    def update():
        game.update_object()

    def input(key):
        game.update_input_handlers(key)


    game.run()
