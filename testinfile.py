from socket import *
from threading import *
import json

# print("Signing up")

# # client_name = client.recv(1024).decode('utf8')
# # client.sendall(client_name.encode('utf8'))

# # client_psw = client.recv(1024).decode('utf8')
# # client.sendall(client_psw.encode('utf8'))

# f = open('accounts.json', 'r+')
# file_data = json.load(f)
# user = input("tên đăng nhập")
# passed = input("pass")
# for i in file_data['username']:
#     if i == user:
#         print('Username existed')
#         f.close()
#         break

#                 # Append new user's account to database
# file_data['username'].append(user)
# file_data['password'].append(passed)

# temp = "luutru\\" + user + ".json"
# file_data['fileluutru'].append(temp)

# # f.seek(0)
# json.dump(file_data, f, indent=4)

# print("Create account successfully")
# f.close()

# print(user)
# print(passed)
# print()
# print("login")
user = input("tên đăng nhập")
passed = input("pass")
# self.name = self.user.get()
# self.psw = self.pswd.get()
if user == 'Username' or passed == 'Password':
    print("Fields can't be empty")


# Open and store data as a python object
fi = open('accounts.json', 'r')
file_data_in = json.load(fi)
fi.close()

j = 0
for i in file_data_in['username']:
    if i == user:
        if file_data_in['password'][j] == passed:
            print("Login succesfully")
            break
        print("Wrong password")
        break
    j += 1

tenfile = file_data_in['fileluutru'][j]
fil = open(tenfile,'r')
file_data_out = json.load(fil)
fil.close()
for i in file_data_out['text']:
    print(i)


print("Username doesn't exist")