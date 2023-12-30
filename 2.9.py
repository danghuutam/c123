# Nhập module json
import json

# Mở tệp JSON chứa thông tin về công ty và nhân viên
with open("company.json", "r") as f:
    # Chuyển đổi nội dung tệp thành một đối tượng Python
    data = json.load(f)

# Lấy thông tin về tên công ty, địa chỉ và tổng số nhân viên
company_name = data["name"]
company_address = data["address"]
total_employees = data["total_employees"]

# In ra thông tin về công ty
print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {company_address}")
print(f"Tổng số nhân viên: {total_employees}")

# Lấy danh sách các đ