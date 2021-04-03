import ursina
from fps.main.game_objects.GameObject import GameObject


class Enemy(GameObject):
    _model: str = "cube"
    _scale: tuple[int, int, int] = (1, 1, 1)
    _position: tuple[int, int, int] = (0, 0.5, 0)
    _color: ursina.color.color = ursina.color.green
    _collider_type: str = "box"
    _texture_name: str = "white_cube"

    __has_been_shot: bool = False

    def __init__(self, position: tuple[float, float, float], **kwargs):
        super().__init__(**kwargs)
        self.position = position

    def update_object(self, is_shooting: bool):
        if self.hovered and is_shooting:
            self.__has_been_shot = True

    def is_shot(self):
        return self.__has_been_shot
