from passlib.hash import bcrypt

password = "Admin123"

hashed_password = bcrypt.hash(password)

print("Hashed Password:")
print(hashed_password)

print("\nTesting Correct Password Result:")
print(bcrypt.verify("Admin123", hashed_password))

print("\nTesting Wrong Password Result:")
print(bcrypt.verify("Admin", hashed_password))