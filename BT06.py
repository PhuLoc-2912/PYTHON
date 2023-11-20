
import math

# Sử dụng Lambda để tính diện tích và chu vi hình tròn
tinh_chu_vi_hinh_tron = lambda r: 2 * math.pi * r
tinh_dien_tich_hinh_tron = lambda r: math.pi * r*r

# Sử dụng Lambda để tính diện tích và chu vi hình chữ nhật
tinh_chu_vi_hcn = lambda a, b: 2 * (a + b)
tinh_dien_tich_hcn = lambda a, b: a * b


# Nhập giá trị từ người dùng và tính toán
chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))

print("Diện tích hình chữ nhật:", tinh_dien_tich_hcn(chieu_dai, chieu_rong))
print("Chu vi hình chữ nhật:", tinh_chu_vi_hcn(chieu_dai, chieu_rong))

ban_kinh = float(input("Nhập bán kính: "))
print("Diện tích hình tròn:", tinh_dien_tich_hinh_tron(ban_kinh))
print("Chu vi hình tròn:", tinh_chu_vi_hinh_tron(ban_kinh))


