dic={}

def root():
	name = raw_input('What is your name?\n')
	#print '%s.' % name
	number = int(input("Enter the number please: "))
	dic[name]=number
print dic

while True:
    a = input("Enter yes/no to continue")
    if a=="yes":
        root()
        continue
    elif a=="no":
        choice=input("Enter your choice(name/number):")
		if choice=="name":
		   x=raw_input('Enter the name:\n')
		   for i in dict.keys():
		   	if x=dic[i]:
			   print dic[i]
		   
    else:
        print("Enter either yes/no")

