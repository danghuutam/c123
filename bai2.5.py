# Nhập các module cần thiết
import requests
import xml.etree.ElementTree
import csv

# Tải nguồn cấp RSS từ URL cho trước
response = requests.get("http://www.hindustantimes.com/rss/topnews/rssfeed.xml")

# Phân tích cú pháp tệp XML thành một đối tượng ElementTree
tree = xml.etree.ElementTree.fromstring(response.content)

# Lấy danh sách các phần tử có tên thẻ là "item"
items = tree.findall(".//item")

# Tạo một danh sách rỗng để lưu trữ các mục tin tức
news_list = []

# Duyệt qua danh sách các phần tử "item"
for item in items:
    # Tạo một từ điển rỗng để lưu trữ các thông tin của mục tin tức
    news_dict = {}
    # Lấy các phần tử con có tên thẻ là "title", "link", "description", "pubDate" và "guid"
    # và lấy nội dung của chúng bằng thuộc tính text
    news_dict["title"] = item.find("title").text
    news_dict["link"] = item.find("link").text
    news_dict["description"] = item.find("description").text
    news_dict["pubDate"] = item.find("pubDate").text
    news_dict["guid"] = item.find("guid").text
    # Thêm từ điển của mục tin tức vào danh sách tin tức
    news_list.append(news_dict)

# Tạo một đối tượng writer, và mở một tệp CSV để ghi dữ liệu
with open("news.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "link", "description", "pubDate", "guid"])
    # Ghi tiêu đề của các cột vào tệp CSV
    writer.writeheader()
    # Ghi toàn bộ danh sách tin tức vào tệp CSV
    writer.writerows(news_list)
