from ursina.prefabs.first_person_controller import FirstPersonController

from fps.main.game_objects.Ground import Ground


class Player(FirstPersonController):
    __position: tuple[int, int, int] = (0, 10, 0)
    __ground: Ground

    def __init__(self, ground: Ground, **kwargs):
        super().__init__(**kwargs)
        self.position = self.__position
        self.__ground = ground

    def update_object(self, right_mouse_is_pressed: bool):
        pass
