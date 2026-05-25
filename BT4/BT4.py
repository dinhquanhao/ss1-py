print("===== HỆ THỐNG NHẬP DẤU HIỆU SINH TỒN =====")

# Nhập thông tin
patient_code = input("Nhập mã bệnh nhân: ").strip()
body_temperature = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate = int(input("Nhập nhịp tim: "))

# Kiểm tra mã bệnh nhân
if not patient_code:
    print("Lỗi: Mã bệnh nhân không được để trống")
    exit()

# Hiển thị thông tin
print("\n===== THÔNG TIN BỆNH NHÂN =====")
print("Mã bệnh nhân :", patient_code)
print("Nhiệt độ     :", body_temperature)
print("Nhịp tim     :", heart_rate)

# Kiểm tra kiểu dữ liệu
print("\n===== KIỂU DỮ LIỆU =====")
print("Kiểu dữ liệu nhiệt độ :", type(body_temperature))
print("Kiểu dữ liệu nhịp tim :", type(heart_rate))