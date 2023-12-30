# Nhập module json
import json

# Tạo một đối tượng từ điển Python mẫu
python_dict = {"name": "Nguyen Van A", "age": 25, "skills": ["Python", "Java", "C++"]}

# Chuyển đổi đối tượng từ điển Python thành chuỗi JSON, sắp xếp theo khóa và thụt lề 4
json_string = json.dumps(python_dict, sort_keys=True, indent=4)

# In ra chuỗi JSON
print(json_string)
