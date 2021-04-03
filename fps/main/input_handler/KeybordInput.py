class KeyboardInput:
    __right_mouse_is_pressed: bool = False

    def update_object(self, key: str):
        if key == "right mouse up":
            self.__right_mouse_is_pressed = False
        elif key == "right mouse down":
            self.__right_mouse_is_pressed = True

    def is_right_mouse_pressed(self):
        return self.__right_mouse_is_pressed
