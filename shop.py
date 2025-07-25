from db import north, isan, central, south

def choose_re(region):
    if region == 1 :
        print("---------------------------")
        print("คุณเลือกภาคกลาง")
    elif region == 2 :
        print("---------------------------")
        print("คุณเลือกภาคเหนือ")
    elif region == 3 :
        print("---------------------------")
        print("คุณเลือกภาคใต้")
    elif region == 4 :
        print("---------------------------")
        print("คุณเลือกภาคอีสาน")

def chooseRegion(region):
    if region == 1:
        print("=== ภาคกลาง ===")
        for province in central:
            print(f"\nจังหวัด: {province['city']}")
            for item in province['souvenirs']:
                print(f"- {item['product']}: {item['price']} ฿ \nเหลือ {item['stock']} ชิ้น")
    elif region == 2:
        print("=== ภาคเหนือ ===")
        for province in north:
            print(f"\nจังหวัด: {province['city']}")
            for item in province['souvenirs']:
                print(f"- {item['product']}: {item['price']} ฿ \nเหลือ {item['stock']} ชิ้น")
    elif region == 3:
        print("=== ภาคใต้ ===")
        for province in south:
            print(f"\nจังหวัด: {province['city']}")
            for item in province['souvenirs']:
                print(f"- {item['product']}: {item['price']} ฿ \nเหลือ {item['stock']} ชิ้น")
    elif region == 4:
        print("=== ภาคอีสาน ===")
        for province in isan:
            print(f"\nจังหวัด: {province['city']}")
            for item in province['souvenirs']:
                print(f"- {item['product']}: {item['price']} ฿ \nเหลือ {item['stock']} ชิ้น")

print("ระบบเช็ค stock สินค้าและราคาร้านอาหาร")
i = int(input("เช็คสินค้ากด 1 / ไม่เช็คสินค้า กด 2 \n"))

if i == 1 :
    region = int(input("เลือกภาคที่ต้องการเช็ค\n 1.ภาคกลาง \n2.ภาคเหนือ \n3.ภาคใต้ \n4.ภาคอีสาน\n"))
else :
    print("ลาก่อน")
    region = 0

choose_re(region)
chooseRegion(region)
