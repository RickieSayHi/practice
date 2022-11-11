count = 0
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}\t", end="")
        count += 1
    print()
print(f"一共循环了 {count} 次")