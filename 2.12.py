# Nhập module requests
import requests

# Tạo một biến để lưu trữ URL của API
url = "https://jsonplaceholder.typicode.com/comments?postId=1"

# Gửi một yêu cầu GET đến URL
response = requests.get(url)

# Kiểm tra trạng thái của yêu cầu
if response.status_code == 200:
    print("Yêu cầu thành công!")
else:
    print("Có lỗi xảy ra!")

# Chuyển đổi dữ liệu trả về từ định dạng JSON sang định dạng Python
data = response.json()

# In ra danh sách các bài post nổi bật
# Sắp xếp danh sách dữ liệu theo thuộc tính name
data = sorted(data, key=lambda x: x["name"])

# Giới hạn chỉ hiển thị 3 bài đầu tiên
data = data[:3]

# Duyệt qua từng phần tử trong danh sách dữ liệu, mỗi phần tử là một từ điển chứa thông tin về một bài post, và in ra các thông tin bao gồm: id, name, email, body
for post in data:
    print(f"id: {post['id']}")
    print(f"name: {post['name']}")
    print(f"email: {post['email']}")
    print(f"body: {post['body']}")
    print("-" * 20)
