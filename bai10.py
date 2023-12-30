# Lớp điểm, là lớp cơ sở cho các lớp khác
class Diem:
    # Hàm tạo với tham số là tọa độ x, y của điểm
    def __init__(self, x, y):
        self.x = x # Hoành độ
        self.y = y # Tung độ
    
    # Phương thức để nhập tọa độ điểm từ bàn phím
    def nhap(self):
        self.x = float(input("Nhập hoành độ: "))
        self.y = float(input("Nhập tung độ: "))
    
    # Phương thức để hiển thị tọa độ điểm
    def hien_thi(self):
        print(f"Điểm có tọa độ ({self.x}, {self.y})")

# Lớp elip, kế thừa từ lớp điểm
class Elip(Diem):
    # Hàm tạo với tham số là tọa độ tâm, bán trục lớn và bán trục nhỏ của elip
    def __init__(self, x, y, a, b):
        super().__init__(x, y) # Gọi hàm tạo của lớp cha
        self.a = a # Bán trục lớn
        self.b = b # Bán trục nhỏ
    
    # Ghi đè phương thức nhập, nhập thêm bán trục lớn và bán trục nhỏ
    def nhap(self):
        super().nhap() # Gọi phương thức nhập của lớp cha
        self.a = float(input("Nhập bán trục lớn: "))
        self.b = float(input("Nhập bán trục nhỏ: "))
    
    # Ghi đè phương thức hiển thị, hiển thị thêm bán trục lớn và bán trục nhỏ
    def hien_thi(self):
        super().hien_thi() # Gọi phương thức hiển thị của lớp cha
        print(f"Elip có bán trục lớn {self.a} và bán trục nhỏ {self.b}")
    
    # Phương thức để tính diện tích elip, trả về tích của bán trục lớn, bán trục nhỏ và pi
    def tinh_dien_tich(self):
        import math # Nhập thư viện toán học
        return self.a * self.b * math.pi

# Lớp đường tròn, kế thừa từ lớp elip
class DuongTron(Elip):
    # Hàm tạo với tham số là tọa độ tâm và bán kính của đường tròn
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r) # Gọi hàm tạo của lớp cha với a = b = r
    
    # Ghi đè phương thức nhập, chỉ nhập tọa độ tâm và bán kính
    def nhap(self):
        super().nhap() # Gọi phương thức nhập của lớp cha
        self.a = self.b # Đồng bộ bán trục lớn và bán trục nhỏ
    
    # Ghi đè phương thức hiển thị, chỉ hiển thị tọa độ tâm và bán kính
    def hien_thi(self):
        super().hien_thi() # Gọi phương thức hiển thị của lớp cha
        print(f"Đường tròn có bán kính {self.a}")
