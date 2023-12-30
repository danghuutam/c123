# Nhập module requests
import requests

# Tạo một biến để lưu trữ URL của API
url = "https://jsonplaceholder.typicode.com/posts"

# Gửi một yêu cầu GET đến URL
response = requests.get(url)

# Kiểm tra trạng thái của yêu cầu
if response.status_code == 200:
    print("Yêu cầu thành công!")
else:
    print("Có lỗi xảy ra!")

# Chuyển đổi dữ liệu trả về từ định dạng JSON sang định dạng Python
data = response.json()

# In ra tổng số bài post
print(f"Tổng số bài post: {len(data)}")

# Duyệt qua từng phần tử trong danh sách dữ liệu, mỗi phần tử là một từ điển chứa thông tin về một bài post, và in ra các thông tin bao gồm: userID, id, title, body
for post in data:
    print(f"userID: {post['userId']}")
    print(f"id: {post['id']}")
    print(f"title: {post['title']}")
    print(f"body: {post['body']}")
    print("-" * 20)
