print('--- Hệ thống nhập chỉ số sinh tồn ---')
name_patient = input('Nhập tên của bệnh nhân: ')
weight = float(input('Nhập cân nặng của bệnh nhân: '))

print('--- Kiểm tra dữ liệu lưu trữ ---')
print('Bệnh nhân: ', name_patient)
print('Cân nặng đã nhập: ', weight, 'Kg')


print('Cảnh báo - kiểu dữ liệu đang lưu là: ', type(weight))

# Nguyên nhân lỗi là do weight nhưng ép kiểu str(weight là float)

