import time
import cv2
import screen
import input
import keys

scr = screen.Screen()

tem_velvet_room = cv2.imread("images\\persona\\velvet_room.JPG", 0)
tem_talk_igor = cv2.imread("images\\persona\\talk_igor.JPG", 0)
tem_igor_dialogue = cv2.imread("images\\persona\\igor_dialogue.JPG", 0)

tem_create_persona = cv2.imread("images\\persona\\create_persona.JPG", 0)
tem_persona_fusion = cv2.imread("images\\persona\\persona_fusion.JPG", 0)
tem_network_fusion = cv2.imread("images\\persona\\network_fusion.JPG", 0)

tem_network_fusion_screen = cv2.imread("images\\persona\\network_fusion_screen.JPG", 0)
tem_arsene_selected = cv2.imread("images\\persona\\arsene_selected.JPG", 0)

tem_caroline_dialogue = cv2.imread("images\\persona\\caroline_dialogue.JPG", 0)
tem_fusion_go_ahead = cv2.imread("images\\persona\\fusion_go_ahead.JPG", 0)

tem_skip = cv2.imread("images\\persona\\skip.JPG", 0)
tem_almighty = cv2.imread("images\\persona\\almighty.JPG", 0)
tem_leave_message = cv2.imread("images\\persona\\leave_message.JPG", 0)
tem_leave_answer = cv2.imread("images\\persona\\leave_answer.JPG", 0)

tem_system = cv2.imread("images\\persona\\system.JPG", 0)
tem_load_data = cv2.imread("images\\persona\\load_data.JPG", 0)
tem_load = cv2.imread("images\\persona\\load.JPG", 0)
tem_confirm_load = cv2.imread("images\\persona\\confirm_load.JPG", 0)



def wait_for_template(template):
    while not scr.template_match(template):
        time.sleep(.1)
        scr.update_frames()
    time.sleep(.2)


def talk_to_igor():
    wait_for_template(tem_velvet_room)

    while not scr.template_match(tem_talk_igor):
        input.press(keys.left_up, .1)
        scr.update_frames()
    input.press(keys.cross)

    wait_for_template(tem_igor_dialogue)
    print("found igor's dialogue")
    input.press(keys.cross)


def to_fusion_screen():
    wait_for_template(tem_create_persona)
    input.press(keys.cross)

    wait_for_template(tem_persona_fusion)
    input.press(keys.cross)

    wait_for_template(tem_network_fusion)
    input.press(keys.dpad_up)
    input.press(keys.cross)


def start_fusion():
    wait_for_template(tem_network_fusion_screen)
    input.press(keys.dpad_up)
    input.press(keys.cross)

    wait_for_template(tem_arsene_selected)
    input.press(keys.cross)

    wait_for_template(tem_caroline_dialogue)
    input.press(keys.cross)

    wait_for_template(tem_fusion_go_ahead)
    input.press(keys.cross)


def conclude_fusion():
    time.sleep(6)
    input.press(keys.options)
    time.sleep(6)

    while True:
        scr.update_frames()
        if scr.template_match(tem_almighty, threshold=.8):
            return True
        if scr.template_match(tem_leave_message, threshold=.6):
            break
        input.press(keys.circle)
        time.sleep(1.5)

    input.press(keys.cross)

    wait_for_template(tem_leave_answer)
    input.press(keys.dpad_up)
    input.press(keys.cross)

    return False


def load_game():
    time.sleep(3)
    input.press(keys.triangle)

    wait_for_template(tem_system)
    time.sleep(.5)
    input.press(keys.dpad_up)
    input.press(keys.cross)

    wait_for_template(tem_load_data)
    time.sleep(.5)
    input.press(keys.dpad_up)
    input.press(keys.dpad_up)
    input.press(keys.dpad_up)
    input.press(keys.cross)

    wait_for_template(tem_load)
    time.sleep(1)
    input.press(keys.cross)

    wait_for_template(tem_confirm_load)
    time.sleep(.5)
    input.press(keys.cross)

mode = "test"

if mode == "screenshot":

    t = 0
    frames = 0

    while True:
        start_time = time.time()
        scr.update_frames()
        scr.show()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        frames += 1
        t += time.time() - start_time
        if t >= 1:
            print("fps: " + str(frames))
            t = 0
            frames = 0

else:

    time.sleep(8)

    while True:
        talk_to_igor()
        to_fusion_screen()
        start_fusion()
        if conclude_fusion() is True:
            break
        load_game()

