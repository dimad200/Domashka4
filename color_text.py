
print("\u001b[0;35m dfdsfs")
print("aaa")
print("\u001b[0m dfdsfs")
k=0
for i in range(255):
    k = 0 if k >6 else k+1
    if k==0:
        print(" ")
    print(f"\u001b[38;2;{i};{130};{i}m {"******"}", end="")
