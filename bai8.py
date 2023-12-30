# Lớp Date để lưu trữ ngày tháng năm
class Date:
    # Hàm tạo với 3 tham số
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    # Hàm tạo mặc định
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000
    
    # Phương thức __str__ để trả về chuỗi có định dạng ngày/tháng/năm
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

# Lớp Employee để lưu trữ thông tin của một nhân viên
class Employee:
    # Hàm tạo với 4 tham số
    def __init__(self, name, birth_date, join_date, salary):
        self.name = name
        self.birth_date = birth_date
        self.join_date = join_date
        self.salary = salary
    
    # Hàm tạo mặc định
    def __init__(self):
        self.name = "Unknown"
        self.birth_date = Date()
        self.join_date = Date()
        self.salary = 0.0
    
    # Phương thức __str__ để trả về chuỗi có định dạng thông tin nhân viên
    def __str__(self):
        return f"Name: {self.name}\n" + \
               f"Birth date: {self.birth_date}\n" + \
               f"Join date: {self.join_date}\n" + \
               f"Salary: {self.salary}"

# Lớp EmployeeManager để quản lý danh sách nhân viên
class EmployeeManager:
    # Hàm tạo với tham số là kích thước của danh sách
    def __init__(self, size):
        self.employees = [] # Danh sách để lưu trữ nhân viên
        self.size = size # Kích thước tối đa của danh sách
        self.count = 0 # Biến để đếm số lượng nhân viên hiện có
    
    # Phương thức để thêm một nhân viên vào danh sách
    def add_employee(self, employee):
        if self.count < self.size:
            self.employees.append(employee)
            self.count += 1
        else:
            print("The list is full. Cannot add more employee.")
    
    # Phương thức để sửa thông tin của một nhân viên theo tên
    def edit_employee(self, name, employee):
        found = False
        for i in range(self.count):
            if self.employees[i].name == name:
                self.employees[i] = employee
                found = True
                break
        if not found:
            print(f"Cannot find employee with name {name}")
    
    # Phương thức để xóa một nhân viên theo tên
    def delete_employee(self, name):
        found = False
        for i in range(self.count):
            if self.employees[i].name == name:
                self.employees.pop(i)
                self.count -= 1
                found = True
                break
        if not found:
            print(f"Cannot find employee with name {name}")
    
    # Phương thức để sắp xếp nhân viên theo lương tăng dần
    def sort_employee_by_salary(self):
        self.employees.sort(key=lambda e: e.salary)
    
    # Phương thức để sắp xếp nhân viên theo tên theo thứ tự từ điển
    def sort_employee_by_name(self):
        self.employees.sort(key=lambda e: e.name)
    
    # Phương thức để hiển thị danh sách nhân viên
    def show_employee(self):
        for employee in self.employees:
            print(employee)
            print("---------------------")

# Lớp Main để chạy chương trình và thực hiện các chức năng
class Main:
    def main():
        # Tạo một đối tượng EmployeeManager với kích thước danh sách là 10
        manager = EmployeeManager(10)
        
        # Tạo một số đối tượng Employee để thêm vào danh sách
        e1 = Employee("Nguyen Van A", Date(1, 1, 1990), Date(1, 1, 2010), 1000.0)
        e2 = Employee("Tran Thi B", Date(2, 2, 1991), Date(2, 2, 2011), 2000.0)
        e3 = Employee("Le Van C", Date(3, 3, 1992), Date(3, 3, 2012), 3000.0)
        
        # Thêm các đối tượng Employee vào danh sách
        manager.add_employee(e1)
        manager.add_employee(e2)
        manager.add_employee(e3)
        
        # Hiển thị danh sách nhân viên
        print("Danh sách nhân viên:")
        manager.show_employee()
        
        # Sửa thông tin của nhân viên có tên là Nguyen Van A
        e4 = Employee("Nguyen Van A", Date(4, 4, 1993), Date(4, 4, 2013), 4000.0)
        manager.edit_employee("Nguyen Van A", e4)
        
        # Xóa nhân viên có tên là Tran Thi B
        manager.delete_employee("Tran Thi B")
        
        # Sắp xếp nhân viên theo lương tăng dần
        manager.sort_employee_by_salary()
        
        # Hiển thị lại danh sách nhân viên
        print("Danh sách nhân viên sau khi sửa, xóa và sắp xếp:")
        manager.show_employee()
    
    # Gọi hàm main để chạy chương trình
    if __name__ == "__main__":
        main()
