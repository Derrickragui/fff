import os
'''
r: read
a: append
w: write
x:create
'''


if os.path.exists("C:\Users\Student\Desktop\gt"):
    os.rmdir("C:\Users\Student\Desktop\gt")
    print("File deleted")

else:
    print("file does not exist")