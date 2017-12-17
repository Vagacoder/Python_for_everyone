## Ch1 R2.7
s = 'Hello'
t = 'World'

print(len(s)+ len(t)) #5+5 = 10
print(s[1] + s[2])  #el
print(s[len(s)//2]) #l
print(s + t) # HelloWorld
print(t + s) # WorldHello
print(s*2) #HelloHello

## Ch1 P2.15
#method 1
a= '+'+'--+'*3
b= '|'+'  |'*3

print(a)
print(b)
print(a)
print(b)
print(a)
print(b)
print(a)
#method 2
c = '+'+'--+'*3+'\n'+'|'+'  |'*3+'\n'
print(c*3+a)

## Ch1 P2.22
text = input()
print(text[0] + text[1] + text[2] + '.'*3 + \
      text[len(text)-3]+text[len(text)-2]+text[len(text)-1])
