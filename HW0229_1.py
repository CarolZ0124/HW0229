def count_vowels(word):
    vowels=['a','e','i','o','u']
    i=len(word)
    number=0
    while i>0:
        if word[i-1] in vowels:
          number+=1
        i-=1
    return number
print(count_vowels('Carol'))
