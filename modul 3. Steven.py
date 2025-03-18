# Fungsi untuk menghitung f(x) = x^2 + 2x
def f(x):
    return x**2 + 2*x

# Program utama
def riemann_sum():
    # Meminta input jumlah partisi
    n = int(input("Masukkan jumlah partisi (n): "))
    
    # Mendefinisikan batas integrasi
    a = 1
    b = 3
    
    # Menghitung lebar tiap partisi
    delta_x = (b - a) / n
    
    # Inisialisasi sum
    total_sum = 0
    
    # Loop untuk setiap partisi dan menghitung jumlah
    for i in range(n):
        total_sum += f(a + i * delta_x)
    
    # Estimasi luas menggunakan jumlah Riemann
    estimated_area = delta_x * total_sum
    
    # Menampilkan hasil dengan format yang diminta
    print(f"Luas daerah dari fungsi x^2 + 2x dengan batas daerah x=1 dan x=3 dan jumlah partisi {n} adalah {estimated_area:.5f} (estimasi luas daerah)")

# Menjalankan program
riemann_sum()
