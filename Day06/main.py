print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "pruthvi" and password == "password":
 print("Welcome Pruthvi!")
elif username == "pruthvi" and password == "1234":
 print("Hey there Pruthvi!")
else:
 print("Go away!")

# Output:
# SECURE LOGIN
# Username > pruthvi
# Password> 1234
# Hey there Pruthvi!