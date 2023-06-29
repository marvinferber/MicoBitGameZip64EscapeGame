def my_function():
    global y22
    if running and not (finished):
        display.clear()
        gameField()
        if y22 < 7 and A[x22][y22 + 1] != "#":
            y22 += 1
        else:
            GAME_ZIP64.run_motor(50)
        pixelAt(x22, y22)
        testWin()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.DOWN,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function)

def my_function2():
    global running
    running = True
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.FIRE1,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function2)

def my_function3():
    global running
    running = True
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.FIRE2,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function3)

def pixelAt(x: number, y: number):
    display.set_matrix_color(x, y, GAME_ZIP64.colors(ZipLedColors.YELLOW))
    display.show()
def testWin():
    global hit
    if A[x22][y22] == "A":
        music.play_melody("C D E F G A B C5 ", 240)
        hit += 1

def my_function4():
    global x22
    if running and not (finished):
        display.clear()
        gameField()
        if x22 > 0 and A[x22 - 1][y22] != "#":
            x22 += -1
        else:
            GAME_ZIP64.run_motor(50)
        pixelAt(x22, y22)
        testWin()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.LEFT,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function4)

def gameField():
    for i in range(8):
        for j in range(8):
            if A[i][j] == "#":
                display.set_matrix_color(i, j, GAME_ZIP64.colors(ZipLedColors.WHITE))
            else:
                display.set_matrix_color(i, j, GAME_ZIP64.colors(ZipLedColors.BLACK))
                if A[i][j] == "A":
                    display.set_matrix_color(i, j, GAME_ZIP64.colors(ZipLedColors.GREEN))
    display.show()

def my_function5():
    global x22
    if running and not (finished):
        display.clear()
        gameField()
        if x22 < 7 and A[x22 + 1][y22] != "#":
            x22 += 1
        else:
            GAME_ZIP64.run_motor(50)
        pixelAt(x22, y22)
        testWin()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.RIGHT,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function5)

def my_function6():
    global y22
    if running and not (finished):
        display.clear()
        gameField()
        if y22 > 0 and A[x22][y22 - 1] != "#":
            y22 += -1
        else:
            GAME_ZIP64.run_motor(50)
        pixelAt(x22, y22)
        testWin()
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.UP,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function6)

y2 = 0
x2 = 0
done = False
hit = 0
finished = False
running = False
y22 = 0
x22 = 0
display: GAME_ZIP64.ZIP64Display = None
A: List[List[str]] = []
A = [["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", " ", " ", " ", "#"],
    ["#", " ", " ", "#", " ", "#", "#", "#"],
    ["#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", " ", "#", " ", "#", "A", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]]
pins.touch_set_mode(TouchTarget.P0, TouchTargetMode.RESISTIVE)
pins.set_matrix_width(DigitalPin.P0, 8)
GAME_ZIP64.set_buzzer_pin()
display = GAME_ZIP64.create_zip64_display()
display.set_brightness(20)
display.clear()
x22 = 4
y22 = 4
cx = 4
cy = 4

def on_forever():
    global done, x2, y2
    basic.pause(2000)
    if not (running) or finished:
        if not (finished):
            display.clear()
            display.set_matrix_color(7, 5, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.set_matrix_color(6, 5, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.set_matrix_color(5, 5, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.set_matrix_color(4, 5, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.set_matrix_color(3, 5, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.set_matrix_color(6, 6, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.set_matrix_color(6, 4, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.set_matrix_color(5, 7, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.set_matrix_color(5, 3, GAME_ZIP64.colors(ZipLedColors.WHITE))
            display.show()
        else:
            display.clear()
            display.show()
            basic.pause(5000)
            control.reset()
    else:
        for k in range(8):
            for l in range(8):
                if A[k][l] == "A":
                    A[k][l] = " "
        done = False
        while not (done):
            x2 = randint(0, 7)
            y2 = randint(0, 7)
            if not (A[x2][y2] == "#") and x2 != x22 and y2 != y22:
                A[x2][y2] = "A"
                done = True
        display.clear()
        gameField()
        pixelAt(x22, y22)
basic.forever(on_forever)

def on_in_background():
    global cx, cy, finished
    while not (running):
        basic.show_icon(IconNames.GHOST)
        basic.pause(200)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        # . # . #
        # # # # #
        """)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . # # # .
        """)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    gameField()
    pixelAt(x22, y22)
    while cx >= 0 and cy >= 0:
        led.plot(cx, cy)
        basic.pause(1000)
        cx += -1
        if cx < 0:
            cx = 4
            cy += -1
    finished = True
    basic.show_number(hit)
control.in_background(on_in_background)
