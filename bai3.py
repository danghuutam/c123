# Định nghĩa lớp PS
class PS:
    # Hàm khởi tạo
    def __init__(self, tu, mau):
        self.tu = tu # Tử số
        self.mau = mau # Mẫu số
    
    # Hàm kiểm tra tính hợp lệ của phân số
    def hop_le(self):
        return self.mau != 0 # Mẫu số khác 0
    
    # Hàm nhập phân số
    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        while not self.hop_le(): # Nếu phân số không hợp lệ
            print("Phân số không hợp lệ. Mời nhập lại.")
            self.mau = int(input("Nhập mẫu số: "))
    
    # Hàm in phân số ra màn hình
    def in_ps(self):
        print(f"{self.tu}/{self.mau}")
