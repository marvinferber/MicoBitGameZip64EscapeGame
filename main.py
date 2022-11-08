def my_function():
    global y22
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

def pixelAt(x: number, y: number):
    display.set_matrix_color(x, y, GAME_ZIP64.colors(ZipLedColors.YELLOW))
    display.show()
def testWin():
    if A[x22][y22] == "A":
        music.play_melody("C D E F G A B C5 ", 240)

def my_function2():
    global x22
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
    my_function2)

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

def my_function3():
    global x22
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
    my_function3)

def my_function4():
    global y22
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
    my_function4)

y2 = 0
x2 = 0
done = False
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
gameField()
pixelAt(x22, y22)

def on_forever():
    global x2, y2, x22, y22, done
    basic.pause(2000)
    for k in range(8):
        for l in range(8):
            if A[k][l] == "A":
                A[k][l] = " "
    done = False
    while not (done):
        x2 = randint(0, 7)
        y2 = randint(0, 7)
        if (not A[x2][y2] == "#") and x2 != x22 and y2 != y22:
            A[x2][y2] = "A"
            done = True
    display.clear()
    gameField()
    pixelAt(x22, y22)
basic.forever(on_forever)
