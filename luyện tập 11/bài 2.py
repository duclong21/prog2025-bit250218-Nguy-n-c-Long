def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"Tìm ở vị trí {mid}: '{arr[mid]}' (độ dài {len(arr[mid])})")
        if len(arr[mid]) == len(target):
            if arr[mid] == target:
                return mid
            else:
                return -1

        elif len(arr[mid]) > len(target):
            left = mid + 1
        else:
            right = mid - 1

    return -1
#ex
chuoi_list = ["xin chào cả nhà", "mình là đức long", "thảo linh", "trúc", "lượng"]

target = input("\nNhập chuỗi cần tìm: ").strip()

vi_tri = binary_search(chuoi_list, target)

if vi_tri != -1:
    print(f"Tìm thấy '{target}' tại vị trí {vi_tri} (độ dài {len(target)})")
else:
    print("Không tìm thấy chuỗi có cùng độ dài hoặc khớp chính xác.")