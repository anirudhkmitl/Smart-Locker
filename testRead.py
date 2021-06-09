from time import sleep
import sys
from mfrc522 import SimpleMFRC522


class RfidReader:
    def readRfid():
        reader = SimpleMFRC522()
        try:    
            print("Hold a tag near the reader")
            id, text = reader.read()
            #print("ID: %s\nText: %s" % (id,text))
            return id

        except KeyboardInterrupt:
            GPIO.cleanup()
            raisefvg
                

#RfidReader.readRfid()
