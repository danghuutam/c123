# Định nghĩa lớp TS
class TS:
    # Hàm khởi tạo
    def __init__(self, ten, toan, ly, hoa):
        self.ten = ten # Họ tên thí sinh
        self.toan = toan # Điểm môn Toán
        self.ly = ly # Điểm môn Lý
        self.hoa = hoa # Điểm môn Hoá
    
    # Hàm nhập thông tin thí sinh
    def nhap(self):
        self.ten = input("Nhập họ tên thí sinh: ")
        self.toan = float(input("Nhập điểm môn Toán: "))
        self.ly = float(input("Nhập điểm môn Lý: "))
        self.hoa = float(input("Nhập điểm môn Hoá: "))
    
    # Hàm in thông tin thí sinh
    def in_thong_tin(self):
        print("Họ tên: ", self.ten)
        print("Điểm Toán: ", self.toan)
        print("Điểm Lý: ", self.ly)
        print("Điểm Hoá: ", self.hoa)
    
    # Hàm tính tổng điểm của thí sinh
    def tong_diem(self):
        return self.toan + self.ly + self.hoa

# Nhập số lượng thí sinh
n = int(input("Nhập số lượng thí sinh: "))

# Tạo một danh sách để lưu trữ các đối tượng TS
ds = []

# Nhập thông tin cho từng thí sinh và thêm vào danh sách
for i in range(n):
    print("Nhập thông tin thí sinh thứ", i+1)
    ts = TS("", 0, 0, 0) # Tạo một đối tượng TS rỗng
    ts.nhap() # Gọi hàm nhập để nhập thông tin
    ds.append(ts) # Thêm đối tượng TS vào danh sách

# Sắp xếp danh sách theo thứ tự giảm dần của tổng điểm
ds.sort(key=lambda ts: ts.tong_diem(), reverse=True)

# In ra danh sách thí sinh trúng tuyển
print("Danh sách thí sinh trúng tuyển:")
for ts in ds:
    if ts.tong_diem() >= 20: # Nếu tổng điểm >= 20
        ts.in_thong_tin() # In thông tin thí sinh
        print("Tổng điểm: ", ts.tong_diem()) # In tổng điểm
        print("------------------------")
