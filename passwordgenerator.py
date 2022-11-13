import secrets

pw = ""
zeichen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!§$%&/())=`*#_"
länge = int(input("Bitte gebe die Passwortlänge ein:"))

for _ in range(länge):
    pw = pw+secrets.choice(zeichen)

print(pw)
