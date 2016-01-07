function typesetCanvas() {
    // Generate the image data
    var Pic = document.getElementById("can").toDataURL("image/png");
    Pic = Pic.replace(/^data:image\/(png|jpg);base64,/, "")
    // Sending the image data to Server
    $.ajax({
           type: 'POST',
           url: 'typeset',
           data: '{ "base64PNGData" : "' + Pic + '" }',
           contentType: 'application/json; charset=utf-8',
           dataType: 'json',
           success: function (msg) {
           alert("Done, Picture Typeset and Analyzed.");
           }
           });
}

function trainFromCanvas(moleculeID) {
    // Generate the image data
    var Pic = document.getElementById("can").toDataURL("image/png");
    Pic = Pic.replace(/^data:image\/(png|jpg);base64,/, "")
    // Sending the image data to Server
    var jqxhr = $.ajax({
                       type: 'POST',
                       url: 'train',
                       data: '{ "moleculeID": "' + moleculeID + '", "base64PNGData": "' + Pic + '"}',
                       contentType: 'application/json; charset=utf-8'
                       })
        .always(function(data, textStatus, jqxhr) {
                window.location.href=data["redirect"];
        });
}

var canvas, ctx, flag = false,
    prevX = 0,
    currX = 0,
    prevY = 0,
    currY = 0,
    dot_flag = false;

var x = "black",
    y = 5;

// Variables to keep track of the touch position
var touchX,touchY;

function init() {
    canvas = document.getElementById('can');
    ctx = canvas.getContext("2d");
    w = canvas.width;
    h = canvas.height;

    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false);

    // React to touch events on the canvas
    canvas.addEventListener("touchmove", function (e) {
        findxy('touchmove', e)
    }, false);
    canvas.addEventListener("touchstart", function (e) {
        findxy('touchstart', e)
    }, false);
    canvas.addEventListener("touchend", function (e) {
        findxy('touchend', e)
    }, false);
}

function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = "black";
    ctx.lineWidth = y;
    ctx.stroke();
    ctx.closePath();
}

function erase() {
        ctx.clearRect(0, 0, w, h);
        document.getElementById("canvasimg").style.display = "none";
}

function findxy(res, e) {
    if (res == 'down' || res == 'touchstart') {
        prevX = currX;
        prevY = currY;
        if (res == 'down') {
            currX = e.pageX - canvas.offsetLeft;
            currY = e.pageY - canvas.offsetTop;
        } else if (res == 'touchstart') {
            getTouchPos(e);
            currX = touchX;
            currY = touchY;
        }
        flag = true;
        dot_flag = true;
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = x;
            ctx.fillRect(currX, currY, 2, 2);
            ctx.closePath();
            dot_flag = false;
        }
        if (res == 'touchstart') {
            // Prevents an additional mousedown event being triggered
            event.preventDefault();
        }
    }
    if (res == 'up' || res == "out" || res == "touchend") {
        flag = false;
    }
    if (res == 'move' || res == 'touchmove') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            if (res == 'move') {
                currX = e.pageX - canvas.offsetLeft;
                currY = e.pageY - canvas.offsetTop;
            } else if (res == 'touchmove') {
                getTouchPos(e);
                currX = touchX;
                currY = touchY;
            }
            draw();
        }
        if (res == 'touchmove') {
            // Prevents an additional mousedown event being triggered
            event.preventDefault();
        }
    }
}

function getTouchPos(e) {
    if (!e)
        var e = event;

    if(e.touches) {
        if (e.touches.length == 1) { // Only deal with one finger
            var touch = e.touches[0]; // Get the information for finger #1
            touchX=touch.pageX-touch.target.offsetLeft;
            touchY=touch.pageY-touch.target.offsetTop;
        }
    }
}
