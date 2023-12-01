def checkx(x):
    if (x%2==0 or x%5==0):
        print("The x must not divisible by 2 and not divisible by 5 ")

def duplicates(num, a):
    num=str(num)
    num_dup = ''
    for k in range(a):
        num_dup+=num
    num_dup = int(num_dup)
    return num_dup

def beautiful_number(x):
    numlist=[1,2,3,4,5,6,7,8,9]
    resultss=0
    loop_amount=0   
    list_iterate_amount=0   #how many times the list has been iterated, ex: 1,2,3,... -> list_iterate_amount=1 and 11,22,... -> list_iterate_amount=2

    while(resultss==0):
        num_from_numlist = loop_amount % 9      #num_from_numlist is the index number from numlist 
        if(num_from_numlist % 9 == 0):          #the biggest index number is 8, so when the index is 0 then it will have a modulo of 0. This means that the list has iterate once more
            list_iterate_amount+=1          
        number_used = duplicates(numlist[num_from_numlist],list_iterate_amount)     #duplicate number based on the list_iterate_amount
        if(number_used % x == 0):
            resultss = number_used
            break
        loop_amount+=1
        
    return resultss

        
x=int(input("Input x: "))
checkx(x)

resultt = beautiful_number(x)
print(f'The smallest beautiful number divisible by {x} is {resultt}.')

