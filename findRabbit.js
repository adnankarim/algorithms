//finding hopping rabbit

let pos =20;
let len=1000;
function step(){
  let prev =pos;
  if (Math.random()>0.5){
    pos++;
  }
  else{
    pos--;
    
  }
  pos=Math.min(pos,len)
  pos=Math.max(0,pos)
  
}
let condition=true;
let myCheck=Math.round(len/2);
while (condition){
  if (myCheck==pos)
  {
    console.log("found")
    condition=false;
  }
  else{
    step();
  }
}
  
  
