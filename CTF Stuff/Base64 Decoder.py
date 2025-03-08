import base64

value = "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0FDOEZDRDc1fQ=="

decoded_flag = base64.b64decode(value).decode()

print(decoded_flag)