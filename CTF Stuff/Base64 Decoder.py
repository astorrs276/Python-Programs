import base64

values = ["cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0FDOEZDRDc1fQ==", # picoCTF - Cookie Monster Secret Recipe
            "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMTBmOTM3NmZ9", # picoCTF - WebDecode
            "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg==", # picoCTF - interencdec p1
            "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ==", # picoCTF - interencdec p2
            ]

value = values[-1]

decoded_flag = base64.b64decode(value).decode()

print(decoded_flag)