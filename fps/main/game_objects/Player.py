from ursina.prefabs.first_person_controller import FirstPersonController


class Player(FirstPersonController):
    __position: tuple[int, int, int] = (0, 10, 0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = self.__position

    def update_object(self):
        pass
