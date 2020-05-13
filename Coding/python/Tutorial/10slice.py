array = [1,2,3,4,5]
print(array[0:2]) #取[0][1]
print(array[0:5:2]) #间隔2
print(array[::2]) #间隔2
#列表生成式
array = [x*x for x in range(1,10) if x%2 == 0]
print(array)