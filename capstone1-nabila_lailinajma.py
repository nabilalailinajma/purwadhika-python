from prettytable import PrettyTable
from datetime import datetime
from datetime import timedelta
import sys

kendaraan = [
    {
        "plat": "B 0106 LOV",
        "jenis": "Motor",
        "merek": "Beat",
        "status_pajak": True,
        "masa_berlaku": "2024-11-13",
        "harga_pajak": 500000,
    },
    {
        "plat": "BE 0726 MLU",
        "jenis": "Motor",
        "merek": "Ninja",
        "status_pajak": False,
        "masa_berlaku": "2023-01-23",
        "harga_pajak": 1350000,
    },
    {
        "plat": "D 2456 FX",
        "jenis": "Mobil",
        "merek": "Avanza",
        "status_pajak": True,
        "masa_berlaku": "2025-12-20",
        "harga_pajak": 1200000,
    },
    {
        "plat": "DE 8262 FG",
        "jenis": "Mobil",
        "merek": "Pajero Sport",
        "status_pajak": False,
        "masa_berlaku": "2022-12-20",
        "harga_pajak": 4250000,
    },
    {
        "plat": "Y 0282 NAB",
        "jenis": "Yacht",
        "merek": "Lurssen",
        "status_pajak": False,
        "masa_berlaku": "2017-10-03",
        "harga_pajak": 12200000,
    },
    {
        "plat": "A 9876 ZYX",
        "jenis": "Pesawat",
        "merek": "Boeing 77",
        "status_pajak": True,
        "masa_berlaku": "2030-12-25",
        "harga_pajak": 21550000,
    },
    {
        "plat": "F 1123 ABC",
        "jenis": "Kapal Laut",
        "merek": "Titanic",
        "status_pajak": True,
        "masa_berlaku": "2035-12-12",
        "harga_pajak": 15200000,
    },
    {
        "plat": "G 2211 RRT",
        "jenis": "Roket",
        "merek": "SpaceX",
        "status_pajak": True,
        "masa_berlaku": "2050-01-01",
        "harga_pajak": 78700000,
    }
]

penyewaan=[]

header_kendaraan = ["Plat", "Jenis", "Merek", "Status Pajak", "Masa Berlaku", "Harga Pajak"]
header_penyewaan = ["Plat", "Jenis", "Merek", "Nama Penyewa", "Tanggal Sewa", "Tanggal Kembali"]

# HELPER START
def validate_plat(): #Validasi apakah format plat sudah sesuai atau belum
  while True:
    plat = input("Masukkan plat kendaraan (Ketik 'Y' untuk menampilkan ketentuan plat): ").upper()
    plat_list = plat.split(" ")

    error_message = "Format salah. Pastikan plat memiliki format 'B 1234 ABC'."
    
    if (plat == 'Y'):
        print("Ketentuan plat kendaraan:\n")
        print("1. Kendaraan terdiri dari tiga bagian yang dipisahkan oleh spasi (Contoh: 'B 1234 ABC')")
        print("2. Bagian pertama terdiri dari 1 s/d 2 huruf")
        print("3. Bagian kedua terdiri dari 1 s/d 4 digit angka")
        print("4. Bagian ketida terdiri dari 1 s/d 3 huruf\n")
        continue
    
    if len(plat_list) != 3: # Cek apakah plat memiliki tepat 3 bagian
      print(error_message)
      continue

    if not (plat_list[0].isalpha() and 1 <= len(plat_list[0]) <= 2): # Validasi bagian pertama (1-2 karakter alfabet)
      print(error_message)
      continue

    if not (plat_list[1].isdigit() and 1 <= len(plat_list[1]) <= 4):# Validasi bagian kedua (1-4 digit angka)
      print(error_message)
      continue

    if not (plat_list[2].isalpha() and 1 <= len(plat_list[2]) <= 3): # Validasi bagian ketiga (1-3 karakter alfabet)
      print(error_message)
      continue

    return plat

def validate_masa_berlaku():
  while True:
    masa_berlaku = input("Masukkan masa berlaku baru (format: 'YYYY-MM-DD'): ")
    try:
        datetime.strptime(masa_berlaku, "%Y-%m-%d") # Coba parsing input ke format tanggal
        return masa_berlaku

    except ValueError:
      print("Format salah. Pastikan masa berlaku memiliki format 'YYYY-MM-DD'.")
      continue # Jika parsing gagal, format tidak sesuai

def validate_tanggal():
  while True:
    try:
        tanggal = int(input("Masukkan tanggal yang ingin dicek (1-31): "))
        if 1 <= tanggal <= 31:
          return tanggal
        else:
          print("Tanggal tidak valid! Masukkan angka antara 1-31.")
    except ValueError:
      print("Input tidak valid! Masukkan angka.")

def lanjutkan(konfirmasi):
  while True:
    validasi = input(konfirmasi + " (Y/N): ").upper()

    if validasi == "Y":
        return True
    
    elif validasi =='N':
        return False
    
    else:
        print("Pilihan Tidak Valid.")

def tampilkan_kendaraan(data): #Pretty Table untuk menampilkan data
  table = PrettyTable() # Membuat objek PrettyTable

  table.field_names = header_kendaraan # Menambahkan kolom header berdasarkan kunci dalam data

  for kendaraan in data:
      table.add_row(kendaraan.values()) # Menambahkan setiap baris data ke tabel

  print(table) # Menampilkan tabel

def tampilkan_penyewaan(data):
    if not penyewaan:
        print("\nTidak ada kendaraan yang sedang disewa.")
    else:
        table = PrettyTable()
        table.field_names = header_penyewaan
        for sewa in data:
            table.add_row(sewa.values())
        print("\nBerikut adalah Kendaraan yang telah disewa")
        print(table)

def check_status_pajak(masa_berlaku):
  today = datetime.now().strftime("%Y-%m-%d") #Get tanggal sekarang pake format YYYY-MM-DD

  if(masa_berlaku > today ): #Cek apakah hari ini udah lewat dari masa berlaku
    return True #Masih aktif

  else:
    return False #Sudah tidak aktif

def plat_exist(plat): #Check apakah PLAT sudah ada di sistem atau belum
    if any(data["plat"] == plat for data in kendaraan):
        return True
    else:
        return False

def cari_kendaraan(plat_cari, data = kendaraan):
    for item in data:
        if item["plat"] == plat_cari: # Mencari kendaraan berdasarkan plat
            return item  # Mengembalikan data jika ditemukan

    print("Kendaraan dengan plat tersebut tidak ditemukan.")
    return None  # Jika plat tidak ditemukan
    

def cari_penyewaan(plat_cari):
    for data in penyewaan:
        if data["plat"] == plat_cari: # Mencari kendaraan berdasarkan plat
            return data  # Mengembalikan data jika ditemukan

    print("Kendaraan dengan plat tersebut tidak ditemukan")
    return None  # Jika plat tidak ditemukan

def kendaraan_tersedia():
    kendaraan_disewa = []
    for sewa in penyewaan:
        kendaraan_disewa.append(sewa["plat"])

    kendaraan_hidup = cari_kendaraan_hidup()
    
    kendaraan_tidak_disewa = []
    for item in kendaraan_hidup:
        if item["plat"] not in kendaraan_disewa:
            kendaraan_tidak_disewa.append(item)

    return kendaraan_tidak_disewa

# HELPER END

def get_kendaraan(): # menu 1a, menampilkan semua jenis kendaraan
    if not kendaraan:
        print("Tidak ada data kendaraan.")
    else:
        tampilkan_kendaraan(kendaraan)

def get_kendaraan_by_plat():
  while True:
    plat = validate_plat()

    kendaraan = cari_kendaraan(plat)
    if not kendaraan:
      if not lanjutkan("Apakah Anda masih ingin mencari kendaraan lainnya?"):
        break
      else:
        continue

    else:
      print("\nBerikut adalah data kendaraan yang Anda cari")
      tampilkan_kendaraan([kendaraan])
      if not lanjutkan("Apakah Anda masih ingin mencari kendaraan lainnya?"):
        break

def cari_kendaraan_hidup():
    return list(filter(lambda x: x['status_pajak'] == True, kendaraan))

def cari_kendaraan_mati():
    return list(filter(lambda x: x['status_pajak'] == False, kendaraan))

def get_kendaraan_by_status_pajak():
  while True:
    status_pajak = input("Masukkan status pajak 'Mati' atau 'Hidup': ")

    if status_pajak.capitalize() == "Mati": # Filter kendaraan berdasarkan status ganjil
      print("\nBerikut adalah Daftar Kendaraan dengan Pajak Mati")
      get_kendaraan = cari_kendaraan_mati()

    elif status_pajak.capitalize() == "Hidup": # Filter kendaraan berdasarkan status genap
      print("\nBerikut adalah Daftar Kendaraan dengan Pajak Hidup")
      get_kendaraan = cari_kendaraan_hidup()

    else:
      print("Pilihan tidak valid. Masukkan 'Mati' atau 'Hidup'.")
      continue

    # Tampilkan hasil
    if not get_kendaraan:
      print("Tidak ada kendaraan dengan status pajak", status_pajak)

    else:
      tampilkan_kendaraan(get_kendaraan)

    if not lanjutkan("Apakah Anda ingin mencari berdasarkan status pajak?"):
      break

def get_kendaraan_by_jenis():
  while True:
    jenis_kendaraan = input("Masukkan jenis kendaraan: ")

    get_kendaraan = list(filter(lambda x: x['jenis'].upper() == jenis_kendaraan.upper(), kendaraan))

    # Tampilkan hasil
    if not get_kendaraan:
      print("Tidak ada kendaraan dengan jenis", jenis_kendaraan)

    else:
      print("\nBerikut adalah daftar kendaraan dengan jenis", jenis_kendaraan)
      tampilkan_kendaraan(get_kendaraan)

    if not lanjutkan("Apakah Anda masih ingin mencari berdasarkan jenis kendaraan?"):
      break

def cek_gangen_by_input():
  while True:
    tanggal = validate_tanggal()

    if tanggal % 2 == 0:
      filter_jenis = "Genap"
      get_kendaraan = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 == 0, kendaraan))

    else:
      filter_jenis = "Ganjil"
      get_kendaraan = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 != 0, kendaraan))

    print(f"\nTanggal {tanggal} adalah tanggal {filter_jenis}.")

    # Tampilkan hasil
    if not get_kendaraan:
      print(f"Tidak ada kendaraan dengan plat {filter_jenis}")

    else:
      print(f"\nDaftar kendaraan dengan plat {filter_jenis}:")
      tampilkan_kendaraan(get_kendaraan)

    if not lanjutkan("Apakah Anda masih ingin mencari kendaraan berdasarkan ganjil genap?"):
      break

def cek_gangen_by_datetime():
    today = datetime.now()  # Mendapatkan tanggal hari ini
    print(f"\nTanggal hari ini: {today.strftime('%Y-%m-%d')}")

    # Memeriksa apakah tanggal hari ini ganjil atau genap
    if today.day % 2 == 0:
        print("Hari ini adalah tanggal Genap.")
        filter_jenis = "Genap"
    else:
        print("Hari ini adalah tanggal Ganjil.")
        filter_jenis = "Ganjil"

    # Memisahkan kendaraan berdasarkan plat ganjil/genap
    if filter_jenis == "Ganjil":
        kendaraan_filtered = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 != 0, kendaraan))
    else:
        kendaraan_filtered = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 == 0, kendaraan))

    # Menampilkan kendaraan yang sesuai dengan filter
    if kendaraan_filtered:
        print(f"\nDaftar kendaraan dengan plat {filter_jenis}:")
        tampilkan_kendaraan(kendaraan_filtered)
    else:
        print(f"Tidak ada kendaraan dengan plat {filter_jenis} hari ini.")

def cek_ganjil_genap_by_today():
    today = datetime.now()  # Mendapatkan tanggal hari ini
    print(f"\nTanggal hari ini: {today.strftime('%Y-%m-%d')}")

    # Memeriksa apakah tanggal hari ini ganjil atau genap
    if today.day % 2 == 0:
        filter_jenis = "Genap"
        kendaraan_filtered = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 == 0, kendaraan))
    else:
        filter_jenis = "Ganjil"
        kendaraan_filtered = list(filter(lambda x: int(x['plat'].split(" ")[1]) % 2 != 0, kendaraan))

    print(f"\nHari ini adalah tanggal {filter_jenis}:")

    # Menampilkan kendaraan yang sesuai dengan filter
    if kendaraan_filtered:
        print(f"\nDaftar kendaraan dengan plat {filter_jenis}:")
        tampilkan_kendaraan(kendaraan_filtered)
    else:
        print(f"Tidak ada kendaraan dengan plat {filter_jenis} hari ini.")

def cek_gangen():
        while True:
            try:
                print("\n|=============== Menu Cek Kendaraan program Ganjil-Genap =====================|")
                print("1. Cek Kendaraan berdasarkan Hari Ini")
                print("2. Cek Kendaraan berdasarkan Tanggal Input")
                print("3. Kembali ke Menu Lihat Daftar Kendaraan")
                print("|===========================================================|")

                pilihan = int(input("Pilih menu (1-3): "))

                if pilihan == 1:
                    cek_gangen_by_datetime()
                elif pilihan == 2:
                    cek_gangen_by_input()
                elif pilihan == 3:
                    menu_read()
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
            except ValueError:
                print("Pilihan tidak valid. Silakan pilih lagi.")

def bubble_sort_asc(field="harga_pajak"):
    data = kendaraan.copy()
    n = len(data)
    # Melakukan Bubble Sort
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][field] > data[j+1][field]:
                # Tukar posisi jika harga pajak data[j] lebih besar dari harga pajak data[j+1]
                data[j], data[j+1] = data[j+1], data[j]
                
    return data

def bubble_sort_desc(field="harga_pajak"):
    data = kendaraan.copy()
    n = len(data)
    # Melakukan Bubble Sort untuk urutan menurun (descending)
    for i in range(n):
        for j in range(0, n-i-1):
            # Jika harga pajak data[j] lebih kecil dari harga pajak data[j+1]
            if data[j][field] < data[j+1][field]:
                # Tukar posisi jika kondisi tersebut terpenuhi
                data[j], data[j+1] = data[j+1], data[j]
    
    return data

def get_pajak_terkecil(kendaraan):
    # Menginisialisasi kendaraan dengan pajak terkecil
    kendaraan_terkecil = kendaraan[0]  # Anggap kendaraan pertama sebagai yang pajaknya terkecil

    # Melakukan iterasi untuk membandingkan pajak kendaraan lainnya
    for kendaraan_item in kendaraan:
        if kendaraan_item["harga_pajak"] < kendaraan_terkecil["harga_pajak"]:
            kendaraan_terkecil = kendaraan_item  # Menyimpan kendaraan dengan pajak terkecil

    return kendaraan_terkecil

def get_pajak_terbesar(kendaraan):
    # Menginisialisasi kendaraan dengan pajak terbesar
    kendaraan_terbesar = kendaraan[0]  # Anggap kendaraan pertama sebagai yang pajaknya terbesar

    # Melakukan iterasi untuk membandingkan pajak kendaraan lainnya
    for kendaraan_item in kendaraan:
        if kendaraan_item["harga_pajak"] > kendaraan_terbesar["harga_pajak"]:
            kendaraan_terbesar = kendaraan_item  # Menyimpan kendaraan dengan pajak terbesar

    return kendaraan_terbesar

def get_biaya_pajak():
        while True:
            try:
                print("\n|=============== Menu Mencari Biaya Pajak ==================|")
                print("1. Tampilkan Biaya Pajak Terkecil")
                print("2. Tampilkan Biaya Pajak Terbesar")
                print("3. Urutkan Biaya Pajak dari yang Terkecil")
                print("4. Urutkan Biaya Pajak dari yang Terbesar")
                print("5. Kembali ke Menu Lihat Daftar Kendaraan")            
                print("|===========================================================|")

                pilihan = int(input("Pilih menu (1-5): "))

                if pilihan == 1:
                    kendaraan_terkecil = get_pajak_terkecil(kendaraan)
                    print("\nKendaraan dengan Pajak Terkecil:")
                    tampilkan_kendaraan([kendaraan_terkecil])  # Menampilkan kendaraan terkecil
                elif pilihan == 2:
                    kendaraan_terbesar = get_pajak_terbesar(kendaraan)
                    print("\nKendaraan dengan Pajak Terbesar:")
                    tampilkan_kendaraan([kendaraan_terbesar])  # Menampilkan kendaraan terbesar
                elif pilihan == 3:
                    print("\nKendaraan diurutkan berdasarkan Pajak Terkecil:")
                    tampilkan_kendaraan(bubble_sort_asc())  # Menampilkan kendaraan yang sudah diurutkan
                elif pilihan == 4:
                    print("\nKendaraan diurutkan berdasarkan Pajak Terbesar:")
                    tampilkan_kendaraan(bubble_sort_desc())  # Menampilkan kendaraan yang sudah diurutkan
                elif pilihan == 5:
                    menu_read()
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
            except ValueError:
                print("Pilihan tidak valid. Silakan pilih lagi.")

def menu_read():
    while True:
        try:
            print("\n|=============== Menu Lihat Daftar Kendaraan ===============|")
            print("1. Menampilkan Semua Kendaraan")
            print("2. Mencari Kendaraan berdasarkan Plat")
            print("3. Mencari kendaraan berdasarkan Jenis")
            print("4. Mencari Kendaraan berdasarkan Status Pajak")
            print("5. Mengecek Ketersediaan Kendaraan jika Ganjil-Genap")
            print("6. Mencari Biaya Pajak")
            print("7. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-7): "))

            if pilihan == 1:
                print("\nBerikut adalah daftar semua kendaraan")
                get_kendaraan()
            elif pilihan == 2:
                get_kendaraan_by_plat()
            elif pilihan == 3:
                get_kendaraan_by_jenis()
            elif pilihan == 4:
                get_kendaraan_by_status_pajak()
            elif pilihan == 5:
                cek_gangen()
            elif pilihan == 6:
                get_biaya_pajak()
            elif pilihan == 7:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")

        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def add_kendaraan():
    while True:
        plat = validate_plat()

        # Check if plat already exists
        if plat_exist(plat):
            print("Kendaraan Anda sudah terdaftar.")
            continue

        # Prompt for other details if plat is valid
        jenis = input("Masukkan jenis kendaraan (misalnya: motor/mobil): ").capitalize()
        merek = input("Masukkan merek kendaraan: ").capitalize()

        masa_berlaku = validate_masa_berlaku()

        harga_pajak = int(input("Masukkan harga pajak: "))

        new_data = {
            "plat": plat,
            "jenis": jenis,
            "merek": merek,
            "status_pajak" : check_status_pajak(masa_berlaku),
            "masa_berlaku": masa_berlaku,
            "harga_pajak": harga_pajak,
        }

        tampilkan_kendaraan([new_data])
        validasi = input("Apakah Anda yakin ingin menambahkan data ini? (Y/N):").upper()

        if(validasi == "Y"):
          kendaraan.append(new_data)

          print("Data kendaraan berhasil ditambahkan.")
          if not lanjutkan("Apakah Anda ingin menambahkan data kendaraan lainnya?"):
            break
        else:
          if not lanjutkan("Apakah Anda masih ingin menambahkan data kendaraan?"):
            break

def menu_create():
    while True:
        try:
            print("\n|=============== Menu Tambah Kendaraan =====================|")
            print("1. Tambah Data Kendaraan")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = input("Pilih menu (1-2): ")

            if pilihan == "1":
                add_kendaraan()
            elif pilihan == "2":
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def update_kendaraan():
    while True:
        tampilkan_kendaraan(kendaraan)
        plat = validate_plat()

        kendaraan_data = cari_kendaraan(plat)

        if kendaraan_data is None:
            print("Kendaraan dengan plat tersebut tidak ditemukan.")
            if not lanjutkan("Apakah Anda ingin mencari plat lainnya?"):
                break
            else:
                continue

        # Menampilkan data kendaraan yang akan diubah
        print("\nData kendaraan yang akan diubah:")
        tampilkan_kendaraan([kendaraan_data])

        # Meminta konfirmasi untuk update
        if not lanjutkan("Apakah Anda yakin ingin mengubah data kendaraan ini?"):
            if not lanjutkan("Apakah Anda ingin mencoba mengubah kendaraan lain?"):
                break
            else:
                continue

        while True:
            # Memilih kolom yang ingin diubah
            print("\n|===============Pilih data yang ingin diubah:===============|")
            print("1. Jenis kendaraan")
            print("2. Merek kendaraan")
            print("3. Masa berlaku")
            print("4. Harga pajak")
            print("5. Kembali")
            print("|==============================================================|")

            pilihan = int(input("Pilih nomor (1-6): "))

            if pilihan == 1:
                jenis = input("Masukkan jenis kendaraan baru (misalnya: motor/mobil): ").capitalize()
                kendaraan_data["jenis"] = jenis

            elif pilihan == 2:
                merek = input("Masukkan merek kendaraan baru: ").capitalize()
                kendaraan_data["merek"] = merek

            elif pilihan == 3:
                masa_berlaku = validate_masa_berlaku()
                kendaraan_data["masa_berlaku"] = masa_berlaku
                kendaraan_data["status_pajak"] = check_status_pajak(masa_berlaku)

            elif pilihan == 4:
                harga_pajak = int(input("Masukkan harga pajak baru: "))
                kendaraan_data["harga_pajak"] = harga_pajak

            elif pilihan == 5:
                print("Kembali ke pilih kendaraan.")
                break

            else:
                print("Pilihan tidak valid, silakan pilih lagi.")
                continue

            # Menampilkan data kendaraan yang sudah diperbarui
            print("\nData kendaraan yang telah diperbarui:")
            tampilkan_kendaraan([kendaraan_data])

            if not lanjutkan(f"Apakah Anda ingin mengubah detail lain dari kendaraan ini?"):
                break

        if not lanjutkan("Apakah Anda ingin mengubah data kendaraan lainnya?"):
            break
                 
def menu_update():
    while True:
        try:
            print("\n|=============== Menu Update Kendaraan =====================|")
            print("1. Ubah Data Kendaraan")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-2): "))

            if pilihan == 1:
                update_kendaraan()
            elif pilihan == 2:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def hapus_kendaraan():
    while True:
        tampilkan_kendaraan(kendaraan)
        plat = validate_plat()

        kendaraan_data = cari_kendaraan(plat)
        if kendaraan_data is None:
            print("Kendaraan dengan plat tersebut tidak ditemukan.")
            if not lanjutkan("Apakah Anda ingin mencari plat lainnya?"):
                break
            else:
                continue

        # Menampilkan data kendaraan yang akan dihapus
        print("\nData kendaraan yang akan dihapus:")
        tampilkan_kendaraan([kendaraan_data])

        # Meminta konfirmasi untuk menghapus
        if not lanjutkan("Apakah Anda yakin ingin menghapus data kendaraan ini?"):
            if not lanjutkan("Apakah Anda ingin mencoba menghapus kendaraan lain?"):
                break
            else:
                continue

        # Menghapus kendaraan dari daftar
        kendaraan.remove(kendaraan_data)
        print(f"Kendaraan dengan plat {plat} telah dihapus.")

        if not lanjutkan("Apakah Anda ingin menghapus kendaraan lainnya?"):
            break

def menu_delete():
    while True:
        try:
            print("\n|=============== Menu Hapus Kendaraan =====================|")
            print("1. Hapus Data Kendaraan")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-2): "))

            if pilihan == 1:
                hapus_kendaraan()
            elif pilihan == 2:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
                print("Pilihan tidak valid. Silakan pilih lagi.")

def is_kendaraan_disewa(plat):
    return any(sewa['plat'] == plat for sewa in penyewaan)

def sewa_kendaraan():
    print("\nData kendaraan yang tersedia untuk disewa:")
    tampilkan_kendaraan(kendaraan_tersedia())
    plat = validate_plat()
    if plat_exist(plat):
        if is_kendaraan_disewa(plat):
            print(f"Kendaraan dengan plat {plat} sudah disewa.")
            return
        
        kendaraan_data = cari_kendaraan(plat, kendaraan_tersedia())
        
        if kendaraan_data:
            print("\nData kendaraan yang kamu pilih untuk disewa:")
            tampilkan_kendaraan([kendaraan_data])
            
            nama_penyewa = input("Masukkan Nama Penyewa: ").capitalize()
            tanggal_sewa = datetime.now().strftime("%Y-%m-%d")
            # Menghitung tanggal kembali (misalnya 7 hari kemudian)
            tanggal_kembali = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
            
            data_penyewaan = {
                "plat": plat,
                "jenis": kendaraan_data["jenis"],
                "merek": kendaraan_data["merek"],
                "nama_penyewa": nama_penyewa,
                "tanggal_sewa": tanggal_sewa,
                "tanggal_kembali": tanggal_kembali
            }

            penyewaan.append(data_penyewaan)
            
            print("\nKendaraan berhasil disewa.")
            tampilkan_penyewaan([data_penyewaan])        
        else:
            print("\nKendaraan tidak terdapat dalam list")
    else:
        print(f"Kendaraan dengan plat {plat} tidak ditemukan dalam sistem.")

def kembalikan_kendaraan():
    if not penyewaan:
        tampilkan_penyewaan(penyewaan)
        menu_sewa()
    else:
        tampilkan_penyewaan(penyewaan)
        plat = validate_plat()
        if plat_exist(plat):
            # Mencari kendaraan yang sedang disewa berdasarkan plat
            penyewa_data = cari_penyewaan(plat)
            
            if penyewa_data:
                # Menampilkan data penyewaan yang akan dikembalikan
                print()
                tampilkan_penyewaan([penyewa_data])
                
                if lanjutkan("Apakah Anda yakin ingin mengembalikan kendaraan ini?"):
                    penyewaan.remove(penyewa_data)
                    print(f"Kendaraan dengan plat {plat} telah berhasil dikembalikan.")
                else:
                    print("Pengembalian dibatalkan.")
            else:
                print(f"Kendaraan dengan plat {plat} tidak ditemukan dalam penyewaan.")
        else:
            print(f"Kendaraan dengan plat {plat} tidak ditemukan dalam sistem.")

def menu_sewa():
    while True:
        try:
            print("\n|==================== Menu Penyewaan Kendaraan ==============|")
            print("1. Sewa Kendaraan")
            print("2. Kembalikan Kendaraan")
            print("3. Lihat Daftar Penyewaan")
            print("4. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-4): "))

            if pilihan == 1:
                sewa_kendaraan()
            elif pilihan == 2:
                kembalikan_kendaraan()
            elif pilihan == 3:
                tampilkan_penyewaan(penyewaan)
            elif pilihan == 4:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def main_menu():
    while True:
        try:
            print("\n|==================== Kendaraan Tracker ====================|")
            print("1. Lihat Daftar Kendaraan")
            print("2. Menambah Daftar Kendaraan")
            print("3. Mengubah Daftar Kendaraan")
            print("4. Menghapus Daftar Kendaraan")
            print("5. Penyewaan Kendaraan")
            print("6. Keluar Program")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-6): "))

            if pilihan == 1:
                menu_read()
            elif pilihan == 2:
                menu_create()
            elif pilihan == 3:
                menu_update()
            elif pilihan == 4:
                menu_delete()
            elif pilihan == 5:
                menu_sewa()
            elif pilihan == 6:
                print("Terima kasih telah menggunakan program kami!\n")
                sys.exit()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

main_menu()