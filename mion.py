s='BANANA'
count1=0
count2=0
vovel='AEIOU'
for i in s:
    if i in vovel:
        count1=count1+2
    else:
            count2 =count2+1
print(count1)
print(count2)