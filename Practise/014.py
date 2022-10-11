def arrneg(arr,n):
  j=0
  for i in range(0,n):
    if(arr[i]<0):
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp
      j=j+1
  print(arr)

arr=[-5,8,7,-2,10,12]
n=len(arr)
arrneg(arr,n)


