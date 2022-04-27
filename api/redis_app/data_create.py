from redis_app.models import TableA, TableB, TableC, TableD, TableE
import random
import string


def random_token_creator(size = 64):
    return "".join(random.choice(string.ascii_letters + string.digits) for x in range(size))


def create_tables(size = 1000):
    if size < 1000:
        size = 1000
        
    for obja in range(size):
        TableA.objects.create(a_str = random_token_creator(), a_bool = random.choice([True, False]), a_int = int(random.random() * 1000000000))

    for objb in range(size):
        print("table b ")
        print(objb)
        a_obj = TableA.objects.all().order_by("?").first()
        for f_obj_a in range(10):
            TableB.objects.create(b_str = random_token_creator(), b_bool = random.choice([True, False]), b_int = int(random.random() * 1000000000), table_a = a_obj)
    
    for objc in range(size):
        print("table c ")
        print(objc)
        b_obj = TableB.objects.all().order_by("?").first()
        for f_obj_b in range(10):
            TableC.objects.create(c_str = random_token_creator(), c_bool = random.choice([True, False]), c_int = int(random.random() * 1000000000), table_b = b_obj)
    
    for objd in range(size):
        print("table d ")
        print(objd)
        c_obj = TableC.objects.all().order_by("?").first()
        for f_obj_c in range(10):
            TableD.objects.create(d_str = random_token_creator(), d_bool = random.choice([True, False]), d_int = int(random.random() * 1000000000), table_c = c_obj)

    for obje in range(size):
        print("table e ")
        print(obje)
        d_obj = TableD.objects.all().order_by("?").first()
        for f_obj_d in range(10):
            TableE.objects.create(e_str = random_token_creator(), e_bool = random.choice([True, False]), e_int = int(random.random() * 1000000000), table_d = d_obj)