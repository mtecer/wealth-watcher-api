import bcrypt

# password = "secret"
# byte_password = password.encode('utf-8')

# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(byte_password, salt)
# hashed = bcrypt.hashpw(byte_password, bcrypt.gensalt(12))

# print(salt, hashed)
# print(hashed)

def get_hashed_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

hashed = get_hashed_password("MyPassword")
print(hashed)
print(verify_password("MyPassword",'$2b$12$4TI1zgFIvNNliYMD/aeuN.xukfMusppP3R4gMjwoeAJn2cridUwXG'))
