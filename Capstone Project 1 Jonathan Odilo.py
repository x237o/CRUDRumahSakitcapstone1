import tabulate
import datetime

recordpatient = [{"NRM": "001-01-01", "Nama": "Budi Padidi", "Jenis Kelamin": "L", "Tanggal lahir":"18-03-1974", "Lama rawat": 5, "Klasifikasi penyakit":"Jantung", "Prosedur":"EKG"},{"NRM": "001-01-02", "Nama": "Dita Wati", "Jenis Kelamin": "P", "Tanggal lahir":"25-09-1991", "Lama rawat": 4, "Klasifikasi penyakit":"Obstetri Ginekologi", "Prosedur":"SC"}]

def cek_nrm(rm):
    urai_nrm=list(map(str, rm))
    nrm_komponen=rm.split("-")
    nrm_nomor=''.join(nrm_komponen)
    nrm_valid = True
    if (urai_nrm.count("-")!=2) or (nrm_nomor.isdigit() != 1):
        print("NRM tidak valid")
        nrm_valid = False
    return nrm_valid
    
def cek_tgl(tgl):
    try:
        datetime.datetime.strptime(tgl, "%d-%m-%Y")
        return True
    except ValueError:
        return False
    

def lihat_record():
    if len(recordpatient) == 0:
        print("Tidak ada pasien dalam sistem")
    else:
        print(tabulate.tabulate(recordpatient, headers="keys", tablefmt="grid"))

def lihat_record_search():
    cari = input("Cari berdasarkan item (NRM/nama/Tanggal Lahir/Lama rawat/Klasifikasi penyakit/Prosedur) :").lower()
    hasil_cari = []
    for pasien in recordpatient:
        if any(cari in str(value).lower() for value in pasien.values()):
            hasil_cari.append(pasien)
    
    if len(hasil_cari) >0:
        print(tabulate.tabulate(hasil_cari, headers="keys", tablefmt="grid"))
    else:
        print("Data tidak ditemukan")

def tambah_record():
    print("Masukkan pasien baru :")
    nrm = str(input("Masukkan nomor rekam medis (XXX-XX-XX) :"))
    if (cek_nrm(nrm) != 1):
        return
    nama = str(input("Masukkan nama pasien :")).title()
    JK = input("Masukkan Jenis Kelamin Pasien (L/P) :")
    JKiter = 0
    if (JK.lower() == "l"):
        JKiter +=1
    if (JK.lower() == "p"):
        JKiter +=1
    if JKiter == 0:
        print("Input Jenis kelamin tidak benar")
        return
    tanggal = str(input("Masukkan tanggal lahir (DD-MM-YYYY) :"))
    if cek_tgl(tanggal) == 0:
        print("Tanggal tidak valid")
        return
    admisi = input("Lama rawat (hari) :")
    if admisi.isdigit() != 1:
        print ("Masukkan lama rawat hari dalam bilangan bulat")
        return
    klas = input("Klasifikasi penyakit :")
    pros = input("Masukkan prosedur pada pasien :")
    simpan = input ("Apakah yakin data akan disimpan (Y/N)? ")
    while (simpan.lower() != "y") and (simpan.lower() != "n"):
        simpan = input ("Apakah yakin data akan disimpan (Y/N)? ")
    
    if simpan =="y":
        pasien = {"NRM": nrm, "Nama": nama, "Jenis Kelamin": JK.upper(), "Tanggal lahir":tanggal, "Lama rawat": int(admisi), "Klasifikasi penyakit":klas, "Prosedur":pros}
        recordpatient.append(pasien)
        print("Data pasien sudah ditambahkan ke dalam database")
    else:
        return
    
def ubah_record():
    ubahan = input("Masukkan Nomor Rekam Medis pasien yang akan diubah :")
    if (cek_nrm(ubahan)):
        for pasien in recordpatient:
            if pasien["NRM"]==ubahan:
                print("Pasien ditemukan. Silahkan edit data yang diinginkan. Jika kategori tidak diupdate, silahkan langsung tekan enter")
                nama_update = input(f"Nama {pasien["Nama"]} ->") or pasien["Nama"]
                JK_update = input(f"Jenis kelamin {pasien["Jenis Kelamin"]} ->") or pasien["Jenis Kelamin"]
                TL_update = input (f"Tanggal lahir {pasien["Tanggal lahir"]} ->") or pasien["Tanggal lahir"]
                admisi_update = input (f"Lama rawat {pasien["Lama rawat"]} ->") or pasien["Lama rawat"]
                klas_update = input (f"Klasifikasi penyakit {pasien["Klasifikasi penyakit"]} ->") or pasien["Klasifikasi penyakit"]
                pros_update = input (f"Prosedur {pasien["Prosedur"]} ->") or pasien["Prosedur"]

                if TL_update and not cek_tgl(TL_update):
                    print("Format tanggal salah")
                    return
                
                pasien.update({"Nama": nama_update, "Jenis Kelamin": JK_update.upper(), "Tanggal lahir":TL_update, "Lama rawat": int(admisi_update), "Klasifikasi penyakit":klas_update, "Prosedur":pros_update})
                print("Database ter-update")
                return
        print("Pasien tidak ditemukan")


def delete_record():
    nrm_delete = input("Masukkan Nomor Rekam Medis pasien yang akan diubah :")
    global recordpatient
    nrm_checker = False
    if any(pasien["NRM"] == nrm_delete for pasien in recordpatient):
        nrm_checker = True

    if (cek_nrm(nrm_delete)):
        recordpatient = [p for p in recordpatient if p["NRM"] != nrm_delete]
        if nrm_checker == True:
            print(f"Data pasien dengan NRM {nrm_delete} sudah dihapus")
        else:
            print("NRM tidak ditemukan")
    else:
        return


def mainmenu():
    while True:
        try:
            print("========Data Pasien RS AXY========")
            print("1. Report Data Pasien")
            print("2. Tambah Data Pasien")
            print("3. Ubah Data Pasien")
            print("4. Hapus Data Pasien")
            print("5. Exit")

            pilihmenu = int(input("Pilih menu [1-5]: "))
            if pilihmenu == 1:
                while True:
                    try:
                        print("1. Report Data Seluruh Pasien")
                        print("2. Report Data Pasien Tertentu")
                        print("3. Kembali ke menu awal")
                        pilihsubmenu = int(input("Pilih submenu Report data pasien [1-3]: "))
                        if pilihsubmenu == 1:
                            lihat_record()
                            break
                        elif pilihsubmenu == 2:
                            lihat_record_search()
                            break
                        elif pilihsubmenu == 3:
                            break
                    except ValueError:
                        print("Pilih submenu menggunakan angka yang valid \n")
            elif pilihmenu == 2:
                while True:
                    try:
                        print("1. Tambah Data Pasien")
                        print("2. Kembali ke menu awal")
                        pilihsubmenu = int(input("Pilih submenu Tambah data pasien [1-2]: "))
                        if pilihsubmenu == 1:
                            tambah_record()
                            break
                        elif pilihsubmenu == 2:
                            break
                    except ValueError:
                        print("Pilih submenu menggunakan angka yang valid \n")
            elif pilihmenu == 3:
                while True:
                    try:
                        print("1. Ubah Data Pasien")
                        print("2. Kembali ke menu awal")
                        pilihsubmenu = int(input("Pilih submenu Ubah data pasien [1-2]: "))
                        if pilihsubmenu == 1:
                            ubah_record()
                            break
                        elif pilihsubmenu == 2:
                            break
                    except ValueError:
                        print("Pilih submenu menggunakan angka yang valid \n")
            elif pilihmenu == 4:
                while True:
                    try:
                        print("1. Hapus Data Pasien")
                        print("2. Kembali ke menu awal")
                        pilihsubmenu = int(input("Pilih submenu Hapus data pasien [1-2]: "))
                        if pilihsubmenu == 1:
                            delete_record()
                            break
                        elif pilihsubmenu == 2:
                            break
                    except ValueError:
                        print("Pilih submenu menggunakan angka yang valid \n")
            elif pilihmenu == 5:
                print ("Exit program")
                break
        except ValueError:
            print("Pilih menu yang valid \n")

if __name__ == "__main__":
    mainmenu()
