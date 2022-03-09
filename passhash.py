from passlib.hash import pbkdf2_sha256

# generate new salt, and hash a password
hash = pbkdf2_sha256.hash("toomanysecrets")
print(hash)
# '$pbkdf2-sha256$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk'

# verifying the password
print(pbkdf2_sha256.verify("toomanysecrets", hash))
# True
print(pbkdf2_sha256.verify("joshua", hash))
# Fa