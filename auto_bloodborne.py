import time
import cv2
import screen
import input
import keys


screen = screen.Screen()
template = cv2.imread("images\\mark.JPG", 0)


def switch_item():
    input.press(keys.dpad_down)


def use_item():
    input.press(keys.square)
    time.sleep(.5)


def use_mark():
    use_item()
    time.sleep(1)
    input.press(keys.cross)


def move_forward(duration):
    input.press(keys.left_up, duration)


def turn_right():
    input.press(keys.left_right)
    input.press(keys.r3)
    input.press(keys.r3)


def power_attack():
    input.press(keys.r2)
    time.sleep(.60)


def charged_power_attack():
    input.press(keys.r2, 1.75)


def visceral():
    input.press(keys.r1)
    time.sleep(6)


def assassinate():
    input.press(keys.r2, 1.75)
    input.press(keys.r2)
    time.sleep(.60)
    input.press(keys.r1)
    time.sleep(6)


def lock_on():
    input.press(keys.r3)


def xp_run():
    move_forward(4)
    switch_item()
    use_item()
    move_forward(9)
    use_item()
    turn_right()
    lock_on()
    use_item()
    move_forward(2.25)
    use_item()
    lock_on()
    assassinate()
    switch_item()
    time.sleep(2)
    use_mark()


def xp_run_old():
    switch_item()
    use_item()
    move_forward(18.5)
    use_item()
    turn_right()
    lock_on()
    use_item()
    move_forward(2.25)
    use_item()
    lock_on()
    assassinate()
    switch_item()
    time.sleep(2)
    use_mark()


for i in range(99):
    if not screen.template_match(template, .08):
        break
    time.sleep(14)
    xp_run_old()

# t = 0
# frames = 0
#
# while True:
#     start_time = time.time()
#     screen.update_frames()
#     screen.show()
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
#     frames += 1
#     t += time.time() - start_time
#     if t >= 1:
#         print("fps: " + str(frames))
#         t = 0
#         frames = 0



