import hashlib
print("\nHey...Welcome to the fastest md5 cracker\n")
hashcode=input("\nEnter the md5 hash code to crack : ")
file1=input("\nEnter the wordlist file location : ")
print("\nPlease wait.......\n")
with open(file1) as data:
    for line in data:
            line=line[:-1]
            str1 = hashlib.md5(line.encode())
            if(hashcode == str1.hexdigest()):
                print("Hurray...Password found = ",line)
                print("\nThanks for using my Program..Hope you liked it...@luk0y\n")
                break
if(hashcode != str1.hexdigest()):
    print("Password not found...Try another wordlist...\nThanks for using my Program...@luk0y\n")
