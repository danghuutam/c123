# Lớp tam giác, là lớp cơ sở cho các lớp khác
class TamGiac:
    # Hàm tạo với tham số là 3 cạnh của tam giác
    def __init__(self, a, b, c):
        self.a = a # Cạnh a
        self.b = b # Cạnh b
        self.c = c # Cạnh c
    
    # Phương thức để nhập độ dài 3 cạnh từ bàn phím
    def nhap_cac_canh(self):
        self.a = float(input("Nhập cạnh a: "))
        self.b = float(input("Nhập cạnh b: "))
        self.c = float(input("Nhập cạnh c: "))
    
    # Phương thức để hiển thị độ dài 3 cạnh
    def hien_thi_cac_canh(self):
        print(f"Cạnh a có độ dài {self.a}")
        print(f"Cạnh b có độ dài {self.b}")
        print(f"Cạnh c có độ dài {self.c}")
    
    # Phương thức để xác định kiểu tam giác
    def xac_dinh_kieu(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a: # Điều kiện tồn tại tam giác
            if self.a == self.b == self.c: # 3 cạnh bằng nhau
                return "Tam giác đều"
            elif self.a == self.b or self.a == self.c or self.b == self.c: # 2 cạnh bằng nhau
                return "Tam giác cân"
            elif self.a**2 + self.b**2 == self.c**2 or self.a**2 + self.c**2 == self.b**2 or self.b**2 + self.c**2 == self.a**2: # Bình phương 1 cạnh bằng tổng bình phương 2 cạnh còn lại
                return "Tam giác vuông"
            else: # Không thuộc các trường hợp trên
                return "Tam giác thường"
        else: # Không thỏa điều kiện tồn tại tam giác
            return "Không phải tam giác"
    
    # Phương thức để tính chu vi tam giác, trả về tổng 3 cạnh
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    
    # Phương thức để tính diện tích tam giác, sử dụng công thức Heron
    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2 # Nửa chu vi
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5 # Căn bậc hai của tích p và các hiệu p với 3 cạnh

# Lớp tam giác vuông, kế thừa từ lớp tam giác
class TamGiacVuong(TamGiac):
    # Hàm tạo với tham số là 2 cạnh góc vuông và cạnh huyền của tam giác vuông
    def __init__(self, a, b, c):
        super().__init__(a, b, c) # Gọi hàm tạo của lớp cha
    
    # Ghi đè phương thức nhập các cạnh, chỉ nhập 2 cạnh góc vuông và tính cạnh huyền theo định lý Pythagoras
    def nhap_cac_canh(self):
        self.a = float(input("Nhập cạnh góc vuông a: "))
        self.b = float(input("Nhập cạnh góc vuông b: "))
        self.c = (self.a**2 + self.b**2)**0.5 # Tính cạnh huyền
    
    # Ghi đè phương thức xác định kiểu, luôn trả về "Tam giác vuông"
    def xac_dinh_kieu(self):
        return "Tam giác vuông"
    
    # Ghi đè phương thức tính diện tích, trả về tích của 2 cạnh góc vuông chia 2
    def tinh_dien_tich(self):
        return self.a * self.b / 2

# Lớp tam giác cân, kế thừa từ lớp tam giác
class TamGiacCan(TamGiac):
    # Hàm tạo với tham số là 2 cạnh bằng nhau và cạnh đáy của tam giác cân
    def __init__(self, a, b, c):
        super().__init__(a, b, c) # Gọi hàm tạo của lớp cha
    
    # Ghi đè phương thức nhập các cạnh, chỉ nhập 2 cạnh bằng nhau và cạnh đáy
    def nhap_cac_canh(self):
        self.a = float(input("Nhập cạnh bằng nhau a: "))
        self.b = self.a # Cạnh b bằng cạnh a
        self.c = float(input("Nhập cạnh đáy c: "))
    
    # Ghi đè phương thức xác định kiểu, kiểm tra xem tam giác cân có phải tam giác đều không
    def xac_dinh_kieu(self):
        if self.a == self.c: # Nếu cạnh đáy bằng cạnh bằng nhau
            return "Tam giác đều" # Trả về tam giác đều
        else: # Nếu không
            return "Tam giác cân" # Trả về tam giác cân
    
    # Ghi đè phương thức tính diện tích, sử dụng công thức S = (c * h) / 2
    # Trong đó h là chiều cao của tam giác cân, h = sqrt(a^2 - (c/2)^2)
    def tinh_dien_tich(self):
        h = (self.a**2 - (self.c / 2)**2)**0.5 # Tính chiều cao
        return (self.c * h) / 2 # Tính diện tích

# Lớp tam giác đều, kế thừa từ lớp tam giác cân
class TamGiacDeu(TamGiacCan):
    # Hàm tạo với tham số là cạnh của tam giác đều
    def __init__(self, a):
        super().__init__(a, a, a) # Gọi hàm tạo của lớp cha với a = b = c
    
    # Ghi đè phương thức nhập các cạnh, chỉ nhập 1 cạnh
    def nhap_cac_canh(self):
        self.a = float(input("Nhập cạnh a: "))
        self.b = self.a # Cạnh b bằng cạnh a
        self.c = self.a # Cạnh c bằng cạnh a
    
    # Ghi đè phương thức xác định kiểu, luôn trả về "Tam giác đều"
    def xac_dinh_kieu(self):
        return "Tam giác đều"
    
    # Ghi đè phương thức tính diện tích, sử dụng công thức S = (a^2 * sqrt(3)) / 4
    def tinh_dien_tich(self):
        import math # Nhập thư viện toán học
        return (self.a**2 * math.sqrt(3)) / 4 # Tính diện tích