
#while True:
# user_input = int(input("please enter a number: "))

# def cube(num):
	# result = num**3
	# return result

# cube = cube(user_input)
# print(user_input,"^3 =",cube)



n_input = int(input("please enter the value of n: "))
r_input = int(input("please enter the value of r: "))

def factorial(num):
	fac = 1
	for i in range(num,1,-1):
		fac = fac*i
	return(fac)

def combination(n,r):
	n_fac = factorial(n)
	r_fac = factorial(r)
	n_r_fac = factorial(n-r)
	result = n_fac/(r_fac*n_r_fac)
	return result

combination = combination(n_input,r_input)
print("C(n,r) =",int(combination))


