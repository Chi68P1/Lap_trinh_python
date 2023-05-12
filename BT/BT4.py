#nhập vào 1 số nguyên a
#in ra màn hình các số nguyên tố nằm trong đoạn [0,a]


#hàm kiểm tra số nguyên tố
def so_nguyen_to(n):
    #flag = 0 => không phải số nguyên tố
    #flag = 1 => số nguyên tố
    flag = 1;
    if (n <2):
        flag = 0
        return flag  
    
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break #Chỉ cần tìm thấy 1 ước số là đủ và thoát vòng lặp
    return flag


#input chỉ chấp nhận số nguyên
while True:
    try:
        a = int(input("\nNhập 1 số nguyên a: ")) 
        break
    except:
        print("Nhập lại!")

#tìm số nguyên tố trong đoạn [0,a]

print("Các số nguyên tố trong đoạn [0,{}]:".format(a))
for i in range(0,a+1):
    if so_nguyen_to(i) == 1:
        print(i,end =" ")
