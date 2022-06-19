import BeautyStock
from BeautyStock.Beauty_products import cosmetics_name as td
# import price as p
print("Select product:")
print('''1. hair_fall,
2. face_wash,
3.face_mask''')
cosmetics_names=["","hair_fall","face_wash","peeloff_mask"]
mls_list=["","25ml","50ml","100ml","250ml","500ml"]
cosmetics_name=int(input("Enter the selection (1/2/3)"))




# print("please select ml")
# print('''1) 25ml
# 2) 50ml
# 3) 100ml
# 4) 250ml
# 5) 500ml
# ''')
# ml=int(input("select ml (1/2/3/4/5)"))
if cosmetics_name>=0 and  cosmetics_name<=3:
    res=td.shows(cosmetics_names[cosmetics_name])
    j=1
    temp=res.keys()
    print(f"select the product")
    for i in temp:
        print(f"{j}) {i}")
        j=j+1
    prd_index=int(input("select product list"))
    if prd_index>0 and prd_index<=j:
        print("please select ml")
        print('''1) 25ml
                2) 50ml
                3) 100ml
                4) 250ml
                5) 500ml
                ''')
        ml=int(input("select ml (1/2/3/4/5)"))
        inp=input("Whether you wanted to know the prices? Say (yes/no)")
        if inp.lower()=="yes":
            print(f"beauty products \n cosmetic name : {cosmetics_names[cosmetics_name]}")
            print(f" produdct iname is {temp} and index is {prd_index}")
            print(f" product is {temp[prd_index-1]}")
            temp=temp[prd_index-1]
            print(f"product price :{res[temp]}")
        

    else:
        print("non_valid")
else:
    print(f"please select a valid product")