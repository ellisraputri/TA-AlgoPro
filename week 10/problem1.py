def stringOfWord2(word2, j):
    stringWord2=''
    for kk in range(j):
        stringWord2 += word2[kk] 
    return stringWord2

def stringOfWord1(word1, j):
    stringWord1 =''
    for k in range(1, j+1):
        stringWord1 = word1[-k]+stringWord1
    return stringWord1

def checkWord(word1, word2, length1, length2):
    if length1<length2:
       shortest_length=length1
    else:
        shortest_length=length2

    amount_of_same_letter=0
    a=0
    for j in range(0, shortest_length+1):
        stringword2=stringOfWord2(word2, j)
        stringword1=stringOfWord1(word1, j)

        if(stringword1 == stringword2):
            amount_of_same_letter=a
        a+=1
    
    same_words=[]
    for k in range(amount_of_same_letter):
        same_words.append(word2[k])

    return same_words


length1=int(input("Length of the first word: "))
word1=input("First word: ")
length2=int(input('Length of the second word: '))
word2=input("Second word: ")

word1=list(word1)
word2=list(word2)

wordlink=checkWord(word1,word2,length1,length2)
result=''

if wordlink == []:
    print('Both words cannot be linked.')
else:
    for letter in wordlink:
        result += letter
    print(f"Both words can be linked with the subword '{result}'.")
