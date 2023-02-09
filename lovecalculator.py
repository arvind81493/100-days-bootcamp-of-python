print("welcome to the love calculator")
name1=input("what is your name\n ")
name2=input("what is their name \n")
com=name1 +name2
lowerstring=com.lower()
t=lowerstring.count("t")
r=lowerstring.count("r")
u=lowerstring.count("u")
e=lowerstring.count("e")
true=t+r+r+u+e
l=lowerstring.count("l")
o=lowerstring.count("o")
v=lowerstring.count("v")
e=lowerstring.count("e")
love=l+o+v+e
love_score=str(true)+str(love)
print(f"your love score is {love_score}")
