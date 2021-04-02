import ursina
from fps.main.game_objects.GameObject import GameObject


class Gun(GameObject):
    _model: str = "cube"
    _scale: tuple[int, int, int] = (0.1, 0.1, 1)
    _position: tuple[int, int, int] = (1, 1.5, 1)
    _color: ursina.color.color = ursina.color.red
    _collider_type: str = "box"
    _texture_name: str = "white_cube"
