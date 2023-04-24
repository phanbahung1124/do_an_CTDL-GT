# Lấy input từ bàn phím
lst = list(map(int, input("Nhập một dãy số nguyên, cách nhau bằng khoảng trắng: ").split()))

# Sắp xếp dãy số theo thứ tự tăng dần
n = len(lst)
for i in range(n):
    for j in range(n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

# In ra kết quả
print("Dãy số được sắp xếp theo thứ tự tăng dần là:")
print(lst)

