print("""1 tìm tính tổng các số chẵn trong danh sách 
2 Đếm số lần xuất hiện của một phần tử trong danh sách
3 Tìm chuỗi dài nhất trong danh sách
4 Lọc các số nguyên tố trong một danh sách 
5 Tạo một từ điển từ hai danh sách
6 Chuyển đổi một chuỗi thành chữ hoa/chữ thường
7  Sắp xếp một danh sách theo thứ tự giảm dần
8 Tìm số lớn nhất trong danh sách""")

i = int(input())

if i == 1 :
    u = int(input("nhập số các chữ số "))
    a = []
    for h in range(1,u+1):
        h = int(input("số thứ {} là :".format(h)))
        a.append(h)
    def even(x):
        count = 0
        for p in x :
            if p % 2 == 0 :
                count += p
        return count
    print(even(a))

if i == 2 :
    u = int(input("nhập số các chữ số "))
    a = []
    for h in range(1,u+1):
        h = int(input("số thứ {} là :".format(h)))
        a.append(h)
    def tracuu(x,y):
        count = 0
        for j in x :
            if y == j:
                count +=1
        return count
    z = int(input(" số cần tra cứu "))
    print("số chữ số {} là : ".format(z),tracuu(a,z))

if i == 3 :
    h = int(input(" nhập số các xâu kí tự"))
    a = []
    for l in range(1,h+1):
        l = str(input(" nhập xâu thứ {} ".format(l)))
        a.append(l)
    def tian(x):
        longest = x[0]
        for j in x :
            if len(j) > len(longest):
                longest = j 
        return longest
    print(tian(a))

if i == 4 :

    u = int(input("nhập số các chữ số "))
    a = []
    for h in range(1,u+1):
        h = int(input("số thứ {} là :".format(h)))
        a.append(h)
    def prime(x):
        z = []
        p = []
        for l in x:
            if l == 1 :
                z.append(l)
            for k in range(2, int(l**0.5) + 1):  
                if l % k == 0:
                    p.append(l)
                else :
                    z.append(l)
                    break
        return z
    print(prime(a))

if i == 5 :
    l = int(input("nhập số các số key"))
    a = []
    b = []

    for i in (1,l+1):
        h = input("nhâp key thứ {}".format(i))
        a.append(h)
        k = input("nhập value {}".format(i))
        b.append(k)

    def dictation(key,value,p):
        mydic = {}
        for i in range(p):
            mydic[key[i]]=value[i]
        return mydic
    print(dictation(a,b,l))

if i == 6 :
   z = str(input())
   def inthuong(l):
       a = l.lower()
       return a
   print(inthuong(z))

if i == 8 :
    a = []
    z = int(input())
    for i in range(1,z+1):
        i = int(input())
        a.append(i)
    def m(x):
        max = x[0]
        for u in x :
            if u > max :
                max = u 
        return u 
    print(m(a))
        

            
        


    
                
            
            


        
        
            

    

    

   
    



    