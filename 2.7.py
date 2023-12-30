# Nhập module json
import json

# Tạo một đối tượng Python mẫu
python_object = {
    "name": "Nguyen Van A",
    "age": 25,
    "skills": ["Python", "Database", "Web"],
    "married": False,
    "salary": None
}

# Chuyển đổi đối tượng Python thành chuỗi JSON
json_string = json.dumps(python_object)

# In ra chuỗi JSON
print(json_string)
