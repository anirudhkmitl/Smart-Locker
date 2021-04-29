import pymysql
import testRead
import time
#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="password",database="smartLocker" )
cursor = connection.cursor()
# some other statements  with the help of cursor

def rfidUserValidate():
    userPass = False
    while not(userPass):
        retrive = "Select rfid_code from access_list;"

        #executing the quires
        cursor.execute(retrive)
        rows = cursor.fetchall()

        rfid_id = str(testRead.readRfid())
        print(type(rfid_id))
        for row in rows :
            if rfid_id in row[0] :
                userPass = True
                print("Onto the PIN page...")
                return userPass
        
        print("UAD")
        
          
            
    

rfidUserValidate()
    
#commiting the connection then closing it.
connection.commit()
connection.close()
