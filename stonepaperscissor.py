import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=='st':
        if you=='p':
          return True
        elif you=='sc':
            return False
    elif comp=='p':
        if you=='sc':
          return True
        elif you=='st':
            return False
    elif comp=='sc':
        if you=='st':
          return True
        elif you=='p':
            return False

print("Computer's Turn : Stone(st), Paper(p) or Scissor(sc)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='st'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='sc'



userinput=input("User's Turn : Stone(st), Paper(p) or Scissor(sc)? ")

a=game(comp,userinput)
print(f"Computer's input: {comp}")
print(f"User's input: {userinput}")
if a==None:
    print("It's a tie!")
elif a==True:
    print("You won!")
else:
    print("You lost!")




    