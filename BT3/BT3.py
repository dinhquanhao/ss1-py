print("===== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN =====")

# Nhập thông tin bệnh nhân
full_name = input("Nhập họ và tên bệnh nhân: ").strip()
medical_code = input("Nhập mã bệnh án: ").strip()
department = input("Nhập khoa/phòng khám chỉ định: ").strip()

# Kiểm tra dữ liệu trống
if not full_name or not medical_code or not department:
    print("\nLỗi: Không được để trống thông tin.")
    exit()

# Hiển thị phiếu khám bệnh điện tử
print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")
print("Xác nhận tiếp nhận bệnh nhân thành công.\n")

print("Họ và tên bệnh nhân :", full_name)
print("Mã bệnh án          :", medical_code)
print("Khoa/Phòng khám     :", department)

print("\nVui lòng chờ tới lượt khám.")
print("===================================")