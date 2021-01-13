# Init.py 
YES = ("Y","YES","CONFIRM","+")
NO = ("N","NO","DISCONFIRM","-")

def Write()
  while True:
    SID = input("SID : ")
    SidLine = f"SID={SID}"
    AUTH = input("AUTHKEY : "
    AuthLine = f"\nAUTH={AUTH}"
    FROM = input("FROM : ")
    FromLine = f"\nFROM={FROM}"
    TO = input("TO : ")
    ToLine = f"\nTO={TO}"
    while True:
      Confirmation = input(f"Name | Value
      SID  | {SID}
      AUTH | {AUTH}
      FROM | {FROM}
      To   | {TO}
                            ")
      if Confirmation in YES:
        break
      
    
  with open("Twilio.conf","a") as f:
    f.writelines([SidLine],[AuthLine],[FromLine],[ToLine])

with open("Twilio.conf","a") as f:
  if f.read() == ""
    Write()
  else:
    while True:
      Confirmation = input("Are you sure you wish to overwrite this file?")
      if Confirmation in YES:
        Write()
        break
      elif Confirmation in NO:
        exit()