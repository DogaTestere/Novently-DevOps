print("--- Hesap Makinesi Uygulamasına Hoşgeldiniz ---")

sayi1 = float(input("Lütfen 1. saynızı giriniz: "))
sayi2 = float(input("Lütfen 2. sayınızı giriniz: "))
# Normalde input sonucu çıkan değerler 'str' olarak yani 'yazı' olarak kaydedilir
# 'str' tipi değişkenler toplanamaz, bu nedenle float() ile türünün sayıya dönüştürülmesi gerekir.
# Bunu ya input() kısmını float() içine alarak yada değişkeni float() içine alarak yaparız

islem = str(input("Lüften işleminizi giriniz( +, -, x, ÷) "))
# Burada sadece ek önlem olarak tekrardan str yaptım.
# Değişkenin türünü sabitlemek için yani, yoksa normalde de 'str' olarak belirleniyor tür

def addition(num1, num2):
    return num1 + num2
# Burada işlem kısa olduğu ve sadece tek bir sonuç ortaya çıkacağı için direkt return kullanılabiliyor
# Eğer fonksiyon içinde başka işlemler yapılacak olsaydı:
# işlem_sonucu = ...
# return işlem_sonucu
# Yapılabilirdi

def substraction(num1, num2):
    return num1 - num2

def multipilication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2
# Eğer burada iki çizgi // kullanılsaydı, bölme işleminde sadece virgülden öncesi gelirdi
# Tek çizgi kullanıldığında ise virgülden sonrasını da gösteriyor
# Örn 1580 // 1440 --> 1.0
#     1580 / 1440 --> 1.0972

if islem == "+":
    print(f"Sonuç: {addition(sayi1, sayi2)})
elif islem == "-":
    print(f"Sonuç: {substraction(sayi1, sayi2)}")
elif islem == "x":
    print(f"Sonuç {multipilication(sayi1, sayi2)}")
elif islem == "÷":
    print(f"Sonuç: {division(sayi1, sayi2)}")
else:
    print("Geçersiz işlem girildi")