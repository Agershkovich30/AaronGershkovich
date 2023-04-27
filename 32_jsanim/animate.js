var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#0000FF";

var requestID;

var clear = (e) => {
    e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
};
var radius = 0;
var growing = true

var rectX = 250;
var rectY = 250;
var xVel = 2;
var yVel = 2;
const image = document.getElementById("source");

var logo = new Image();
logo.src = "logo_dvd.jpg";

    // var xVel = 10 * Math.cos(Math.random() *2 * MathPI);
    // var yVel = 10 * Math.sin(Math.random() *2 * MathPI);

    var logo = new Image();
    logo.src = "logo_dvd.jpg";


var dvdLogo =  function() {
    var rectX = Math.random(c.width-rectWidth);
    var rectY = Math.random(c.height- rectHeight);
    var rectWidth = 90;
    var rectHeight = 60;
    var update = () =>{
        clear();

    if(rectX >= c.width-rectWidth){
        xVel = -10 * Math.cos(Math.random() *2 * MathPI);
    }
    if(rectX <= 0){
        xVel = 10 * Math.cos(Math.random() *2 * MathPI);
      }
    if(rectY > c.height-rectHeight){
        yVel = -10 * Math.sin(Math.random() *2 * MathPI);
    }
    if(rectY <= 0){
      yVel = 10 * Math.sin(Math.random() *2 * MathPI);
    }
    rectX = rectX + xVel;
    rectY = rectY + yVel;

    ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);

    stopIt();
    requestID = window.requestAnimationFrame(dvdLogo);
    }
update();
}

var radius = 0;
var growing  = true;


let drawCirc = function() {
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, Math.PI*2);
    ctx.fill();
    ctx.closePath();
  }

var drawDot = () => {
    clear();
    if(radius==c.width/2){
        growing = false;
    }
    else if(radius==0){
        growing = true;
    }

    if (growing){
        radius++;
    }else{
        radius--;
     }

    drawCirc();

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}


var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click",drawDot);
dvdButton.addEventListener("click", dvdLogo);
stopButton.addEventListener("click", stopIt);
