import os
from .  import operasi 
from . import database 
from . import waktu

def header():
    os.system("cls")
    print("="*80)
    print(f"{'CEKET.IN':^80}")
    print(f"{'#YSSA Yang Simple Simple Ajah':^80}")
    print("-"*80)
    print(f"{waktu.time_header():^80}")

def footer():
    print("="*80)
    print("-"*80)


class Menu():
    
    def menu():
        header()
        print("""
            -----------------------------------------------------
            |        Nama Minuman         |        Harga        |
            |---------------------------------------------------|
            | 1.Jelly milk strawberry     |       Rp.5000       |
            | 2.Jelly milk permen karet   |       Rp.5000       |
            | 3.Jelly milk coklat         |       Rp.5000       |
            | 4.es kopiko                 |       Rp.8000       |
            | 5.es kopi blaster           |       Rp.8000       |
            | 6.es rainbow                |       Rp.10000      |
            -----------------------------------------------------
    """)

    def struk(nama,banyak,list_harga,qty,list_total,list_order,sales_produk) :
        print(f"\npesanan atas nama sdr/i {nama}")
        print("="*80)
        print(f"{' NO':^3} | {'PESANAN':^25} | {'HARGA SATUAN':^15} | {'BANYAK PESAN':^10} | {'HARGA TOTAL':^10} |")
        print("-"*80)
        for x in range(banyak) :
            produk = operasi.Operasi.list_produk(list_order[x])
            print(f"{x+1:^3} | {produk :^25} | {list_harga[list_order[x]-1]:^15} | {qty[x]:^12} | {list_total[x]:^11} |")
        print("="*80)

        total_bayar = 0
        for x in list_total :
            total_bayar += x

        tagihan = f"Total bayar Rp.{total_bayar}"
        print(f"\n{tagihan:^80}")
        bayar = int(input("\t\t\t    Uang bayar : Rp."))

        operasi.Operasi.payment(total_bayar,bayar)
        
        input("\nEnter untuk kembali ke menu.....")
        database.data_for_database(sales_produk,total_bayar)


    def history_jual():
        header()
        print(f"\n{'== HISTORY PENJUALAN ==':^80}\n")
        print(f"{'Silahkan pilih opsi':^80}\n")
        print(f"{'1.HARI INI':^80}\n")
        print(f"{'2.HARI LAIN':^80}\n")
        footer()

        tanggal = operasi.Operasi.input_history()
        header()
        if tanggal :
            database.read_history(tanggal)
            input("\nEnter untuk Kembali...")
        else:
            print("Kode yang dimasukan salah")

    def menu_utama():
        print(f"\n{'== MENU UTAMA ==':^80}\n")
        print(f"{'Silahkan pilih opsi':^80}\n")
        print(f"{'1.KASIR':^80}\n")
        print(f"{'2.HISTORY PENJUALAN':^80}\n")
        print(f"{'0.Keluar':^80}")

    def tutup():
        while True :
            print(f"\n\n{'TOKO SEDANG TUTUP':^80}\n\n")
            print(f"{'Jam operasional toko':^80}")
            print(f"{'09-00 sampai 16.00 WIB':^80}")

            input("\n\nEnter untuk melanjutkan.....")
            header()

            print(f"\n{'Silahkan pilih opsi':^80}\n")
            print(f"{'1.HISTORY PENJUALAN':^80}")
            print(f"{'0.KELUAR':^80}\n")
            footer()

            is_input = input("\nMasukan opsi 1/0: ")
            if is_input == "1" :
                hasil = Menu.history_jual()
                header()
                print(f"{'TERIMA KASIH TELAH MENGGUNAKAN APLIKASI CEKET.IN':^80}\n")

            elif is_input == "0" :
                header()
                print(f"\n{'TERIMA KASIH TELAH MENGGUNAKAN APLIKASI CEKET.IN':^80}\n")
                footer()
                break

            else :
                header()
                print("KODE YANG DIMASUKAN SALAH")

    def buka():
        print(f"{'SELAMAT DATANG':^80}")
        while True :
            header()
            Menu.menu_utama()
            footer()
            is_input = input("Masukan opsi 1/2/0 : ")
            
            if is_input == "1" :
                header()
                operasi.Operasi.input_order()

            elif is_input == "2" :
                header()
                Menu.history_jual()
                
            elif is_input == "0" :
                header()
                print(f"\n{'TERIMA KASIH TELAH MENGGUNAKAN APLIKASI CEKET.IN':^80}\n")
                footer()
                break
            
            else :
                desain.header()
                print(f"\n{'KODE YANG DIMASUKAN SALAH':^80}\n")
                input("\n\nEnter untuk kembali.....")







