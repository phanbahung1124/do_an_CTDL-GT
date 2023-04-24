# Lấy input từ bàn phím
lst = list(map(int, input("Nhập một dãy số nguyên, cách nhau bằng khoảng trắng: ").split()))

# Tạo dictionary để lưu trữ số lần xuất hiện của mỗi số
freq = {}

# Tính số lần xuất hiện của từng số
for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# In ra kết quả
print("Số lần xuất hiện của từng số trong dãy số là:")
for key, value in freq.items():
    print(f"({key},{value})", end=" ")
