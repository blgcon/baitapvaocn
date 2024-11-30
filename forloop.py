print(""" bấm 1 để in dãy số từ 1 đên n
      bấm 2 để in bảng cửu chương
      bấm 3 để in ra số nguyên tố từ 1 đến n
      bấm 4 để in dãy fibonacci 
      bám 5 để tính tổng số chãn từ 1 đến n 
      bấm 6 để tính tổng các số chia hết cho 3 trong 1 danh sách""" )
i = int(input())

if i == 1 :
    g = int(input())
    def day(k):
        for i in range(1,k+1):
            print(i)
        
    print(day(g))


if i == 2 :
    a = int(input())

    def nhan(x):
        if x > 0 and x < 10:
            for y in range(1,11):
                f = x * y
                print("{} * {} = {}" .format(y,x,f))

    print(nhan(a))

if i == 5 :
    a = int(input())
    
    def tong(h):
        count = 0
        for u in range(0,h+1):
            if u % 2 == 0 :
                count += u
               
        return count

    print("tổng các số chẵn là :",tong(a))


if i == 6 :
    n = int(input("nhập số các chữ số"))
    a = []
    for z in range(1,n +1 ):
        z = int(input("nhập các số"))
        a.append(z)

    def tong(h):
        count=0
        for l  in  h :
            if l % 3 == 0:
                count += l

        return count
    print("tổng các số chia hết cho 3 là ",tong(a))

if i == 4 :
    a = int(input())
    
    def fibonaci(u):
        l = []
        a = 0
        b = 1
        p = [0,1]
        for h in range(1,u-1):
            tong = a + b
            a = b
            b = tong
            l.append(tong)
        for i in l :
            if i < u :
                p.append(i)

        return p
        
    print(fibonaci(a))



else :
    print("nhap dung huong dan")



       




        

    
        


