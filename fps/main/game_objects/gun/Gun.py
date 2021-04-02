import ursina


class Gun(ursina.Entity):
    __model: str = "cube"
    __scale: tuple[int, int, int] = (0.1, 0.1, 1)
    __position: tuple[int, int, int] = (1, 1.5, 1)
    __color: ursina.color.color = ursina.color.red
    __collider: str = "box"
    __texture: str = "white_cube"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = self.__model
        self.scale_x = self.__scale[0]
        self.scale_y = self.__scale[1]
        self.scale_z = self.__scale[2]
        self.position = self.__position
        self.color = self.__color
        self.collider = self.__collider
        self.texture = self.__texture
