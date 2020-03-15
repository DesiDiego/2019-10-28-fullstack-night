var app = new Vue({
    el: '#app',
    data: {
        view: ['test01', 'test02', 'test03', 'test04'],
        i: 0,
    },
    components: {
        'test01': {
            template: `<div>Test 01</div>`
        },
        'test02': {
            template: `<div>Test 02</div>`
        },
        'test03': {
            template: `<div>Test 03</div>`
        },
        'test04': {
            template: `<div>Test 04</div>`
        },
    
    },
    methods: {
        forward: function() {
            if (this.i < this.view.length - 1) {
                this.i++;
            }
        },
        backward: function() {
            if (this.i > 0) {
                this.i--;
            }
        }
    }
})

let width = 500;
let height = 500;
let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');

let ball1 = {
    color: 'green',
    radius: Math.random() * (width/4),
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,
    ay: Math.random() / 10,//gravity
};

let ball2 = {
    color: 'blue',
    radius: Math.random() * (width/4),
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,
    ay: Math.random() / 10,//gravity
}

let ball3 = {
    color: 'yellow',
    radius: Math.random() * (width/4),
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,
    ay: Math.random() / 10,//gravity
}

let ballsArray = [ball1, ball2, ball3]

function main_loop() {
    ctx.clearRect(0, 0, width, height);
    // ctx.fillStyle = 'red', 0.0000000001;
    // ctx.fillRect(0, 0, width, height);
    // update the ball's position
    for (let i=0; i < ballsArray.length; i++) {
        ballsArray[i].vy += ballsArray[i].ay //gravity
        ballsArray[i].px += ballsArray[i].vx
        ballsArray[i].py += ballsArray[i].vy
    
        // check if it hit a boundary
        if (ballsArray[i].px < 0 || ballsArray[i].px > width) {
            ballsArray[i].vx *= -1
            ballsArray[i].vx *= .99 //friction
            ballsArray[i].vy *= .99 //friction
        }
        if (ballsArray[i].py < 0 || ballsArray[i].py > width) {
            ballsArray[i].vy *= -1
            ballsArray[i].vx *= .99 //friction
            ballsArray[i].vy *= .99 //friction
        }
    
        // draw the ballsArray[i]
        ctx.beginPath();
        ctx.arc(ballsArray[i].px, ballsArray[i].py, ballsArray[i].radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = ballsArray[i].color;
        ctx.fill();
    }
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);