
name = "itheima is a brand of black horse"

count = 0
for x in name:
    if x == "a":
        count += 1

print(f"itheima is a brand of black horse 中一共有 {count} 个 'a'")


count = 0
for x in range(1, 100):
    if x % 2 == 0:
        count += 1
print(f"range(1, 100) 从1到100不包含100，一共有 {count} 个偶数")

i = 0
for i in range(5):
    print(i)
print(i)



