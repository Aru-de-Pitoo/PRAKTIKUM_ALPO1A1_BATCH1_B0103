# 1. Deklarasi Variabel Profil Karakter Game
nama_hero = "Benedetta"
level = 10
hp = 4.036
is_alive = True
inventory = ["Blade of the Heptaseas", "Sea Halberd", "Blade of Despair"]
atribut = {"kekuatan": 205, "kelincahan": 255}

# 2. Menampilkan Seluruh Informasi Karakter
print("=== INFORMASI KARAKTER AWAL ===")
print("Nama Hero    :", nama_hero)
print("Level        :", level)
print("Health Point :", hp)
print("Status Hidup :", is_alive)
print("Inventory    :", inventory)
print("Atribut      :", atribut)

# 3. Menampilkan Tipe Data dari Masing-Masing Variabel
print("\n=== TIPE DATA VARIABEL ===")
print("Tipe data nama_hero :", type(nama_hero))
print("Tipe data level     :", type(level))
print("Tipe data hp        :", type(hp))
print("Tipe data is_alive  :", type(is_alive))
print("Tipe data inventory :", type(inventory))
print("Tipe data atribut   :", type(atribut))

# 4. Aksi Perubahan (Dapat item baru & Naik level)
# Menambahkan item "Ramuan HP" ke dalam list inventory
inventory.append("Sky Piercer")

# Karakter naik level: konversi level ke float lalu tambahkan 0.5
level = float(level) + 1.0

# 5. Mencetak Kembali Informasi Terbaru dari Karakter
print("\n=== INFORMASI KARAKTER TERBARU (SETELAH UPDATE) ===")
print("Nama Hero    :", nama_hero)
print("Level Terbaru:", level)
print("Tipe Level   :", type(level))
print("Health Point :", hp)
print("Status Hidup :", is_alive)
print("Inventory    :", inventory)
print("Atribut      :", atribut)