#more simple and common way
M = 21
N = 7
flick = "-"
special = ".|."

# solvation
for i in range(1, N, 2):
    print((special * i).center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N - 2, 0, - 2):
    print((special * i).center(M, "-"))

# advanced solvation
#s = [(special * i).center(M, "-") for i in range(1, N, 2)]
#print("\n".join(s + ["WELCOME".center(M, "-")] + list(reversed(s))))