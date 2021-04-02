import ursina
from fps.main.game_objects.GameObject import GameObject


class Ground(GameObject):
    _model: str = "cube"
    _scale: tuple[int, int, int] = (100, 0.1, 100)
    _position: tuple[int, int, int] = (0, 0, 0)
    _color: ursina.color.color = ursina.color.gold
    _collider_type: str = "box"
    _texture_name: str = "white_cube"
