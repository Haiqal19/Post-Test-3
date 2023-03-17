import time 
import os
os.system ("cls")

class wishlist:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.next = None

class steam:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.riwayat = []

    def twishlisht (self):
        game = wishlist(nama, harga)
        if self.head is None:
            self.head = game
        else:
            game.next = self.head
            self.head = game
        self.riwayat.append (f"Ditambahkan : {game.nama} (Rp. {game.harga})")
    
    def tampilw (self):
        if self.head is None:
            print("Tidak ada barang")
        else:
            current = self.head
            while current is not None:
                print (f"{current.nama} (Rp. {current.harga})")
                current = current.next

    def list (self,nama,harga):
        data_baru = wishlist (nama,harga)
        if self.head == None:
            self.head = data_baru
        else:
            data_baru.next = self.head
            self.head = data_baru

    def hwishlist (self, nama):
        gamesekarang = self.head
        gamesebelumnya = None
        while gamesekarang is not None:
            if gamesekarang.nama == nama:
                if gamesebelumnya is not None:
                    gamesebelumnya.next = gamesekarang.next
                    if gamesekarang.next is None:
                        self.tail = gamesebelumnya
                else:
                    self.head = gamesekarang.next
                    if self.head is None:
                        self.tail = None
                self.riwayat.append (f"Dihapus     : {gamesekarang.nama} (Rp. {gamesekarang.harga})")
                return True
            else:
                gamesebelumnya = gamesekarang
                gamesekarang = gamesekarang.next
        return False
    
    def rwishlist (self):
        print ("Riwayat")
        for rgame in self.riwayat:
            print (rgame)

tokline = steam()
tokline.list("Gta V","600.000")
tokline.list("The Forest","100.000")

def loguser():
    print ("~~~/\/\/\/\ Steam Login /\/\/\/\~~~")
    input ("Username : ")
    input ("Password : ")
    return True

if loguser():
    while True:
        os.system ("cls")
        print ("=================================")
        print (">>>=== Wishlist Game Steam ===<<<")
        print ("=================================")
        print ("1. Tambah Wishlist Game")
        print ("2. Tampilkan Wishlist Game")
        print ("3. Hapus Wishlist Game")
        print ("4. Riwayat Wishlist Game")
        print ("5. Keluar")
        print ("=================================")
        pilih = input ("Masukkan Pilihan : ")
        if pilih == "1":
            nama = input ("Nama Game  : ")
            harga = input("Harga Game : ")
            tokline.twishlisht()
            input ("=================================")
        elif pilih == "2":
            tokline.tampilw()
            input ("=================================")
        elif pilih == "3":
            nama = input ("Nama Game : ")
            if tokline.hwishlist(nama):
                print ("Game Telah Berhasil Dihapus Dari Wishlist")
                input ("=================================")
            else:
                print ("Game Tidak Ditemukan Di Wishlist")
                input ("=================================")
        elif pilih == "4":
            tokline.rwishlist()
            input ("=================================")
        elif pilih == "5":
            break
        else:
            print ("Pilihan Salah")
            time.sleep(1)
