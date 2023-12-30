# Định nghĩa lớp Date
class Date:
    # Hàm tạo với ba tham số có giá trị mặc định
    def __init__(self, day=1, month=1, year=2000):
        self.day = day # Ngày
        self.month = month # Tháng
        self.year = year # Năm
    
    # Phương thức display để in thông tin về ngày ra màn hình
    def display(self):
        print(f"{self.day:02d}-{self.month:02d}-{self.year:04d}")
    
    # Phương thức next để tính ngày tiếp theo
    def next(self):
        # Một mảng chứa số ngày của các tháng trong năm
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Kiểm tra năm nhuận
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            days_in_month[1] = 29 # Tháng 2 có 29 ngày
        
        # Tăng ngày lên 1
        self.day += 1

        # Nếu ngày vượt quá số ngày của tháng
        if self.day > days_in_month[self.month - 1]:
            self.day = 1 # Đặt lại ngày là 1
            self.month += 1 # Tăng tháng lên 1
        
        # Nếu tháng vượt quá 12
        if self.month > 12:
            self.month = 1 # Đặt lại tháng là 1
            self.year += 1 # Tăng năm lên 1
