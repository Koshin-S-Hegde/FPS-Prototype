import ursina
from fps.main.game_objects.GameObject import GameObject


class Gun(GameObject):
    __model: str = "cube"
    __scale: tuple[int, int, int] = (0.1, 0.1, 1)
    __position: tuple[int, int, int] = (1, 1.5, 1)
    __color: ursina.color.color = ursina.color.red
    __collider: str = "box"
    __texture: str = "white_cube"
