#kita mencari mata uang yang dipilih user

'''
1. Pembukaan 
'''
while True:
    print("SELAMAT DATANG DI PENGKONVERSI UANG KE RUPIAH per Tanggal 24 Agustus 2023 di Mode Pertama Pembuatan")
    input_jenisuang = input("Masukan Jenis Uang (Dollar, Euro, Bath, Riyal, Ringgit) : ")
    #kita mencari jumlah uang yang ingin di konverter
    input_banyaknya = int(input("Masukkan jumlah uang yang ingin di konversi(Tanpa tanda titik atau Koma) : "))
    #kita mengkalikan dengan converter rupiah

        #dollar
    if(input_jenisuang == "Dollar" or input_jenisuang == "dollar"):
        # Contoh nilai uang dalam format float dengan 2 angka desimal
        uang_rupiah_dollar = input_banyaknya * 15.246
        formatted_uang_rupiah = "{:.3f}".format(uang_rupiah_dollar)

        # Cetak hasil konversi
        print("Per Tanggal 24 Agustus 2023, Jumlah uang yang di konversi adalah Rp.", formatted_uang_rupiah)

        #euro
    elif(input_jenisuang == "Euro" or input_jenisuang == "euro"):
        # Contoh nilai uang dalam format float dengan 2 angka desimal
        uang_rupiah_euro = input_banyaknya * 16.551
        formatted_uang_rupiah2 = "{:.3f}".format(uang_rupiah_euro)

        # Cetak hasil konversi
        print("Per Tanggal 24 Agustus 2023, Jumlah uang yang di konversi adalah Rp.", formatted_uang_rupiah2)

        #Bath
    elif(input_jenisuang == "Bath" or input_jenisuang == "bath"):
    
        uang_rupiah_bath = input_banyaknya * 436
        formatted_uang_rupiah3 = "{:.3f}".format(uang_rupiah_bath)

        # Cetak hasil konversi
        print("Per Tanggal 24 Agustus 2023, Jumlah uang yang di konversi adalah Rp.", formatted_uang_rupiah3)

        #Riyal
    elif(input_jenisuang == "Riyal" or input_jenisuang == "riyal"):
        uang_rupiah_riyal = input_banyaknya * 4.065
        formatted_uang_rupiah4 = "{:.3f}".format(uang_rupiah_riyal)

        # Cetak hasil konversi
        print("Per Tanggal 24 Agustus 2023, Jumlah uang yang di konversi adalah Rp.", formatted_uang_rupiah4)
        
        #Ringgit
    elif(input_jenisuang == "Ringgit" or input_jenisuang == "ringgit"):
        uang_rupiah_ringgit = input_banyaknya * 3.283
        formatted_uang_rupiah5 = "{:.3f}".format(uang_rupiah_ringgit)

        # Cetak hasil konversi
        print("Per Tanggal 24 Agustus 2023, Jumlah uang yang di konversi adalah Rp.", formatted_uang_rupiah5)
    else:
        print("Maaf, jenis uang anda masih belum bisa di konversikan dalam mode pertama pembuatan, silahkan coba tulis ulang")



