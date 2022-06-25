# re - modulini import qilib olamiz
import re

pat = '[absd]'  # username

email = input("Say hello: ")

if re.match(pat, email):
    print("Hello!")
    print(re.match(pat, email).string)
else:
    print("I don't know you!")
