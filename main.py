szam = 0

def on_gesture_shake():
    global szam
    szam = randint(0, 2)
    if szam == 0:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    else:
        if szam == 1:
            basic.show_leds("""
                # # # # #
                                # . . . #
                                # . . . #
                                # . . . #
                                # # # # #
            """)
        else:
            basic.show_leds("""
                # # . . #
                                # # . # .
                                . . # . .
                                # # . # .
                                # # . . #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
