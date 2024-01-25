numbers =  [1,2,3,4,5,6,78,9]
even_number = list(filter(lambda x:x%2==0,numbers))
print(even_number)

#filter lonnger than 5
words= ["jashpal" , "hero","ironman"]
long_word= list(filter(lambda x:len(x)>5,words))
print(long_word)