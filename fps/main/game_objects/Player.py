import ursina
from ursina.hit_info import HitInfo
from ursina.prefabs.first_person_controller import FirstPersonController
import time

from fps.main.game_objects.Ground import Ground


class Player(FirstPersonController):
    __position: tuple[int, int, int] = (0, 10, 0)
    __TIME_BETWEEN_EACH_BULLET_IN_SECONDS: float = 0.5
    __last_time_bullet_shot: float = time.time()
    __ground: Ground

    def __init__(self, ground: Ground, **kwargs):
        super().__init__(**kwargs)
        self.position = self.__position
        self.__ground = ground

    def update_object(self, right_mouse_is_pressed: bool):
        if right_mouse_is_pressed and time.time() - self.__last_time_bullet_shot >= \
                self.__TIME_BETWEEN_EACH_BULLET_IN_SECONDS:
            self.__shoot()

    def __shoot(self):
        origin: tuple[int, int, int] = (self.position.x, self.position.y + 2, self.origin.z)
        hit_info: HitInfo = ursina.raycast(origin, direction=self.camera_pivot.forward, ignore=[self.__ground], debug=True)
        print(hit_info.entity, hit_info.hit)
        self.__last_time_bullet_shot = time.time()
