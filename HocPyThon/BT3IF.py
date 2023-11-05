#1
'''
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
so3 = int(input("Nhập số thứ ba: "))
so4 = int(input("Nhập số thứ tư: "))

max = so1
min = so1
# Giả sử số đầu tiên là số lớn nhất và nhỏ nhất
if so2 > max:
    max = so2
if so3 > max:
    max = so3
if so4 > max:
    max = so4

if so2 < min:
    min = so2
if so3 < min:
    min = so3
if so4 < min:
    min = so4

print("Số lớn nhất:", max)
print("Số nhỏ nhất:", min)
'''
#2
'''
x = int(input("Nhập x: "))

if x >= 0:
    giatrituyetdoi = x
else:
    giatrituyetdoi = -x

print("|", x, "| =", giatrituyetdoi)
'''
#3
'''
loai_xe = int(input("Nhập vào loại xe (chỉ nhập 4 hoặc 7): "))
so_km = float(input("Nhập số km di chuyển: "))
thoi_gian_cho = int(input("Nhập thời gian chờ (làm tròn theo phút): "))

tien_cho = (thoi_gian_cho - 5) * 750  # tính tiền chờ

if loai_xe == 4:
    if so_km <= 0.8:
        tien_di_chuyen = 11000
    elif so_km <= 30:
        tien_di_chuyen = so_km * 15300
    else:
        tien_di_chuyen = 30 * 15300 + (so_km - 30) * 12100
elif loai_xe == 7:
    if so_km <= 0.8:
        tien_di_chuyen = 12000
    elif so_km <= 30:
        tien_di_chuyen = so_km * 16100
    else:
        tien_di_chuyen = 30 * 16100 + (so_km - 30) * 13800
else:
    print("Loại xe không hợp lệ!")

tien_cuoc = tien_di_chuyen + tien_cho  # tính tổng tiền cước

print("Tiền chờ =", tien_cho)
print("Tiền di chuyển:", tien_di_chuyen)
print("Tiền cước = ", str(tien_di_chuyen), " + " ,str(tien_cho), " = ", str(tien_cuoc))
'''

#4
'''
so_kwh_tieu_thu = int(input("Nhập số kWh tiêu thụ: "))

if so_kwh_tieu_thu <= 50:
    tien_dien = so_kwh_tieu_thu * 1.484
elif so_kwh_tieu_thu <= 100:
    tien_dien = 50 * 1.484 + (so_kwh_tieu_thu - 50) * 1.533
elif so_kwh_tieu_thu <= 200:
    tien_dien = 50 * 1.484 + 50 * 1.533 + (so_kwh_tieu_thu - 100) * 1.786
elif so_kwh_tieu_thu <= 300:
    tien_dien = 50 * 1.484 + 50 * 1.533 + 100 * 1.786 + (so_kwh_tieu_thu - 200) * 2.242
elif so_kwh_tieu_thu <= 400:
    tien_dien = 50 * 1.484 + 50 * 1.533 + 100 * 1.786 + 100 * 2.242 + (so_kwh_tieu_thu - 300) * 2.503
else:
    tien_dien = 50 * 1.484 + 50 * 1.533 + 100 * 1.786 + 100 * 2.242 + 100 * 2.503 + (so_kwh_tieu_thu - 400) * 2.587

print("Tiền điện phải trả =", tien_dien, "đồng")
'''
#5

loai_phong = int(input("Nhập loại phòng (từ 1 đến 8): "))
sodem = int(input("Nhập số đêm: "))

gia_phong = 0

if loai_phong == 1:
    gia_phong = 1260000
elif loai_phong == 2:
    gia_phong = 1550000
elif loai_phong == 3:
    gia_phong = 1830000
elif loai_phong == 4:
    gia_phong = 1830000
elif loai_phong == 5:
    gia_phong = 2120000
elif loai_phong == 6:
    gia_phong = 2120000
elif loai_phong == 7:
    gia_phong = 2540000
elif loai_phong == 8:
    gia_phong = 480000
else:
    print("Loại phòng không hợp lệ!")

if sodem >= 4:
    gia_phong = gia_phong * 0.7
elif sodem >= 2:
    gia_phong = gia_phong * 0.75

thanh_tien = gia_phong * sodem

print("Thành tiền =", thanh_tien, "VNĐ")

