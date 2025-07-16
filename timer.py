import time
inp=int(input("Enter the time in seconds: "))
# print("nothing to do just waste time ekdm ")
for sc in range(inp,0,-1):
    seconds=sc%60
    minites=int(sc/60)%60
    hours=int(sc/3600)
    print(f"{hours:02}:{minites:02}:{seconds:02}")
    time.sleep(1)
    
print("Time's Up !!!")
