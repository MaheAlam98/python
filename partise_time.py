import time
ct=int(time.strftime('%H'))
print(ct)
if(ct>=5 and ct<12):
    print("GOOD MORNING")

elif(ct>=12 and ct<18):
    print("GOOD AfterNoon")

elif(ct==18):
    print("GOOD EVENING")

else:
    print("GOOD NIGHT")

    
