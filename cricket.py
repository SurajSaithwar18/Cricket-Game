import random
n=int(input("Enter the number of ball to play:"))
lst=[1,2,3,4,5,6,7,8,9,0]
wicket=12
C_run=0
C_wicket_fall=0
choice_=[]
for i in range(n):
    choice= random.choice(lst)
    choice_.append(choice)
print(choice_)
for i in choice_:
    if C_wicket_fall>=wicket:
        break
    if i==1:
        print("One Run")
        C_run+=1
    elif i==2:
        C_run+=2
        print("Two runs")
    elif i==3:
        C_run+=3
        print("Three runs")
    elif i==4:
        C_run+=4
        print("Four runs")
    elif i==5 or i==7 or i==8 or i==9:
        C_wicket_fall+=1
        print("OUT")
    elif i==6:
        C_run+=6
        print("Six runs")
    else:
        print("No Run")
print("Total: ")
print("You Score= ", C_run)
print("Wicket Falls: ",C_wicket_fall)

