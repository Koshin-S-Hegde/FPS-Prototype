import ursina
from fps.main.game_objects.GameObject import GameObject
from fps.main.input_handler.KeybordInput import KeyboardInput


class Enemy(GameObject):
    _model: str = ""
    _scale: tuple[int, int, int] = (1, 1, 1)
    _position: tuple[int, int, int] = (0, 0.5, 0)
    _color: ursina.color.color = ursina.color.green
    _collider_type: str = "box"
    _texture_name: str = "white_cube"

    __keyboard_input_handler: KeyboardInput
    __has_been_shot: bool = False

    def __init__(self, keyboard_input_handler, **kwargs):
        super().__init__(**kwargs)
        self.parent = ursina.scene
        self.model = "cube"
        self.__keyboard_input_handler = keyboard_input_handler

    def update_object(self, is_shooting: bool):
        if self.hovered and is_shooting:
            self.__has_been_shot = True
            print('a')

    def is_shot(self):
        return self.__has_been_shot
