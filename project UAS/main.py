from CreatRead import operasi,desain,Menu,database,waktu


if __name__ == "__main__" :
    desain.header()
    jam_operasi = waktu.jam_kerja()

    if jam_operasi == False :

        desain.Menu.tutup()
    
    else :
        desain.Menu.buka()

            
            


        