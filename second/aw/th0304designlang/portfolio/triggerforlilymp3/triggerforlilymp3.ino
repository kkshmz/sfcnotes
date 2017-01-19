#include < SPI.h > 
#include < SdFat.h > 
#include < SFEMP3Shield.h >

const int TRIG1 = A0;
const int TRIG2 = A4;
const int TRIG3 = A5;
const int TRIG4 = 1;
const int TRIG5 = 0;
int trigger[5] = {
  TRIG1,
  TRIG2,
  TRIG3,
  TRIG4,
  TRIG5
};

const int ROT_LEDR = 10; // Red LED in rotary encoder (optional)
const int EN_GPIO1 = A2; // Amp enable + MIDI/MP3 mode select
const int SD_CS = 9; // Chip Select for SD card

SFEMP3Shield MP3player;
SdFat sd;

boolean debugging = true;
boolean interrupt = true;
boolean interruptself = false;

char filename[5][13];

void setup() {
  int x, index;
  SdFile file;
  byte result;
  char tempfilename[13];

  for (x = 0; x <= 4; x++) {
    pinMode(trigger[x], INPUT);
    digitalWrite(trigger[x], HIGH);
  }

  // If serial port debugging is inconvenient, you can connect
  // a LED to the red channel of the rotary encoder to blink
  // startup error codes:

  pinMode(ROT_LEDR, OUTPUT);
  digitalWrite(ROT_LEDR, HIGH); // HIGH = off

  // The board uses a single I/O pin to select the
  // mode the MP3 chip will start up in (MP3 or MIDI),
  // and to enable/disable the amplifier chip:

  pinMode(EN_GPIO1, OUTPUT);
  digitalWrite(EN_GPIO1, LOW); // MP3 mode / amp off

  // If debugging is true, initialize the serial port:
  // (The 'F' stores constant strings in flash memory to save RAM)

  if (debugging) {
    Serial.begin(9600);
    Serial.println(F("Lilypad MP3 Player trigger sketch"));
  }

  // Initialize the SD card; SS = pin 9, half speed at first

  if (debugging) Serial.print(F("initialize SD card... "));

  result = sd.begin(SD_CS, SPI_HALF_SPEED); // 1 for success

  if (result != 1) // Problem initializing the SD card
  {
    if (debugging) Serial.print(F("error, halting"));
    errorBlink(1); // Halt forever, blink LED if present.
  } else
  if (debugging) Serial.println(F("success!"));

  // Start up the MP3 library

  if (debugging) Serial.print(F("initialize MP3 chip... "));

  result = MP3player.begin(); // 0 or 6 for success

  // Check the result, see the library readme for error codes.

  if ((result != 0) && (result != 6)) // Problem starting up
  {
    if (debugging) {
      Serial.print(F("error code "));
      Serial.print(result);
      Serial.print(F(", halting."));
    }
    errorBlink(result); // Halt forever, blink red LED if present.
  } else
  if (debugging) Serial.println(F("success!"));

  // Now we'll access the SD card to look for any (audio) files
  // starting with the characters '1' to '5':

  if (debugging) Serial.println(F("reading root directory"));

  // Start at the first file in root and step through all of them:

  sd.chdir("/", true);
  while (file.openNext(sd.vwd(), O_READ)) {
    // get filename

    file.getFilename(tempfilename);

    // Does the filename start with char '1' through '5'?      

    if (tempfilename[0] >= '1' && tempfilename[0] <= '5') {
      // Yes! subtract char '1' to get an index of 0 through 4.

      index = tempfilename[0] - '1';

      // Copy the data to our filename array.

      strcpy(filename[index], tempfilename);

      if (debugging) // Print out file number and name
      {
        Serial.print(F("found a file with a leading "));
        Serial.print(index + 1);
        Serial.print(F(": "));
        Serial.println(filename[index]);
      }
    } else
    if (debugging) {
      Serial.print(F("found a file w/o a leading number: "));
      Serial.println(tempfilename);
    }

    file.close();
  }

  if (debugging)
    Serial.println(F("done reading root directory"));

  if (debugging) // List all the files we saved:
  {
    for (x = 0; x <= 4; x++) {
      Serial.print(F("trigger "));
      Serial.print(x + 1);
      Serial.print(F(": "));
      Serial.println(filename[x]);
    }
  }
  MP3player.setVolume(10, 10);

  digitalWrite(EN_GPIO1, HIGH);
  delay(2);
}

void loop() {
  int t; // current trigger
  static int last_t; // previous (playing) trigger
  int x;
  byte result;

  for (t = 1; t <= (debugging ? 3 : 5); t++) {

    if (digitalRead(trigger[t - 1]) == LOW) {
      x = 0;
      while (x < 50) {
        if (digitalRead(trigger[t - 1]) == HIGH)
          x++;
        else
          x = 0;
        delay(1);
      }

      if (debugging) {
        Serial.print(F("got trigger "));
        Serial.println(t);
      }
      if (filename[t - 1][0] == 0) {
        if (debugging)
          Serial.println(F("no file with that number"));
      } else {

        if (interrupt && MP3player.isPlaying() && ((t != last_t) || interruptself)) {
          if (debugging)
            Serial.println(F("stopping playback"));

          MP3player.stopTrack();
        }

        result = MP3player.playMP3(filename[t - 1]);

        if (result == 0) last_t = t; // Save playing trigger

        if (debugging) {
          if (result != 0) {
            Serial.print(F("error "));
            Serial.print(result);
            Serial.print(F(" when trying to play track "));
          } else {
            Serial.print(F("playing "));
          }
          Serial.println(filename[t - 1]);
        }
      }
    }
  }
}

void errorBlink(int blinks) {
  int x;

  while (true) // Loop forever
  {
    for (x = 0; x < blinks; x++) // Blink the given number of times
    {
      digitalWrite(ROT_LEDR, LOW); // Turn LED ON
      delay(250);
      digitalWrite(ROT_LEDR, HIGH); // Turn LED OFF
      delay(250);
    }
    delay(1500); // Longer pause between blink-groups
  }
}
