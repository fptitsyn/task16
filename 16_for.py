#F(n) = 1, при n < 2,
#F(n) = F(n/2) + 1, когда n ≥ 2 и чётное,
#F(n) = F(n - 3) + 3, когда n ≥ 2 и нечётное.

a = [1, 1]

for i in range(2, 100000):
    a.append(a[i // 2] + 1) if i % 2 == 0 else a.append(a[i - 3] + 3)

print(a)

for i in range(len(a)):
    if a[i] == 31:
        print(i)
        break
