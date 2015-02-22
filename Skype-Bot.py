import Skype4Py
import time

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

print(skype.Call.GetConfrenceId(self))
def OnMessageStatus(Message, Status): #The function we will call on event
#The event handler will define Messsage object and a status string
    if Status == 'RECEIVED':
            body = Message.Body
            from_handle = Message.FromHandle
            print "%s: %s" % (from_handle, body)
skype.OnMessageStatus = OnMessageStatus #Connect the function and event
while 1: #do nothing, wait for event to happen
    time.sleep(0.5)
