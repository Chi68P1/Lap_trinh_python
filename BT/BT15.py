#xây dựng hàm Arange()
#hàm trả về danh sách theo thứ tự từ lớn đến bé, chẵn đứng trước , lẻ đứng sau

############################################
def Xap_Xep_Lon_Be(A):
	M = []
	a = 0
	while len(A) !=0:
		a = max(A)
		M.append(a)
		A.remove(a)
	return M

def Arange(A):
	M = []
	N = []
	K = Xap_Xep_Lon_Be(A)

	for i in K:
		if i%2 ==0:
			M.append(i)
		else:
			N.append(i)	

	return M+N
##############################################
#VD
B = [1,6,2,7,1,9,4]
print(Arange(B))

C = [2,8,5,3,7,5,9,4]
print(Arange(C))