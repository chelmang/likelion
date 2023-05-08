#반복문(loops)

i =0
text = ""
sum = 0

for i in range(1, 101):
    print(i)
    
for i in range(1, 101):
    sum = sum +1
    
print(sum)

#while True:
#   print("while loop")


progress = 0 

while progress < 100:
    progress = progress + 1
    print(f"{progress}% completed")  