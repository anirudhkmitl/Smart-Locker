import pymysql
from testRead import RfidReader
import time
#database connection

# some other statements  with the help of cursor

class RfidConfirm :
    def rfidUserValidate():
        connection = pymysql.connect(host="localhost",user="root",passwd="password",database="smartLocker" )
        cursor = connection.cursor()
        connection.commit()
        userPass = False
        while not(userPass):
            retrive = "Select rfid_code from access_list;"
             
            #executing the quires
            cursor.execute(retrive)
            rows = cursor.fetchall()

            rfid_id = str(RfidReader.readRfid())
            #pin = "Select pin from access_list where rfid_code = %s"
            #print(type(rfid_id))
            for row in rows :
                if rfid_id in row[0] :
                    userPass = True
                    print("Onto the PIN page...")
                    
        
            print("--------------------------")
            
        sql_pin = ("Select pin from access_list where rfid_code = %s" % rfid_id)
        cursor.execute(sql_pin)
        rfid_pin = cursor.fetchall()
        
        connection.close()
        return rfid_pin[0][0]
            
              
            
    

#rfidUserValidate() 
#commiting the connection then closing it.

