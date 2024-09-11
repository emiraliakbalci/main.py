dict = {
        "CRINGE": "Garip ya da utandırıcı bir şey",
        "LOL": "Komik bir şeye verilen cevap",
        "SHEESH": "onaylamamak",
        "ROFL": "bir şakaya karşılık cevap",
        "CREEPY": "korkunç"
        }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in dict.keys():
    print(word, "kelimesinin anlamı: ", dict[word])
else:
    print("Yazdığınız kelime sözlükte mevcut değil.")
