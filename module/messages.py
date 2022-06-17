from module.colors import c

#Message for After_click function 
def show_message(msg):
    if msg == "loc":
        print(c.yellow+"\n[ - ] "+c.red+"Waiting for User Interaction ! ! !\n")
    
    elif msg == "mic":
        print(c.yellow+"\n[ - ] "+c.red+"\nWaiting to receive victim Voice ! ! ! \n")

    elif msg == "webcam":
        print(c.yellow+"\n[ - ] "+c.red+"Waiting to receive victim Picture ! ! !\n")
