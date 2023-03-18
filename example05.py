string = ' 1,2 , 3 , 4,5'
print(string.replace(' ', ''))
#replace(바뀌게 될 문자열, 바꿀 문자열)을 이용하여 공백이 있는 문자열을 공백이 없는 문자열로 치환
a=string.replace(' ','')
b=a.split(",")
print(b)



