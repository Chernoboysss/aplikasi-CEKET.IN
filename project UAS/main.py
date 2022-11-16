import os
from CreatRead import operasi,desain,Menu,database,waktu


if __name__ == "__main__" :
    os.system("cls")
    desain.header()
    jam_operasi = waktu.jam_kerja()
    if jam_operasi == False :
        print(f"\n\n{'TOKO SEDANG TUTUP':^80}\n")
        input("\n\nEnter untuk melanjujtkan.....")
        desain.header()

        print(f"\n{'Silahkan pilih opsi':^80}\n")
        print(f"{'1.HISTORY PENJUALAN':^80}")
        print(f"{'0.KELUAR':^80}\n")
        desain.footer()

        is_input = input("\nMasukan opsi 1/0: ")
        if is_input == "1" :
            hasil = desain.Menu.History_jual()
            desain.header()
            print(f"{'TERIMA KASIH TELAH MENGGUNAKAN APLIKASI CEKET.IN':^80}\n")


        elif is_input == "0" :
            desain.header()
            print(f"{'TERIMA KASIH TELAH MENGGUNAKAN APLIKASI CEKET.IN':^80}\n")

        else :
            desain.header()
            print("kode yang dimasukan salah")
    
    
    else :
        print(f"{'SELAMAT DATANG':^80}")

        while True :
            desain.header()
            print(f"\n{'== MENU UTAMA ==':^80}\n")
            print(f"{'Silahkan pilih opsi':^80}\n")
            print(f"{'1.KASIR':^80}\n")
            print(f"{'2.HISTORY PENJUALAN':^80}\n")
            print(f"{'0.Keluar':^80}")

            desain.footer()
            is_input = input("Masukan opsi 1/2/0 : ")
            
            if is_input == "1" :
                desain.header()
                operasi.Operasi.input_order()

            elif is_input == "2" :
                desain.header()
                desain.Menu.History_jual()
                
            elif is_input == "0" :
                break



        