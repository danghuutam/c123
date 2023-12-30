# Nhập module xml.dom.minidom
import xml.dom.minidom

# Tải file sample.xml vào một đối tượng DOM
doc = xml.dom.minidom.parse("sample.xml")

# Lấy phần tử gốc của tài liệu
root = doc.documentElement

# Lấy tên của công ty
company_name = root.getElementsByTagName("name")[0].firstChild.data
print(f"Tên công ty: {company_name}")

# Lấy danh sách các nhân viên
staff_list = root.getElementsByTagName("staff")

# Duyệt qua danh sách các nhân viên
for staff in staff_list:
    # Lấy id, tên và lương của mỗi nhân viên
    staff_id = staff.getAttribute("id")
    staff_name = staff.getElementsByTagName("name")[0].firstChild.data
    staff_salary = staff.getElementsByTagName("salary")[0].firstChild.data
    # In thông tin của mỗi nhân viên
    print(f"Nhân viên {staff_id}:")
    print(f"- Tên: {staff_name}")
    print(f"- Lương: {staff_salary}")
