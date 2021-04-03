import ursina


class GameObject(ursina.Entity):
    _model: str
    _scale: tuple[int, int, int]
    _position: tuple[int, int, int]
    _color: ursina.color.color
    _collider_type: str
    _texture_name: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = self._model
        self.scale_x = self._scale[0]
        self.scale_y = self._scale[1]
        self.scale_z = self._scale[2]
        self.position = self._position
        self.color = self._color
        self.collider = self._collider_type
        self.texture = self._texture_name

    def update_object(self):
        pass
