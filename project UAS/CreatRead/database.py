import datetime as dt

database = "database.txt"

template = {
    "tanggal" : "XXXX-XX-XX",
    "sales_produk"    : "XXXX",
    "sales_harga"       : "XXXX",
}

hari_ini = str(dt.date.today())

def update_database(data_add):
    with open(database,"a",encoding="utf-8") as file :
        file.write(data_add)

def data_for_database(sales_produk,sales_harga):

    data = template.copy()

    data["tanggal"] = hari_ini
    data["sales_produk"] = sales_produk
    data["sales_harga"] = sales_harga 

    data_add = f"{data['tanggal']},{data['sales_produk']},{data['sales_harga']},\n"
    update_database(data_add)
    
    
def read_database(tanggal):
    with open(database,"r",encoding="utf-8") as file :
        total_sales_produk = 0
        total_sales_harga = 0

        data = file.readlines()
        for index,data in enumerate(data):
            data_break = data.split(",")
            if data_break[0] == tanggal :
                total_sales_produk += int(data_break[1])
                total_sales_harga += int(data_break[2])     

        return [tanggal,total_sales_produk,total_sales_harga]


def read_history(tanggal):
    data  =read_database(tanggal)

    print(f"\nHistory Penjualan\n ")
    print(f"Tanggal                : {data[0]}  " )
    print(f"Total penjualan Produk : {data[1]} pcs  " )
    print(f"Sales Penjualan produk : Rp.{data[2]} " )

