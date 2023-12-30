# Lớp biểu diễn hình chữ nhật
class HinhChuNhat:
    # Phương thức khởi tạo với hai tham số là chiều dài và chiều rộng
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    # Phương thức nhập dữ liệu hai cạnh cho hình chữ nhật
    def nhap_du_lieu(self):
        # Nhập chiều dài
        self.chieu_dai = float(input("Nhập chiều dài: "))
        # Nhập chiều rộng
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    # Phương thức tính chu vi hình chữ nhật
    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2

    # Phương thức tính diện tích hình chữ nhật
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    # Phương thức in thông tin hình chữ nhật
    def in_thong_tin(self):
        print("Hình chữ nhật có chiều dài là", self.chieu_dai, "và chiều rộng là", self.chieu_rong)
        print("Chu vi hình chữ nhật là", self.tinh_chu_vi())
        print("Diện tích hình chữ nhật là", self.tinh_dien_tich())

# Lớp chứa phương thức main để thực thi chương trình
if __name__ == "__main__":
    # Tạo đối tượng hình chữ nhật
    hcn = HinhChuNhat(0, 0)
    # Nhập dữ liệu cho hình chữ nhật
    hcn.nhap_du_lieu()
    # In thông tin hình chữ nhật
    hcn.in_thong_tin()
