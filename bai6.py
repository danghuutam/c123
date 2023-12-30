# Định nghĩa lớp Stack
class Stack:
    # Hàm tạo
    def __init__(self, size):
        self.size = size # Kích thước tối đa của stack
        self.data = [] # Mảng float để lưu trữ dữ liệu
        self.top = -1 # Vị trí đỉnh của stack
    
    # Hàm huỷ
    def __del__(self):
        del self.data # Giải phóng bộ nhớ
    
    # Hàm push
    def push(self, x):
        if self.isFull(): # Nếu stack đã đầy
            print("Stack overflow") # Báo lỗi
        else: # Nếu stack còn chỗ
            self.top += 1 # Tăng vị trí đỉnh lên 1
            self.data.append(x) # Thêm phần tử x vào cuối mảng
    
    # Hàm pop
    def pop(self):
        if self.isEmpty(): # Nếu stack đã rỗng
            print("Stack underflow") # Báo lỗi
            return None # Trả về giá trị None
        else: # Nếu stack còn phần tử
            x = self.data[self.top] # Lấy phần tử ở đỉnh stack
            self.top -= 1 # Giảm vị trí đỉnh đi 1
            self.data.pop() # Xóa phần tử cuối mảng
            return x # Trả về giá trị x
    
    # Hàm kiểm tra stack rỗng
    def isEmpty(self):
        return self.top == -1 # Trả về True nếu đỉnh stack bằng -1
    
    # Hàm kiểm tra stack đầy
    def isFull(self):
        return self.top == self.size - 1 # Trả về True nếu đỉnh stack bằng kích thước tối đa trừ 1
    
    # Hàm trả về số phần tử trên stack
    def count(self):
        return self.top + 1 # Trả về số phần tử bằng vị trí đỉnh cộng 1
    
    # Hàm in nội dung của stack
    def print(self):
        if self.isEmpty(): # Nếu stack rỗng
            print("Stack is empty") # In thông báo
        else: # Nếu stack có phần tử
            print("Stack contains:", end=" ") # In tiêu đề
            for i in range(self.top + 1): # Duyệt từ đầu đến đỉnh stack
                print(self.data[i], end=" ") # In phần tử
            print() # Xuống dòng
