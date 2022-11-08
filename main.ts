GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Down, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    display.clear()
    gameField()
    if (y22 < 7 && A[x22][y22 + 1] != "#") {
        y22 += 1
    } else {
        GAME_ZIP64.runMotor(50)
    }
    pixelAt(x22, y22)
    testWin()
})
function pixelAt (x: number, y: number) {
    display.setMatrixColor(x, y, GAME_ZIP64.colors(ZipLedColors.Yellow))
    display.show()
}
function testWin () {
    if (A[x22][y22] == "A") {
        music.playMelody("C D E F G A B C5 ", 240)
    }
}
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Left, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    display.clear()
    gameField()
    if (x22 > 0 && A[x22 - 1][y22] != "#") {
        x22 += -1
    } else {
        GAME_ZIP64.runMotor(50)
    }
    pixelAt(x22, y22)
    testWin()
})
function gameField () {
    for (let i = 0; i <= 7; i++) {
        for (let j = 0; j <= 7; j++) {
            if (A[i][j] == "#") {
                display.setMatrixColor(i, j, GAME_ZIP64.colors(ZipLedColors.White))
            } else {
                display.setMatrixColor(i, j, GAME_ZIP64.colors(ZipLedColors.Black))
                if (A[i][j] == "A") {
                    display.setMatrixColor(i, j, GAME_ZIP64.colors(ZipLedColors.Green))
                }
            }
        }
    }
    display.show()
}
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Right, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    display.clear()
    gameField()
    if (x22 < 7 && A[x22 + 1][y22] != "#") {
        x22 += 1
    } else {
        GAME_ZIP64.runMotor(50)
    }
    pixelAt(x22, y22)
    testWin()
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Up, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    display.clear()
    gameField()
    if (y22 > 0 && A[x22][y22 - 1] != "#") {
        y22 += -1
    } else {
        GAME_ZIP64.runMotor(50)
    }
    pixelAt(x22, y22)
    testWin()
})
let y2 = 0
let x2 = 0
let done = false
let y22 = 0
let x22 = 0
let display: GAME_ZIP64.ZIP64Display = null
let A: string[][] = []
A = [
[
"#",
"#",
"#",
"#",
"#",
"#",
"#",
"#"
],
[
"#",
" ",
"#",
" ",
" ",
"#",
" ",
"#"
],
[
"#",
" ",
"#",
"#",
" ",
" ",
" ",
"#"
],
[
"#",
" ",
" ",
"#",
" ",
"#",
"#",
"#"
],
[
"#",
"#",
" ",
"#",
" ",
"#",
" ",
"#"
],
[
"#",
" ",
" ",
" ",
" ",
" ",
" ",
"#"
],
[
"#",
"#",
" ",
"#",
" ",
"#",
"A",
"#"
],
[
"#",
"#",
"#",
"#",
"#",
"#",
"#",
"#"
]
]
pins.touchSetMode(TouchTarget.P0, TouchTargetMode.Resistive)
pins.setMatrixWidth(DigitalPin.P0, 8)
GAME_ZIP64.setBuzzerPin()
display = GAME_ZIP64.createZIP64Display()
display.setBrightness(20)
display.clear()
x22 = 4
y22 = 4
gameField()
pixelAt(x22, y22)
basic.forever(function () {
    basic.pause(2000)
    for (let k = 0; k <= 7; k++) {
        for (let l = 0; l <= 7; l++) {
            if (A[k][l] == "A") {
                A[k][l] = " "
            }
        }
    }
    done = false
    while (!(done)) {
        x2 = randint(0, 7)
        y2 = randint(0, 7)
        if (!(A[x2][y2] == "#") && x2 != x22 && y2 != y22) {
            A[x2][y2] = "A"
            done = true
        }
    }
    display.clear()
    gameField()
    pixelAt(x22, y22)
})
