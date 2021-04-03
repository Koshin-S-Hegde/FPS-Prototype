class KeyboardInput:
    __is_right_mouse_pressed: bool = False

    def update_object(self, key: str):
        if key == "right mouse up":
            self.__is_right_mouse_pressed = False
        elif key == "right mouse down":
            self.__is_right_mouse_pressed = True

    def is_right_mouse_pressed(self):
        return self.__is_right_mouse_pressed
