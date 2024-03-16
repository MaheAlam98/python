a=[
    
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["September 27 is celebrated every year as","Teachers' Day","National Integration Day","World Tourism Day","International Literacy Day",3],
["Good Friday' is observed to commemorate the event of","birth of Jesus Christ","birth of' St. Peter","crucification 'of Jesus Christ","rebirth of Jesus Christ",3],
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
   
   
   
   ]
levels=[1000,2000,3000,4000,5000,6000,8000]
money=0
for i in range(0, len(a)):
    question=a[i]
    print(f"Question for tk:{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}       b.{question[2]}")
    print(f"c.{question[3]}       d.{question[4]}")
    ans=int(input("Enter your answers(1-4):"))
    if(ans==question[-1]):
        print("Correct ans \n you win\n\n")
        money=money+levels[i]
        if(i==5):
            print("You got 5000 tk")
            
    else:
        print("Wrong Ans\n\n")
        print(f"Correct ans is {question[-1]}\n End the game")
        print(f"You got final amount:{money}")
        break



