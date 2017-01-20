import oscP5.*;
import netP5.*;
//import osc library into processing

OscP5 oscp5;
float apx, apy, aprotatex, aprotatey, aprotatez;
float apmw, apmh;

void  setup() {
  size(640, 480, P3D);
  oscp5 = new OscP5(this, 8338);//Face OSC use port# 8338.

  oscp5.plug(this, "getPostion", "/pose/position");
  oscp5.plug(this, "facex",      "/pose/position/0");
  oscp5.plug(this, "facey",      "/pose/position/1");
  oscp5.plug(this, "getRotation", "/pose/orientation");
  oscp5.plug(this, "rotatex", "/pose/orientation/0");
  oscp5.plug(this, "rotatey", "/pose/orientation/1");
  oscp5.plug(this, "rotatez", "/pose/orientation/2");  
  oscp5.plug(this, "getMouthWidth",  "/gesture/mouth/width");
  oscp5.plug(this, "getMouthHeight", "/gesture/mouth/height");
}

void draw() {  
  background(0);
  
  pushMatrix();
  translate(apx, apy);
  rotateZ(aprotatez);
  drawAnpanman(0, 0, (int)apmh);  
  popMatrix();
}

public  void  getRotation(float rotatex, float rotatey, float rotatez){
  aprotatex = rotatex;
  aprotatey = rotatey;
  aprotatez = rotatez;  
}
public  void  getPostion(float facex, float facey) {
  apx = facex;
  apy = facey;
}

public  void  getMouthWidth(float mouthWidth) {
  apmw = mouthWidth;
}

public  void  getMouthHeight(float mouthHeight) {
  apmh = mouthHeight;
  println(apmh);//1.2->8
}

void drawAnpanman(int x, int y, int mouthHeight) {
  strokeWeight(3);
  stroke(0);
  
  fill(255, 165, 79);
  //ellipse(200, 200, 300, 280);
  ellipse(x, y, 300, 280);//face
  
  fill(0, 0, 0);
  ellipse(x-35, y-60, 25, 43);//eye
  ellipse(x+35, y-60, 25, 43);//eye
  
  fill(255, 0, 0);
  ellipse(x, y+10, 90, 80);//nose
  arc(x-94, y+10, 95, 95, -PI / 2, PI / 2);
  arc(x+94, y+10, 95, 95, PI / 2, PI * 1.5);
    
  //mouth
  noFill();
  //fill(150,50,50);
  //arc(x, y+20, 160, 120, PI / 6, PI * 5 / 6 );//mouth
  int mouthParameter = (mouthHeight)*4;
  arc(x, y+20+mouthParameter, 160, 120+mouthParameter, 
    PI/ mouthParameter, (mouthParameter-1)*PI/mouthParameter, CHORD); 
  
  noFill();
  arc(x-40, y-75, 70, 100, PI * 1, PI * 1.9);//brow
  arc(x+40, y-75, 70, 100, PI * 1.1, PI * 2);//brow
  
  noStroke();
  fill(255, 0, 0);
  arc(x-94, y+10, 95, 96, PI / 2, PI * 1.5);
  arc(x+94, y+10, 95, 96, -PI / 2, PI / 2);
  
  fill(255, 255, 255);
  rect(x-123, y-12, 19, 17);
  rect(x-20,  y-12, 27, 20);
  rect(x+70,  y-12, 19, 17);
}
