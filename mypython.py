def main(lst):
    sub_lst=[[]]
    count=0
    for i in range(len(lst)+1):
        for j in range(i+1,len(lst)+1):
            sub=lst[i:j]
            count=count+i
            sub_lst.append(sub)
    print(count)
    return sub_lst    
lst=[1,2,3,4,5]
print(main(lst))


#palindrome of string
num=[1,2,4,5,6,7]
for i in range(0,num):
    a=list(map(int,input("Enter a num").strip().split(" ")))[:num]
print(a)
    

    









