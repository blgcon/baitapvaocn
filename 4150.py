print(""" nhập 1 để Tìm phần tử xuất hiện nhiều nhất trong một danh sách
nhập 2 để  Tính tổng các phần tử trong một từ điển
nhập 3 để Tính tổng của các số trong một chuỗi 
nhập 4 để Kiểm tra xem một chuỗi có phải là anagram không 
nhập 5 để Tìm các phần tử chung giữa hai danh sách
nhập 6 để Kiểm tra một số có phải là số hoàn hảo không
nhập 7 để Xóa tất cả các phần tử trùng lặp trong một danh sách
nhập 8 để Tính chiều dài của chuỗi mà không sử dụng len()
nhập 9 để Kiểm tra số Armstrong 
nhập 10 để Sắp xếp chuỗi theo thứ tự từ điển """)

i = int(input("nhập số để đưa ra yêu cầu"))

if i == 1:
    b = int(input("nhập số các chữ số"))
    a = []
    for h in range(1,b+1):
        h = int(input("nhập số thứ {}".format(h)))
        a.append(h)
    def mce(x):
        a = 0
        maxcount = 0
        for h in x :
            count = x.count(h)
            if count > a:
                a = count 
                count = maxcount
        return maxcount
    print(mce(a))





