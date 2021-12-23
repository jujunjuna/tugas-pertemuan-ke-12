data={}
class daftarNilai():
    
    def tambah(self):
        print('\nTambah Data Mahasiswa')
        nama= input("Masukkan Nama\t\t: ")                                        
        nim= input("Masukkan NIM\t\t: ")                                         
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                              
        nilaiUts= int(input("Masukkan Nilai UTS\t: "))                                   
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))                                    
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        data[nama]=nim,nilaiTugas,nilaiUts,nilaiUas,nilaiAkhir,
        
        
        

    def ubah(self):
        print('\nMengubah Data Mahasiswa')
        nama = input("Masukkan Nama: ")                                                         
        if nama in data.keys():                              
            nim= input("Masukkan NIM Baru\t: ")                              
            nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                           
            nilaiUts= int(input("Masukkan Nilai UTS\t: "))                           
            nilaiUas= int(input("Masukkan Nilai UAS\t: "))                           
            nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)          
            data[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                      
            print("\nData Berhasil Di Update!\n")
        else:                                                                                    
            print("Data tidak ditemukan!\n")

    def hapus(self):
        print('\nmenghapus data')
        nama = input("Masukkan Nama:  ")                                                        
        if nama in data.keys():                                                              
            del data[nama]                                                                   
            print("Data Telah Dihapus!\n")
        else:
            print("Data Mahasiswa Tidak Ada\n")

    def lihat(self):
        if data.items():                                                                     
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================\n")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================\n")

    def keluar(self):
        print('\n=====terimakasih=====\n')
        print(21*'=')
        print("Nama\t: Jujun Junaedi\nKelas\t: TI.21.C5\nNIM\t: 312110568")
        print(21*'=')             
                
                                                        
while True:
    x = daftarNilai()
    print('tambah\nubah\nlihat\nhapus\nkeluar')                                                                                     
    c = input("\nsilahkan masukan pilihan : ")

    if (c== 'tambah'):
        x.tambah()
    elif (c=="ubah"):
        x.ubah()
    elif (c=="lihat"):
        x.lihat()
    elif (c=="hapus"):
        x.hapus()
    elif (c== 'keluar'):
        x.keluar()
        break
    else:
        print('masukan pilihan dengan benar')