from twilio.rest import Client
import os

def Send_Msg(SID, AUTH, FROM, TO, Body):
  try:
    client = Client(SID, AUTH)

    message = client.messages.create(
                        body =  str(Body),
                        from_ = FROM,
                        to =    TO)
    return True
  except Exception as Err:
    print (f"Error Detected : '{Err}' ")
try:
  with open("Twilio.conf","r") as f:
  if f.read() == "":
    print("File appears to be empty")
 else:
   lines = f.readlines()
   SID = lines[0].replace("SID=","")
   AUTH = lines[1].replace("AUTH=","")
   FROM = lines[2].replace("FROM=","")
   TO = lines[3].replace("TO","")
except FileNotFoundError:
  print("File 'Twilio.conf' cannot be found, have you ran the 'init.py' script?") 
  quit()

