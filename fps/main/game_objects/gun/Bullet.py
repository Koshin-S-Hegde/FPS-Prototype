import ursina
from fps.main.game_objects.GameObject import GameObject


class Bullet(GameObject):
    __model: str = "cube"
    __scale: tuple[int, int, int] = (100, 0.1, 100)
    __position: tuple[int, int, int] = (0, 0, 0)
    __color: ursina.color.color = ursina.color.gold
    __collider: str = "box"
    __texture: str = "white_cube"
