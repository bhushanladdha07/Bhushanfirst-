import numpy as np 
arr1=np.array([1,2,3])
arr2=np.array([6])
arr_2d=np.array([[7,8,9],[2,3,4]])

print("1D ARRAY OPERATIONS : ")
add=arr1+arr2
print(add)

sub=arr2-arr1
print(sub)

mul=arr1*arr2
print(mul)

div=arr2/arr1
print(div)

res=arr1.reshape(3,1)
print(res)

arr3=np.append(arr1,arr2)
print(arr3)

sli=arr1[1:]
print(sli)

stack_vertical=np.vstack(arr1)
print(stack_vertical)

square_root=np.sqrt(arr1)
print(square_root)

print("2D ARRAY OPERATIONS : ")
print(arr_2d)

tra=np.transpose(arr_2d)
print(tra)

con=np.concatenate(arr_2d)
print(con)

