let w = window.innerWidth;
let h = window.innerHeight;
let canvas = document.getElementById("canvas");
canvas.width = w;
canvas.height = h;
let ctx = canvas.getContext("2d");

let text_arr = ['500', 'Server Error', '500 Server Error', 'Error', 'error', '连接不上服务器', '服务器异常'];  //显示文字
let text_num = random(100, 500); //页面要显示的文字个数
let word_arr = []; //储存文字坐标等属性的数组
let txt_min_size = 10; //文字最小大小
let txt_max_size = 50; //文字最大大小
let keypress = false; //默认键盘未点击状态，点击键盘实现加速效果
let acclerate = 3; //点击键盘加速速率

window.addEventListener('keydown', function () {
    keypress = true;
}, true);
window.addEventListener('keyup', function () {
    keypress = false;
}, true);

//生成一个随机数
function random(min, max) {
    return Math.random() * (max - min + 1) + min;
}

//实现不同大小文字的移动速度不同
//out_min 最小速度
//out_max 最大速度
function range_map(value, in_min, in_max, out_min, out_max) {
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

// 返回一个数的平方根
// a² + b² = c²
function distance(x, y, x1, y1) {
    return Math.sqrt((x1 - x) * (x1 - x) + (y1 - y) * (y1 - y));
}

//储存文字坐标位置
function saveText() {
    for (let i = 0; i < text_num; i++) {
        let t = {
            x: random(0, w),
            y: random(0, h),
            text: text_arr[~~random(0, text_arr.length)],
            size: ~~random(txt_min_size, txt_max_size)
        };
        word_arr.push(t)
    }
    console.log(word_arr)
}

//在canvas绘制文字移动效果
function draw() {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = "green";
    for (let i = 0; i < word_arr.length; i++) {
        //文字大小，样式
        ctx.font = word_arr[i].size + "px sans-serif";
        //文字宽度
        let t_w = ctx.measureText(word_arr[i].text);
        ctx.fillText(word_arr[i].text, word_arr[i].x, word_arr[i].y);
        if (keypress) {
            word_arr[i].x += range_map(word_arr[i].size, txt_min_size, txt_max_size, 2, 4) * acclerate;
        } else {
            word_arr[i].x += range_map(word_arr[i].size, txt_min_size, txt_max_size, 2, 3);
        }
        //如果大于窗口宽度，那么重新返回，并且随机y轴位置和大小
        if (word_arr[i].x >= w) {
            word_arr[i].x = -t_w.width * 5;
            word_arr[i].y = random(0, h);
            word_arr[i].size = ~~random(txt_min_size, txt_max_size);
        }
    }
    ctx.fill();
    window.requestAnimationFrame(draw)
}

saveText();
draw();