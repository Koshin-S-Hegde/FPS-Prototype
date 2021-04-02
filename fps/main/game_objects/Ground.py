import ursina


class Ground:
    __model: str = "cube"
    __scale: tuple[int, int, int] = (100, 0.1, 100)
    __position: tuple[int, int, int] = (0, 0, 0)
    __color: ursina.color.color = ursina.color.gold
    __collider: str = "box"
    __texture: str = "white_cube"

    def __init__(self):
        ursina.Entity(model=self.__model, scale_x=self.__scale[0], scale_y=self.__scale[1], scale_z=self.__scale[2],
                      position=self.__position, color=self.__color, collider=self.__collider, texture=self.__texture)
