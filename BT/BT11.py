#nhập 1 số nguyên x, nhập sai yêu cầu nhập lại
#tạo 1 list có x giá trị, các giá trị là dãy fibonacci và in kq
#in ra màn hình các số nguyên tố trong list trên


#tạo hàm kiểm tra số nguyên tố
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

#tạo hàm fibonacci
def Fibonacci(a):
    a0 = 0
    a1 = 1
    F = []
    while a >0:
        F.append(a0)
        v = a0
        a0 = a1
        a1 = v +a0
        a = a -1
    return F

###############################################
x = ""

while x.isdigit() ==0:  #chỉ nhận giá trị nguyên dương hoăc bằng 0

    x = input("Nhập 1 số nguyên dương: ")  #input

print("{} số đầu tiên của dãy số fibonacci:\n ".format(x))
fb = Fibonacci(int(x))
print(fb) #output

nt =[]
for i in fb:
    if so_nguyen_to(i) == 1:
        nt.append(i)
       
print("Các số nguyên tố trong dãy Fibonacci trên:\n")
print(nt) #output

