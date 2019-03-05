o = """
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
# door mat
input = input().split(" ")
i = input[0]
j = input[1]

for x in range(int(int(i) / 2)):
    a = "|.." * x
    b = "..|" * x
    str = "." + a + "|" + b + "."
    print(str.center(int(j), "-"))
print("WELCOME".center(int(j), "-"))
for x in reversed(range(int(int(i) / 2))):
    a = "|.." * x
    b = "..|" * x
    str = "." + a + "|" + b + "."
    print(str.center(int(j), "-"))
