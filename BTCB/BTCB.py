import random

patient_name = input("Nhap ten cua ban: ")
patient_sex = input("Nhap gioi tinh cua ban: ")
patient_birthday = int(input("Nhap nam sinh cua ban: "))
patient_phone = input("Nhap so dien thoai cua ban: ")
patient_email = input("Nhap email cua ban: ")
patient_sick = input("Nhap trieu chung cua ban: ")
symptom = float(input("Nhap chi phi cua ban: "))

random_number = random.randint(100, 999)

patient_id = "BN" + str(patient_birthday) + str(random_number)

print("--- Thẻ bệnh nhân ---")
print("Mã BN:", patient_id)
print("Tên:", patient_name)
print("Giới tính:", patient_sex)
print("Năm sinh:", patient_birthday)
print("Số điện thoại:", patient_phone)
print("Email:", patient_email)
print("Triệu chứng:", patient_sick)
print("Chi phí:", symptom, "VNĐ")