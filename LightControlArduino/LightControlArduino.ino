void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);

  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0){
    String value = Serial.readString();

    if(value == "1"){
      digitalWrite(13, HIGH);
    }else{
      digitalWrite(13, LOW);
    }
  }

}