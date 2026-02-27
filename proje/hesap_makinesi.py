print("--- Hesap Makinesi Uygulamasına Hoşgeldiniz ---")
sayi1 = float(input("Lütfen 1. saynızı giriniz: "))
sayi2 = float(input("Lütfen 2. sayınızı giriniz: "))
islem = str(input("Lüften işleminizi giriniz( +, -, x, ÷) "))

if islem == "+":
    added_num = sayi1 + sayi2
    print(f"Sonuç: {added_num}")
elif islem == "-":
    removed_num = sayi1 - sayi2
    print(f"Sonuç: {removed_num}")
elif islem == "x":
    mult_num = sayi1 * sayi2
    print(f"Sonuç: {mult_num}")
elif islem == "÷":
    div_num = sayi1 / sayi2
    print(f"Sonuç: {div_num}")
else:
    print("Geçersiz işlem girildi")

