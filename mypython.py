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
print(lst)
print("\n")
print("It's subet...")
print("\n")
print("\n")
print(main(lst))

    

    









