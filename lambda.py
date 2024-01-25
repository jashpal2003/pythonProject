#add example lambda
a = lambda x,y:x+y
print(a(3,4))
#sqare
sq = lambda a:a**2
print(sq(4))
#maximum
mx = lambda x,y:x if x>y else y
print(mx(8,9))

str_with = lambda stri ,letter : stri.startswith(letter)
print(str_with("jashpal","j"))

last_word = lambda sentence: sentence.split()[-1]
print(last_word("This is a sample sentence"))  