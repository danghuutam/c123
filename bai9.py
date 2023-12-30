# Lớp đa giác, là lớp cơ sở cho các lớp khác
class DaGiac:
    # Hàm tạo với tham số là số cạnh của đa giác
    def __init__(self, n):
        self.n = n # Số cạnh
        self.cac_canh = [] # Danh sách để lưu trữ độ dài các cạnh
    
    # Phương thức để nhập độ dài các cạnh từ bàn phím
    def nhap_cac_canh(self):
        self.cac_canh = [] # Xóa danh sách cũ
        for i in range(self.n):
            canh = float(input(f"Nhập cạnh thứ {i + 1}: "))
            self.cac_canh.append(canh) # Thêm cạnh vào danh sách
    
    # Phương thức để hiển thị độ dài các cạnh
    def hien_thi_cac_canh(self):
        for i in range(self.n):
            print(f"Cạnh thứ {i + 1} có độ dài {self.cac_canh[i]}")
    
    # Phương thức để tính chu vi, trả về tổng độ dài các cạnh
    def tinh_chu_vi(self):
        return sum(self.cac_canh)
    
    # Phương thức để tính diện tích, mặc định trả về 0
    def tinh_dien_tich(self):
        return 0

# Lớp hình bình hành, kế thừa từ lớp đa giác
class HinhBinhHanh(DaGiac):
    # Hàm tạo với tham số là độ dài hai cạnh kề và chiều cao
    def __init__(self, a, b, h):
        super().__init__(4) # Gọi hàm tạo của lớp cha với n = 4
        self.a = a # Cạnh đáy
        self.b = b # Cạnh bên
        self.h = h # Chiều cao
    
    # Ghi đè phương thức nhập các cạnh, chỉ nhập độ dài hai cạnh kề và chiều cao
    def nhap_cac_canh(self):
        self.a = float(input("Nhập độ dài cạnh đáy: "))
        self.b = float(input("Nhập độ dài cạnh bên: "))
        self.h = float(input("Nhập chiều cao: "))
        # Tính độ dài cạnh đáy kia theo công thức: c^2 = a^2 + b^2 - 2ab*cos(C)
        # Trong đó C là góc giữa hai cạnh kề, cos(C) = (a^2 + b^2 - c^2) / (2ab)
        # => c = sqrt(a^2 + b^2 - ab * (a^2 + b^2 - c^2) / (a^2))
        # Giả sử cạnh đáy kia là cạnh thứ 3
        self.cac_canh = [self.a, self.b, 0, self.b] # Khởi tạo danh sách các cạnh
        self.cac_canh[2] = (self.a**2 + self.b**2 - self.a * self.b * (self.a**2 + self.b**2 - self.cac_canh[2]**2) / (self.a**2))**0.5 # Tính cạnh thứ 3
    
    # Ghi đè phương thức tính diện tích, trả về tích của cạnh đáy và chiều cao
    def tinh_dien_tich(self):
        return self.a * self.h

# Lớp hình chữ nhật, kế thừa từ lớp hình bình hành
class HinhChuNhat(HinhBinhHanh):
    # Hàm tạo với tham số là độ dài hai cạnh kề
    def __init__(self, a, b):
        super().__init__(a, b, b) # Gọi hàm tạo của lớp cha với h = b
    
    # Ghi đè phương thức nhập các cạnh, chỉ nhập độ dài hai cạnh kề
    def nhap_cac_canh(self):
        self.a = float(input("Nhập độ dài cạnh dài: "))
        self.b = float(input("Nhập độ dài cạnh ngắn: "))
        self.h = self.b # Chiều cao bằng cạnh ngắn
        self.cac_canh = [self.a, self.b, self.a, self.b] # Khởi tạo danh sách các cạnh

# Lớp hình vuông, kế thừa từ lớp hình chữ nhật
class HinhVuong(HinhChuNhat):
    # Hàm tạo với tham số là độ dài cạnh
    def __init__(self, a):
        super().__init__(a, a) # Gọi hàm tạo của lớp cha với a = b
    
    # Ghi đè phương thức nhập các cạnh, chỉ nhập độ dài cạnh
    def nhap_cac_canh(self):
        self.a = float(input("Nhập độ dài cạnh: "))
        self.b = self.a # Cạnh ngắn bằng cạnh dài
        self.h = self.a # Chiều cao bằng cạnh
        self.cac_canh = [self.a, self.a, self.a, self.a] # Khởi tạo danh sách các cạnh

# Lớp main để chạy chương trình và thực hiện các chức năng
class Main:
    def main():
        # Tạo một đối tượng hình bình hành
        hbh = HinhBinhHanh(0, 0, 0)
        # Nhập các cạnh của hình bình hành
        print("Nhập hình bình hành:")
        hbh.nhap_cac_canh()
        # Hiển thị các cạnh của hình bình hành
        print("Các cạnh của hình bình hành:")
        hbh.hien_thi_cac_canh()
        # Tính và hiển thị chu vi và diện tích của hình bình hành
        print(f"Chu vi của hình bình hành: {hbh.tinh_chu_vi()}")
        print(f"Diện tích của hình bình hành: {hbh.tinh_dien_tich()}")
        print("---------------------")
        
        # Tạo một đối tượng hình chữ nhật
        hcn = HinhChuNhat(0, 0)
        # Nhập các cạnh của hình chữ nhật
        print("Nhập hình chữ nhật:")
        hcn.nhap_cac_canh()
        # Hiển thị các cạnh của hình chữ nhật
        print("Các cạnh của hình chữ nhật:")
        hcn.hien_thi_cac_canh()
        # Tính và hiển thị chu vi và diện tích của hình chữ nhật
        print(f"Chu vi của hình chữ nhật: {hcn.tinh_chu_vi()}")
        print(f"Diện tích của hình chữ nhật: {hcn.tinh_dien_tich()}")
        print("---------------------")
        
        # Tạo một đối tượng hình vuông
        hv = HinhVuong(0)
        # Nhập cạnh của hình vuông
        print("Nhập hình vuông:")
        hv.nhap_cac_canh()
        # Hiển thị các cạnh của hình vuông
        print("Các cạnh của hình vuông:")
        hv.hien_thi_cac_canh()
        # Tí