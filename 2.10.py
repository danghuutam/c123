# Nhập module json và module datetime
import json
import datetime

# Sử dụng lại chương trình quản lý giao dịch đã làm
# Giả sử chương trình này có các biến sau:
# balance: số dư tiền của người dùng
# gold: số lượng vàng của người dùng
# rate: tỷ giá quy đổi giữa tiền và vàng
# transactions: danh sách các giao dịch

# Hỏi người dùng muốn thực hiện giao dịch nào
print("Chọn loại giao dịch bạn muốn thực hiện:")
print("1. Mua vàng")
print("2. Bán vàng")
print("3. Xem số dư")
print("4. Thoát")
choice = input("Nhập lựa chọn của bạn (1, 2, 3 hoặc 4): ")

# Thực hiện giao dịch theo lựa chọn của người dùng
while choice != "4":
    if choice == "1":
        # Mua vàng
        print("Bạn muốn mua bao nhiêu vàng?")
        amount = float(input("Nhập số lượng vàng (tối đa 2 chữ số thập phân): "))
        # Kiểm tra số lượng vàng có hợp lệ không
        if amount <= 0 or round(amount, 2) != amount:
            print("Số lượng vàng không hợp lệ!")
        else:
            # Tính số tiền cần trả
            money = amount * rate
            # Kiểm tra số dư tiền có đủ không
            if money > balance:
                print("Số dư tiền của bạn không đủ để mua vàng!")
            else:
                # Cập nhật số dư tiền và số lượng vàng
                balance -= money
                gold += amount
                # Tạo một từ điển để lưu trữ thông tin về giao dịch
                transaction = {
                    "type": "buy",
                    "amount": money,
                    "gold": amount,
                    "time": datetime.datetime.now()
                }
                # Thêm từ điển vào danh sách các giao dịch
                transactions.append(transaction)
                # In ra thông báo thành công
                print(f"Bạn đã mua {amount} vàng với giá {money} tiền. Số dư tiền của bạn còn {balance} tiền. Số lượng vàng của bạn là {gold} vàng.")
    elif choice == "2":
        # Bán vàng
        print("Bạn muốn bán bao nhiêu vàng?")
        amount = float(input("Nhập số lượng vàng (tối đa 2 chữ số thập phân): "))
        # Kiểm tra số lượng vàng có hợp lệ không
        if amount <= 0 or round(amount, 2) != amount:
            print("Số lượng vàng không hợp lệ!")
        else:
            # Kiểm tra số lượng vàng có đủ không
            if amount > gold:
                print("Số lượng vàng của bạn không đủ để bán!")
            else:
                # Tính số tiền nhận được
                money = amount * rate
                # Cập nhật số dư tiền và số lượng vàng
                balance += money
                gold -= amount
                # Tạo một từ điển để lưu trữ thông tin về giao dịch
                transaction = {
                    "type": "sell",
                    "amount": money,
                    "gold": amount,
                    "time": datetime.datetime.now()
                }
                # Thêm từ điển vào danh sách các giao dịch
                transactions.append(transaction)
                # In ra thông báo thành công
                print(f"Bạn đã bán {amount} vàng với giá {money} tiền. Số dư tiền của bạn là {balance} tiền. Số lượng vàng của bạn còn {gold} vàng.")
    elif choice == "3":
        # Xem số dư
        print(f"Số dư tiền của bạn là {balance} tiền. Số lượng vàng của bạn là {gold} vàng.")
    else:
        # Lựa chọn không hợp lệ
        print("Lựa chọn của bạn không hợp lệ!")
    
    # Hỏi người dùng muốn tiếp tục giao dịch hay không
    print("Bạn có muốn tiếp tục giao dịch không?")
    print("1. Có")
    print("2. Không")
    continue_choice = input("Nhập lựa chọn của bạn (1 hoặc 2): ")
    if continue_choice == "1":
        # Tiếp tục giao dịch
        print("Chọn loại giao dịch bạn muốn thực hiện:")
        print("1. Mua vàng")
        print("2. Bán vàng")