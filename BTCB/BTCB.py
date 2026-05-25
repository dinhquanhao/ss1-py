patient_name = input("Nhap ten cua ban: ")
patient_sex = input("Nhap gioi tinh cua ban: ")
patient_birthday = input("Nhap nam sinh cua ban: ")
patient_phone = input("Nhap so dien thoai cua ban: ")
patient_email = input("Nhap email cua ban: ")
patient_sick = input("Nhap trieu chung cua ban: ")
symptom = input("Nhap chi phi cua ban: ")

patient_birthday = int(patient_birthday)
symptom = float(symptom)


print("--- Thẻ bệnh nhân ---")
print("Mã BN: BN001")
print("Tên:", patient_name)
print("Giới tính:", patient_sex)
print("Nam sinh:", patient_birthday)
print("Số điện thoại:", patient_phone)
print("Email:", patient_email)
print("Triệu chứng:", patient_sick)
print("Chi phí:",symptom,"VNĐ")



