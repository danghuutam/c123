# Nhập module xml.dom.minidom
import xml.dom.minidom

# Tải file sample.xml vào một đối tượng DOM
doc = xml.dom.minidom.parse("sample.xml")

# Lấy danh sách các phần tử có tên thẻ là staff
staff_list = doc.getElementsByTagName("staff")

# Duyệt qua danh sách các phần tử
for staff in staff_list:
    # In ra tên thẻ của mỗi phần tử
    print(staff.tagName)
