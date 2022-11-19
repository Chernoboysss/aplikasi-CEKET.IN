from . import desain
from . import database

class Operasi():

    def list_produk(index):
        list_minuman = ["Jelly milk strawberry","Jelly milk permen karet","Jelly milk coklat","es kopiko","es kopi blaster","es rainbow"]
        return list_minuman[index-1]

    def input_order():
        list_order = []
        list_harga   = [5000,5000,5000,8000,8000,10000]
        list_total = []
        qty = []
        sales_produk = 0

        nama_pembeli = input("Orderan atas Nama : ")
        banyak = int(input("Banyak pesanan \t  : "))

        for x in range(banyak):
            desain.Menu.menu()
            print(f"Pesanan ke - {x+1}")
            is_order = int(input("Silahkan pilih Menu [1/2/3/4/5/6/] : "))
            is_banyak = int(input("banyak pesan \t\t\t   : "))
            list_order.append(is_order)
            list_total.append(is_banyak * list_harga[is_order-1])
            qty.append(is_banyak)
            sales_produk += is_banyak

        desain.header()
        desain.Menu.struk(nama_pembeli,banyak,list_harga,qty,list_total,list_order,sales_produk)
  
    def payment(total_bayar,bayar):
        print("\npembayaran")
        print("-"*28)
        kembalian = bayar - total_bayar
        print(f"Total bayar \t: Rp.{total_bayar}")
        print(f"Uang bayar \t: Rp.{bayar}")
        print("-"*28)
        print(f"Uang kembalian \t: Rp.{kembalian}")

    def input_history():
        is_pilih = input("silahkan pilih opsi : ")
        if is_pilih == "1":
            return database.hari_ini

        elif is_pilih == "2" :
            desain.header()
            print("\nSilahkan isi format tanggal ")
            tahun   = input("Tahun   : ")
            bulan   = input("Bulan   : ")
            tanggal = input("tanggal : ")

            return f"{tahun}-{bulan}-{tanggal}"

        elif is_pilih == "0" :
            return False

        else :
            print("input yang di masukan salah !!!")





