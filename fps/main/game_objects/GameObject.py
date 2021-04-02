import ursina


class GameObject(ursina.Entity):
    __model: str
    __scale: tuple[int, int, int]
    __position: tuple[int, int, int]
    __color: ursina.color.color
    __collider: str
    __texture: str

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
