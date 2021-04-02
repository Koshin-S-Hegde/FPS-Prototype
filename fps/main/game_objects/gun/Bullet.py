import ursina
from fps.main.game_objects.GameObject import GameObject


class Bullet(GameObject):
    _model: str = "sphere"
    _scale: tuple[int, int, int] = (0.1, 0.1, 0.1)
    _position: tuple[int, int, int] = (0, 1, 0)
    _color: ursina.color.color = ursina.color.black
    _collider_type: str = "sphere"
    _texture_name: str = "white_cube"
