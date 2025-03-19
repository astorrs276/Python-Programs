import base64

values = ["cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0FDOEZDRDc1fQ==", # picoCTF - Cookie Monster Secret Recipe
            "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMTBmOTM3NmZ9", # picoCTF - WebDecode
            "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg==", # picoCTF - interencdec
            "cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==", # picoCTF - CanYouSee
            "VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVhRmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNkMlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVWVkpEVGxaYVdFMVhSbFZrTTBKVVZXMTRWMDVHV2toalJYUlhDazFyV25sVVZXaHpWakpHZEdWRlZsaGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==", # picoCTF - repetitions
            "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9", # picoCTF - information
            "cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV83NzVhYzEyZH0=", # picoCTF - SansAlpha
            ]

value = values[-1]

count = 1
decoded_flag = base64.b64decode(value).decode()

'''
All flag formats:
picoCTF
THM
RS
'''
flag_format = "picoCTF"

while (decoded_flag[0:len(flag_format) + 1] != flag_format + "{" and decoded_flag[-1] != "}"):
    count += 1
    decoded_flag = base64.b64decode(decoded_flag).decode()

print(count, ":", sep="")
print(decoded_flag)