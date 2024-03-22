cumleler = [
"Lorem Ipsum is simply dummy text of the printing and typesetting industry",
"Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text",
"There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form",
"Lorem Ipsum is simply dummy text of the printing and typesetting industry",
"There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form",
"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
"Lorem Ipsum is simply dummy text of the printing and typesetting industry",
"There are many variations of passages available, but the majority have suffered",
"Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text",
"There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form"


]

# Yeni bir liste oluşturun
toplam_harf_sayisi_listesi = []

# Her bir cümle için döngü
for cumle in cumleler:
    # Cümledeki boşluk karakterlerini kaldırın ve toplam harf sayısını hesaplayın
    toplam_harf_sayisi = len(cumle.replace(" ", ""))
    # Yeni listenin içine toplam harf sayısını ekleyin
    toplam_harf_sayisi_listesi.append(toplam_harf_sayisi)

# Sonuçları yazdırın
print("Cümlelerin Toplam Harf Sayıları:")
print(toplam_harf_sayisi_listesi)