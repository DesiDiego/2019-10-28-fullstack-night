let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');
let width = 1920;
let height = 1080;
let gravity = {
    ax: 0.1,
    ay: 0.4,
}
accDir = {
    x: '',
    y: '',
}


let gravObjs = [
    obj01 = {ax:  0.0, ay:  0.5},
    obj02 = {ax: -0.1, ay:  0.4},
    obj03 = {ax: -0.2, ay:  0.3},
    obj04 = {ax: -0.3, ay:  0.2},
    obj05 = {ax: -0.4, ay:  0.1},

    obj06 = {ax: -0.5, ay:  0.0},
    obj07 = {ax: -0.4, ay: -0.1},
    obj08 = {ax: -0.3, ay: -0.2},
    obj09 = {ax: -0.2, ay: -0.3},
    obj10 = {ax: -0.1, ay: -0.4},

    obj11 = {ax:  0.0, ay: -0.5},
    obj12 = {ax:  0.1, ay: -0.4},
    obj13 = {ax:  0.2, ay: -0.3},
    obj14 = {ax:  0.3, ay: -0.2},
    obj15 = {ax:  0.4, ay: -0.1},

    obj16 = {ax:  0.5, ay:  0.0},
    obj17 = {ax:  0.4, ay:  0.1},
    obj18 = {ax:  0.3, ay:  0.2},
    obj19 = {ax:  0.2, ay:  0.3},
    obj20 = {ax:  0.1, ay:  0.4},
]
// let ax = 0.1
// let ay = 0.4
let r = 3

let rainbowBalls = [
    red = {
        color: 'red',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    orange = {
        color: 'orange',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    yellow = {
        color: 'yellow',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    green = {
        color: 'green',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    blue = {
        color: 'blue',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    indigo = {
        color: 'indigo',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    violet = {
        color: 'violet',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
]

function borderCollision(rainbowBalls) {
    for (let i=0; i<rainbowBalls.length; i++) {
        if (rainbowBalls[i].px <= rainbowBalls[i].radius || rainbowBalls[i].px >= width - rainbowBalls[i].radius) {
            //friction
            // rainbowBalls[i].vx *= -0.99
            // rainbowBalls[i].vy *= 0.99
            //no friction
            rainbowBalls[i].vx *= -1



        }
        if (rainbowBalls[i].py <= rainbowBalls[i].radius || rainbowBalls[i].py >= height - rainbowBalls[i].radius) {
            //friction
            // rainbowBalls[i].vy *= -0.99
            // rainbowBalls[i].vx *= 0.99
            //no friction
            rainbowBalls[i].vy *= -1
        } 
        rainbowBalls[i].px += rainbowBalls[i].vx
        rainbowBalls[i].py += rainbowBalls[i].vy

    }
}

function drawBalls(rainbowBalls) {
    for (let i=0; i<rainbowBalls.length; i++) {
        ctx.beginPath();
        ctx.arc(rainbowBalls[i].px, rainbowBalls[i].py, rainbowBalls[i].radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = rainbowBalls[i].color;
        ctx.fill();
    }
}

function moveBalls(rainbowBalls) {
    for (let i=0; i<rainbowBalls.length; i++) {
        let ball = rainbowBalls[i]
        ball.vx += gravity.ax
        ball.vy += gravity.ay
        ball.px += ball.vx
        ball.py += ball.vy
    }
}

function rainbowLoop() {
    ctx.fillStyle = 'hsla(0, 0%, 0%, 0.05)'
    ctx.fillRect(0, 0, width, height);
    moveBalls(rainbowBalls);
    borderCollision(rainbowBalls);
    explode()
    drawBalls(rainbowBalls);
    requestAnimationFrame(rainbowLoop)
}

rainbowLoop()

function changeGrav () {
    setTimeout(changeGrav, 15000)
    // ctx.clearRect(0, 0, width, height);
    if (gravity.ay === 0.5) {
        gravity.ay = 0;
        gravity.ax = -0.5;
    } else if (gravity.ax === -0.5) {
        gravity.ax = 0;
        gravity.ay = -0.5;
    } else if (gravity.ay === -0.5) {
        gravity.ay = 0;
        gravity.ax = 0.5;
    } else if (gravity.ax = 0.5) {
        gravity.ax = 0;
        gravity.ay = 0.5
    }
}

function changeGrav2 () {
    setTimeout(changeGrav2, 1000)

    if ((gravity.ax <= 0 && gravity.ax > -0.5) && (gravity.ay > 0 && gravity.ay <= 0.5)) {
        accDir.x = 'left';
        accDir.y = 'up';
    } else if ((gravity.ax >= -0.5 && gravity.ax < 0) && (gravity.ay <= 0 && gravity.ay > -0.5)) {
        accDir.x = 'right';
        accDir.y = 'up';
    } else if ((gravity.ax >= 0 && gravity.ax <0.5) && (gravity.ay >= -0.5 &&gravity.ay < 0)) {
        accDir.x = 'right';
        accDir.y = 'down';
    } else if ((gravity.ax <= 0.5 && gravity.ax > 0) && (gravity.ay > 0 && gravity.ay < 0.5)) {
        accDir.x = 'left';
        accDir.y = 'down'
    }
    
    if (accDir.x === 'left') {
        gravity.ax -= .1;
    } else if (accDir.x === 'right') {
        gravity.ax += .1
    }

    if (accDir.y === 'up') {
        gravity.ay -= .1;
    } else if (accDir.y === 'down') {
        gravity.ay += .1;
    }
    console.log(gravity)
    console.log(accDir)
}

function changeGrav3 () {
    setTimeout(changeGrav3, 5000)

    for (let i=0; i<gravObjs.length; i++) {
        if (gravity.ax === gravObjs[i].ax && gravity.ay === gravObjs[i].ay) {
            gravity.ax = gravObjs[(i + 1) % gravObjs.length].ax
            gravity.ay = gravObjs[(i + 1) % gravObjs.length].ay
            break
        }
    }
}

function getBigger() {
    setTimeout(getBigger, 5000)
    for (let i=0; i<rainbowBalls.length; i++) {
        rainbowBalls[i].radius += 1
    }
}

function getBigger2() {
    setTimeout(getBigger2, 1000)
    for (let i=0; i<rainbowBalls.length; i++) {
        rainbowBalls[i].radius += Math.random()*rainbowBalls[i].radius
    }
}

function getBigger3() {
    setTimeout(getBigger3, 100)
    for (let i=0; i<rainbowBalls.length; i++) {
        rainbowBalls[i].radius += Math.random()*rainbowBalls[i].radius * 0.1;
    }
}

function explode() {
    for (let i=0; i<rainbowBalls.length; i++) {
        if (rainbowBalls[i].radius >= 100) {
            for (let j=0; j<1; j++) {
                let newBall = {
                    color: rainbowBalls[i].color,
                    radius: r,
                    px: rainbowBalls[i].px,
                    py: rainbowBalls[i].py,
                    vx: (2*Math.random() - 1)*15,
                    vy: (Math.random()*-1)*15,
                }
                rainbowBalls.push(newBall)
            }
            rainbowBalls[i].radius = r
        }
    }
}

// changeGrav3()
getBigger3()