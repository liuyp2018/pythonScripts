#不使用递归
def binarysearch(num,list):
    l=len(list)
    left=0
    right=l-1
    while left<=right:
        mid=left+(right-left)//2
        if num>list[mid]:
            left=mid+1
        elif num<list[mid]:
            right=mid-1
        else:
            return True
    return False

#使用递归
def binarysearch1(num,list):
    l=len(list)
    mid=int(l/2)
    if len(list)>1:
        if num==list[mid]:
            return True
        elif num>list[mid]:
           return binarysearch1(num,list[mid+1:]) #递归调用函数的时候，前面需加return 否则会导致返回结果为None的情况
        elif num<list[mid]:
            return binarysearch1(num,list[:mid])
    else:
        if num==list[0]:
            return True
        else:
            return False

list=[1,3,4,5,8,10,11]
r1=binarysearch(5,list)
r2=binarysearch1(6,list)

print(r1)
print(r2)