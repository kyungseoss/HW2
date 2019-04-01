
words = str(input("단어를 입력하세요: "))
length = len(words)
while(length>0): 
    length = length - 1
    print(words[length], end="")
print()