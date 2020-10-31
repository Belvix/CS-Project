d = {"Makudonarudo":"McDiaMaids","Dominicos":"ImBored"}

while True:
	A = input("Enter Username:")
	if A in d:
		break
	print("Incorect Usrname. Try again.")
if A in d:
	while(input("Enter Password:") != d[A]):
		print("Incorect password. Try again.")
print("Welcome Manager")
	

