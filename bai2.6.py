# Nhập module json
import json

# Tạo một chuỗi JSON mẫu
json_string = """
{
    "name": "Nguyen Van A",
    "age": 25,
    "skills": ["Python", "Java", "C++"],
    "married": false,
    "salary": null
}
"""

# Chuyển đổi chuỗi JSON thành đối tượng Python
data = json.loads(json_string)

# In ra kiểu dữ liệu và giá trị của đối tượng Python
print(type(data))
print(data)

# Truy cập và thao tác với đối tượng Python
print(data["name"]) # In ra tên
data["age"] += 1 # Tăng tuổi lên 1
print(data["age"]) # In ra tuổi mới
data["skills"].append("SQL") # Thêm kỹ năng mới
print(data["skills"]) # In ra danh sách kỹ năng
