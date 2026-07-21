def main():
    name=input("what's your name?")
    if name_is(name):
        print("gryffinder")
    else:
        print("who?")
       
def name_is(home):
        if home =="harry" or "ram" or "king":
            return True
    
        else:
            return False
        



     
main()