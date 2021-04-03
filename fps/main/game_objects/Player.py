from ursina.prefabs.first_person_controller import FirstPersonController
from fps.main.game_objects.gun.Bullet import Bullet
import time


class Player(FirstPersonController):
    __position: tuple[int, int, int] = (0, 10, 0)
    __bullets: list[Bullet] = []
    __TIME_BETWEEN_EACH_BULLET_IN_SECONDS: float = 0.5
    __last_time_bullet_shot: float = time.time()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = self.__position

    def update_object(self, right_mouse_is_pressed: bool):
        if right_mouse_is_pressed and time.time() - self.__last_time_bullet_shot >= \
                self.__TIME_BETWEEN_EACH_BULLET_IN_SECONDS:
            self.__shoot()

    def __shoot(self):
        self.__bullets.append(Bullet(self.position))
        self.__last_time_bullet_shot = time.time()

