n = int(input("Cuantos numeros de fibonaci quieres ver? "))
c = 0
f1 = 0
f2 = 1

while c!=n:
	if n==1:
		pass
	else:
		if f1<=f2:
			print(f1)
			f1 = f1+f2
		else:
			if f1>f2:
				print(f2)
				f2 = f1+f2
	c = c+1 
#if f1>f2:
#    print(f2)
#else:
#    print(f1)