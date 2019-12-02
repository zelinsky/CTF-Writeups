import jwt
public = open('signing.pem', 'r').read()
print public
print jwt.encode({"user":"admin", "type":"admin"}, key=public, algorithm='HS256')
