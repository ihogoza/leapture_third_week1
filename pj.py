import jwt

# JSON Web Token (JWT)
encoded = jwt.encode({"some": "payload"}, "don't tell", algorithm="HS256")
print(encoded)
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U
decode = jwt.decode(encoded, "don't tell", algorithms=["HS256"])
print(decode)
# {'some': 'payload'}