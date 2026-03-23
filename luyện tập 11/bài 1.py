def insertion_sort_by_length(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"Bước {i}: Chèn '{key}' (độ dài {len(key)}) vào danh sách: {arr[:i]}")

        while j >= 0 and len(arr[j]) < len(key):
            arr[j + 1] = arr[j]
            j -= 1
            # In trạng thái dịch chuyển
            print(f"   → Dịch chuyển: {arr}")

        arr[j + 1] = key

        print(f"Sau bước {i}: {arr}\n")

# Nhập 5 chuỗi
print("Nhập 5 chuỗi bất kỳ:")
chuoi_list = []
for i in range(5):
    s = input(f"Chuỗi {i + 1}: ").strip()
    chuoi_list.append(s)

print("\nDanh sách ban đầu:", chuoi_list)
print("\nQuá trình sắp xếp theo độ dài giảm dần:\n")

insertion_sort_by_length(chuoi_list)

print("Kết quả cuối cùng:", chuoi_list)