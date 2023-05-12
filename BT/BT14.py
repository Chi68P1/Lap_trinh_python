#nhập n
#in ra n số của dãy fibonacci

n = ""

while n.isdigit() ==0:  #chỉ nhận giá trị nguyên dương hoăc bằng 0

    n = input("Nhập 1 số nguyên dương: ")  #input

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
 
print("{} số đầu tiên của dãy số fibonacci:\n ".format(n))

fb = Fibonacci(int(n))
print(fb)