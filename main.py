print("Penentu Siswa Lulus Atau Tidak")
print("===============================")

nama = input("Masukkan nama: ")
nilai = float(input("Masukkan nilai: "))

print("------------------------------")
print("Nama :", nama)
print("Nilai      :", nilai)

if nilai >= 75 and nilai <= 100:
    print("LULUS")
elif nilai >= 0 and nilai < 75:
    print("TIDAK LULUS")
else:
    print("NILAI TIDAK VALID")

print("______________________________")