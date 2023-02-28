###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)


y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)


l = [1, 2, 3, 4,"String",3.2, False]
type(l)


d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)


s = {"Python", "Machine Learning", "Data Science","Python"}
type(s)



###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

answer = [word.upper() for word in text.replace(",", "").replace(".", "").split()]
answer

text.upper().replace(",", "").replace(".", "").split()

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.

len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.

lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.

lst.remove(lst[8])
lst.pop(8)


# Adım 5: Yeni bir eleman ekleyin.

lst.append("Yeni eleman")
lst


# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8,"N")
lst

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()


# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict["Daisy"] = ["England", 13]
dict
# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict["Ahmet"] = ["Ahmet", 24]
dict
# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")
dict


###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

def fonk(l):
    return [i for i in l if i % 2 == 0], [i for i in l if i % 2 != 0]

fonk(l)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

a = [print(f"Muhendislik {i}. öğrencisi : ", v) if i < 4 else print(f"Tıp {i-3}. öğrencisi : ", v) for i, v in enumerate(ogrenciler,1)]

###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

dkk = list(zip(kredi, ders_kodu, kontenjan))

sonuc = [print(f"Kredisi {k} olan {d} kodlu dersin kontenjanı {ko} kişidir") for k,d,ko in dkk]

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

cvp = [print(kume1.intersection(kume2)) if kume1.issuperset(kume2) else print(kume2 - kume1)]






