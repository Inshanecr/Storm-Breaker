from module.colors import c
def show_message(msg):
    if msg == "loc":
        print(c.red+"\nWaiting for User Interaction ! ! !\n")
    
    elif msg == "mic":
        print(c.red+"\nWaiting to receive victim Voice ! ! ! \n")

    elif msg == "webcam":
        print(c.red+"\nWaiting to receive victim Picture ! ! !\n")
    
