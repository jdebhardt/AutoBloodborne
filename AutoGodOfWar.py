import time
import input
import keys


def shoot():
    input.press(keys.square)
    time.sleep(2)


while True:

    print()

    for g in range(7):
            print("Shooting in: " + str(70 - 10*g))
            time.sleep(10)

    print("Shooting commenced")

    for f in range(6):
        shoot()

    print("Shooting concluded")
    print()

