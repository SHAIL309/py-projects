import random
import array
alpha_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha_upper	= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symboles = ['!','@','£','$','%','&','*','(',')']
numerics = ['1','2','3','4','5','6','7','8','9']
password_length = int(input("how long the password should be?: "))

combined = alpha_lower + alpha_upper + numerics + symboles 

# digits = random.numerics()
# alphas_lower = random.alpha_lower()
# alphas_upper = random.alpha_upper()
# symbol = random.symboles()

# temp_password = digits + alphas_lower + alphas_upper + symbol
while password_length:
	password = combined + random.choice(combined)
# password = 
print(password)	 gate

