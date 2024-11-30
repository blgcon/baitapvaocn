print("""bấm 1 để kiểm tra chẵn lẻ
bấm 2 để kiểm tra số âm dương hay là số dương
bấm 3 để kiểm tra giải phương trình bậc nhất
bấm 4 tính lương theo ca làm
bấm 5  kiểm tra năm nhuận
bấm 6 để kiểm tra học lực
bấm 7 để tính giá trị tuyệt đối
bấm 8 để kiểm tra ngày trong tháng 
bấm 9 kiểm tra tuổi họp lệ hay không""")

i = int(input())




if i == 1:
    p = int(input())
    if p > 0 :
        def ham(p):
            if (p % 2 == 0):
                print(p , "là số chẵn ")
            else:
                print(p, "là số lẻ ")

        
            if p < 0 : 
                print(" không thỏa mãn ")
                return p
        
        ham(p)

if i == 2 :
    def ham(z):
        if z > 0 :
            print(z,"là số dương")
        elif z == 0 :
            print(z,"không phải số âm hoặc số dương")
        else :
            print( z ,"là số âm ")
        
        return z
    
    z = int(input())
    ham(z)


if i == 3 :
    print("phương trình có dạng ax + b = 0")
    x = int(input(" nhập số a"))
    y = int(input(" nhập số b"))
    def pt(a,b):
        if a == 0 and b == 0 :
            return "phương trình có vô số nghiệm với mọi x"
        elif a == 0 and b != 0 :
            return "phương trình vô nghiệm với mọi x"
        elif a != 0 :
           return"Nghiệm của phương trình bậc nhất là {}".format(float(-b/a))
    l = pt(x,y)
    print(l)

if i == 4 :
    g = int(input())
    def gio(k):
        if k <= 40 :
            return "lương tháng này là {}".format(k*2)
        if k >= 40 :
            return "lương tháng này là {}".format(40*2 + (k-40)*4)
        
    h = gio(g)
    print(h)

if i == 5 :
    g = int(input())
    def nam(k):
        if (k % 4 == 0 and k != 100 == 0) or (k % 400 == 0) :
            return k , " là năm nhuận"
        else :
            return k , "không phải là năm nhuận"
        
    l = nam(g)
    print(l)

if i == 6 :
    g = float(input())
    def hocluc(k):
        if  k >0  and k <= 10 :
            if k >= 8 :
                return "học lực giỏi"
            if k >= 7 :
                return "học lực khá"
            if k >= 6 :
                return "học lực trung bình"
            else:
                return "học lực yếu"
            
        else :
            return "số không phù hợp"
        
    print(hocluc(g))

if i == 7 :
    g = float(input())
    def tuyetdoi(i):
        if i >=0 :
            return i
        else:
            return -i
    print(tuyetdoi(g))

if i == 9 :
    g = int(input())
    def tuoi(i):
        if i >= 18 :
            return i ,"là tuổi hợp lệ"
        if i <= 18 :
            return i , "là tuổi không hợp lệ"
        else :
            return "không có tuổi âm"
        
    print(tuoi(g))

if i == 8 :
    h = int(input("nhập năm"))
    g = int(input("nhập tháng"))
    if (h % 4 == 0 and h != 100 == 0) or (h % 400 == 0):
        def thang(i):
            if 0 < i <= 12 :
                if i % 2 == 1 or i == 1 or i == 8 :
                    return "tháng {} có 31 ngày".format(i) 
                if i == 2 :
                    return "tháng 2 có 29 ngày"
                else :
                    return " tháng {} có 30 ngày ".format(i)
        print(thang(g))
    else :
        def thang(i):
            if 0 < i <= 12 :
                if i % 2 == 1 or i == 1 or i == 8 :
                    return "tháng {} có 31 ngày".format(i) 
                if i == 2 :
                    return "tháng 2 có 28 ngày"
                else :
                    return " tháng {} có 30 ngày ".format(i)
        print(thang(g))

else:
    print("nhập số đúng hướng dẫn")



            





    



    





    


