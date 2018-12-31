var Blynk = require("blynk-library");

var sense = require("node-sense-hat");

var AUTH = "272cd5d44c66493b8e583b071dab117b";

var blynk = new Blynk.Blynk(AUTH);

var v1 = new blynk.VirtualPin(1);

var blue =[0,0,255];
sense.Leds.clear();

v1.on('write', function(param) {
  console.log('V1:', param[0]);
  if (param[0]==1){
        sense.Leds.clear(blue)
   }else{
        sense.Leds.clear();
   }
});
