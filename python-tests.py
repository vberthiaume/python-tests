#python automatically concatenates strings
words = "one" "two"
# print (words)

#and you can use "implied line continuation", ie, use parens to automatically
#concatenate multiple lines
lyrics = ("Never gonna give you up, "
           "Never gonna let you down, "
           "Never gonna run around and desert you.")
# print (lyrics)

#operators
print ("regular float division: 5/3 = ", 5/3)
print ("int division division: 5//3 = ", 5//3)
print ("power operator: 2**3 = ", 2**3)
x = 4
print ("you can chain comparison operators: with x = 4, 3 < x < 6 is = ", 3 < x < 6)

#Logical operators !, &&, || in C++ are in plain English in Python (not, and, or).
y = 2
print ("with y = 2, x > 3 and y < 1 = ", x > 3 and y < 1)

#you can swap variables like this
x = "value of x"
y = "value of y"
x, y = y, x
print("x:", x)
print("y:", y)

#slicing: the 3rd index is the step size
meList = [0, 1, 2, 3, 4]
print (meList[0:5:2])

# imma need an actual object here to do this properly. Like call setSomething on it
#variables are just pointers to objects
secondLyricsPointer = lyrics
lyrics = "modified lyrics"  #so here I'm editing the OG object
# print (secondLyricsPointer)
