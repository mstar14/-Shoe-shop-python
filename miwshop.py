a = []
f = (2500,5000,2000,3500,4000,3000,1500)
z=("Michael Kors","Chanel","Burberry","miw")
h=0
i=1
while True:
    b = input('*********Miwky Bag Shop*********\n[1] Michael Kors\tลด 20% \n[2] Chanel\t\tลด 30% \n[3] Burberry\t\tลด 70% \n[4] Miw \t\tลด 70%\n[5] Check \n[6] Exit \nEnter number: ')
    if b == '1':
        print('**********************************************')
        print(z[0])
        c = input('[1] Wallet\t\t\tราคา 2,500\n[2] Crossbody\t\t\tราคา 5,000\n[3] Saffiano handbag\t\tราคา 2,000\nSelect model : ')
        if c == '1':
            a.append('Wallet : 2,500 : 20% : 2,000')
            g = f[0]-((f[0]*20)/100) #h += 2000
            h += g
        elif c == '2':
            a.append('Crossbody Bag : 5,000 : 20% : 4,000')
            g = f[1]-((f[1]*20)/100) #h += 4000
            h += g
        elif c == '3':
            a.append('Saffiano handbag : 2,000 : 20% : 1,600')
            g = f[2]-((f[2]*20)/100) #h += 1600
            h += g
        print('\n***สิ้นค้าเข้าสู่ตะกร้าแล้ว***\n')
        print('เลือกสินค้าที่ต้องการ')
    elif b == '2':
        print('**********************************************')
        print(z[1])
        c = input('[1] Gabrielle \t\tราคา 3,500\n[2] Boy chanel \t\tราคา 4,000 \n[3] Camera case \tราคา 3,000 \nSelect model : ')
        if c == '1':
            a.append('Gabrielle : 3,500 : 30% : 2,450')
            g = f[3]-((f[3]*30)/100) #h += 2450
            h += g
        elif c == '2':
            a.append('Boy chanel : 4,000 : 30% : 2,800')
            g = f[4]-((f[4]*30)/100) #h += 2800
            h += g
        elif c == '3':
            a.append('Camera case : 3,000 : 30% : 2,100')
            g = f[5]-((f[5]*30)/100) #h += 2100
            h += g
        print('\n***สิ้นค้าเข้าสู่ตะกร้าแล้ว***\n')
        print('เลือกสินค้าที่ต้องการ')
    elif b == '3':
        print('**********************************************')
        print(z[2])
        c = input('[1] Paddy Messenger 96 \t\tราคา 2,500\n[2] Leather Barrel \t\tราคา 3,000\n[3] Horseferry print \t\tราคา 1,500\nSelect model : ')
        if c == '1':
            a.append('Paddy Messenger : 2,500 : 70% : 750')
            g = f[0]-((f[0]*70)/100) #h += 750
            h += g
        elif c == '2':
            a.append('Leather Barrel Bag : 3,000 : 70% : 900')
            g = f[5]-((f[5]*70)/100) #h += 900
            h += g
        elif c == '3':
            a.append('Horseferry print : 1,500 : 70% : 450')
            g = f[6]-((f[6]*70)/100) #h += 450
            h += g
        print('\n***สิ้นค้าเข้าสู่ตะกร้าแล้ว***\n')
        print('เลือกสินค้าที่ต้องการ')
    elif b == '4':
        print('**********************************************')
        print(z[3])
        c = input('[1] Sasinipha \t\tราคา 2,500\n[2] Moonmung \t\tราคา 3,000\n[3] Mimiwww \t\tราคา 1,500\nSelect model : ')
        if c == '1':
            a.append('Sasinipha : 2,500 : 70% : 750')
            g = f[0]-((f[0]*70)/100) #h += 750
            h += g
        elif c == '2':
            a.append('Moonmung : 3,000 : 70% : 900')
            g = f[5]-((f[5]*70)/100) #h += 900
            h += g
        elif c == '3':
            a.append('Mimiwww : 1,500 : 70% : 450')
            g = f[6]-((f[6]*70)/100) #h += 450
            h += g
        print('\n***สิ้นค้าเข้าสู่ตะกร้าแล้ว***\n')
        print('เลือกสินค้าที่ต้องการ')

    elif b == '5': 
        print("\n***************************บิลราคาสินค้า**************************")
        print("---------------------------------------------------------------")
        print("รุ่นรองเท้า              ราคา          ส่วนลด             จ่ายจริง")
        print("--------------------------------------------------------------")
        count = 0
        for x in a: 
            y = x.split(":")  
            count += 1
            print(count,end=")")
            print('{0[0]:_<20}{0[1]:_<15}{0[2]:_<17}{0[3]:_<10}'.format(y))       
        print("--------------------------------------------------------------")
        print("ราคารวม\t\t\t\t\t\t\t",h)
        print('**************************************************************')
        print('\n')
    elif b == '6':
        print("\n*****************ออกจากระบบ*****************")
        break