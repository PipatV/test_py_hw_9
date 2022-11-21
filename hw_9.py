#รับvector1
v1,v2 = input("input vector1:").split()
v1 = int(v1)
v2 = int(v2)

v_12 = v1+v2

#รับvector2
v3,v4 = input("input vector2:").split()
v3 = int(v3)
v4 = int(v4)

v_34 = v3+v4

#รับvector3
v5,v6 = input("input vector3:").split()
v5 = int(v5)
v6 = int(v6)

v_56 = v5+v6

#รับvector4
v7,v8 = input("input vector4:").split()
v7 = int(v7)
v8 = int(v8)

v_78 = v7+v8

#รับvector5
v9,v10 = input("input vector5:").split()
v9 = int(v9)
v10 = int(v10)

v_910 = v9+v10

#ตรวจVectorขนาดมากสุด
if (v_12>v_34 and v_12>v_56 and v_12>v_78 and v_12>v_910):
    print("Bigest Vector is",v1,v2)
elif (v_34>v_12 and v_34>v_56 and v_34>v_78 and v_34>v_910):
    print("Bigest Vector is",v3,v4)
elif(v_56>v_12 and v_56>v_34 and v_56>v_78 and v_56>v_910):
    print("Bigest Vector is",v5,v6)
elif(v_78>v_12 and v_78>v_34 and v_78>v_56 and v_78>v_910):
    print("Bigest Vector is",v7,v8)
elif(v_910>v_12 and v_910>v_34 and v_910>v_56 and v_910>v_78):
    print("Bigest Vector is",v9,v10)