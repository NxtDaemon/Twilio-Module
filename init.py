import os 

# Init.py 
YES = ("Y","YES","CONFIRM","+")
NO = ("N","NO","DISCONFIRM","-")

def Write():
  while True:
    SID = input("SID : ")
    SidLine = f"SID={SID}"
    AUTH = input("AUTHKEY : ")
    AuthLine = f"\nAUTH={AUTH}"
    FROM = input("FROM : ")
    FromLine = f"\nFROM={FROM}"
    TO = input("TO : ")
    ToLine = f"\nTO={TO}"
    while True:
      Confirmation = input(f"""Name | Value
      SID  | {SID}
      AUTH | {AUTH}
      FROM | {FROM}
      To   | {TO}
      Are These Correct? """).upper()
      if Confirmation in YES:
        with open("Twilio.conf","a+") as f:
          f.writelines([SidLine,AuthLine,FromLine,ToLine]) 
          quit()
      if Confirmation in NO:
        break
      else:
        print("Invalid Assignment")


f = open("Twilio.conf","a")  
try:
  R = open("Twilio.conf","r")
  data = R.read()
  if data == "":
    Write()
  else:
      while True:
        Confirmation = input("Are you sure you wish to overwrite this file?").upper()
        if Confirmation in YES:
          f.close()
          R.close()
          os.remove("Twilio.conf")
          Write()
          break
        elif Confirmation in NO:
          exit()
except Exception as Err:
  print(f"Err '{Err}' Found ")