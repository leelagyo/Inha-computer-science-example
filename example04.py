a= 95

b= 70

c= 80

d= 60

A_sum =a+b

B_sum =c+d

A_average=A_sum/2

B_average=B_sum/2

print("a학생의 성적 합은 : %d"%( A_sum))

print("b학생의 성적 합은 : %d" % (B_sum))

print("a학생의 성적 평균은 : %0.1f" %(A_average))

print("b학생의 성적 평균은 : %0.1f" %(B_average))

print("----------------------------------------------------------------------")

print(":               :     a     :     b      :     sum     :    average  :")

print("----------------------------------------------------------------------")

print(": English       :    %d     :     %d     :     %d      :      %0.1f     :" %(a, b, A_sum, A_average))

print("----------------------------------------------------------------------")

print(": Mathematics   :    %d     :     %d     :     %d      :      %0.1f     :" %(c, d, B_sum, B_average))

print("----------------------------------------------------------------------")

#%d는 정수, #%f는 실수 표현 / %0.1f - 소수점 한자리만 표시하기 위해 f앞에 0.1 표시
