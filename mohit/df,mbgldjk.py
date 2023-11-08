from os import system 
from time import sleep 
a=(("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","kumar","Pundir","Rana",1),
("What is your name ?","Mohit","Kumar","pundir","Rana",1))
p = (0.0000,10000,20000,30000,40000,50000,100000,200000,300000,400000,500000,1000000,2000000,3000000,4000000,5000000,10000000,50000000,70000000)
f=6
print("Your question is.....")
for n,q in enumerate(a):
    if n==0:
        f=p[0]
        
    elif n<6:
        f=p[1]
        
    elif n<12:
        f=p[6]
        
    elif n==18:
        f=p[19]
    else:
        f=p[12]
    sleep(1)
    system('clear')
    print(f"If you loss the game than you have only Rs.{f}\n")
    print(f"If you quit the game than you won \nRs.{p[n]}\n")
    print(f"Q{n+1}. {q[0]} ")
    print(f"1. {q[1]}\n2. {q[2]}\n3. {q[3]}\n4. {q[4]}\n")
    while True:
        try:
            ans=int(input(f"If you want to quit press 0\nYour answer of Q{n+1} (1-4):: "))
            if 0>ans or ans>4 :
                raise
            break
        except:
            print("ERROR")
    for b in [5,4,3,2,1,0]:
        system("clear")
        print(f"Cheaking your answer....... \n{b}")
        sleep(0.2)
    if ans==q[5]:
        system("clear")
        print(f"You won Rs.{p[n+1]}")
        sleep(1)
        system("clear")
        print("Your question is....." )
    elif ans==0:
        system("clear")
        print("You quit the game ")
        print(f"You won Rs.{p[n]}")
        break
    else:
        system("clear")
        print("Wrong answer")
        print(f"You have Rs.{f}")
        break