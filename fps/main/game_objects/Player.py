from ursina.prefabs.first_person_controller import FirstPersonController
from fps.main.game_objects.gun.Bullet import Bullet


class Player(FirstPersonController):
    __position: tuple[int, int, int] = (0, 10, 0)
    __bullets: list[Bullet]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = self.__position

    def update_object(self, is_right_mouse_pressed: bool):
        print(is_right_mouse_pressed)
