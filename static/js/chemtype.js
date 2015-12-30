        function typesetCanvas() {
            // Generate the image data
            var Pic = document.getElementById("can").toDataURL("image/png");
            Pic = Pic.replace(/^data:image\/(png|jpg);base64,/, "")
            <!--            console.log(Pic)-->
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

        function trainFromCanvas() {
            // Generate the image data
            var Pic = document.getElementById("can").toDataURL("image/png");
            Pic = Pic.replace(/^data:image\/(png|jpg);base64,/, "")
            <!--            console.log(Pic)-->
            // Sending the image data to Server
            $.ajax({
                   type: 'POST',
                   url: 'train',
                   data: '{ "base64PNGData" : "' + Pic + '" }',
                   contentType: 'application/json; charset=utf-8',
                   dataType: 'json',
                   success: function (msg) {
                   alert("Done, Training Picture Uploaded.");
                   }
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
                if (res == 'down') {
                    prevX = currX;
                    prevY = currY;
                    currX = e.pageX - canvas.offsetLeft;
                    currY = e.pageY - canvas.offsetTop;

                    flag = true;
                    dot_flag = true;
                    if (dot_flag) {
                        ctx.beginPath();
                        ctx.fillStyle = x;
                        ctx.fillRect(currX, currY, 2, 2);
                        ctx.closePath();
                        dot_flag = false;
                    }
                }
                if (res == 'up' || res == "out") {
                    flag = false;
                }
                if (res == 'move') {
                    if (flag) {
                        prevX = currX;
                        prevY = currY;
                        currX = e.pageX - canvas.offsetLeft;
                        currY = e.pageY - canvas.offsetTop;
                        draw();
                    }
                }
            }
