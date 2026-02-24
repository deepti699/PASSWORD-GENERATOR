print("WELOCME TO THE PASSWORD  GENERATOR :")

letters = int(input("how many letters would you like to have"))

symbols = int(input("how many symbols would you like to have"))

numbers = int(input("how many numbers would you like to have"))

lett = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symb = ['!','@','#','$','%','^','&','*','(',')']

numb = ['1','2','3','4','5','6','7','8','9']

password_list = " "

for char in range (0,letters):

  password_list.append(random.choice(lett))

for char in range (0,symbols):

  password_list.append(random.choice(symb))

for char in range (0,numbers):

  password_list.append(random.choice(numb))

for char in password_list:

  password += char

print(f"your password is : {password}")
