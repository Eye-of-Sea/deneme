import time


while True:
    meme_sozlugu = {
                "CRINGE": "Garip ya da utandırıcı bir şey",
                "LOL": "Komik bir şeye verilen cevap",
                "BOSS": "Çoğu oyunun sonunda çıkan güçlü karakter",
                "STREAMER":"Online olarak yayın yapan kimse",
                "ROFL":"Bir şakaya karşılık cevap",
                "SHEESH":"Onaylamamak",
                "CREEPY":"Korkunç",
                "TO AGGRO":"Agresifleşmek/Sinirlenmek",
                }

    kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if kelime in meme_sozlugu.keys():
        print("Anlamı:",meme_sozlugu[kelime])
        time.sleep(2)
        # Kelime eşleşiyorsa ne yapmalıyız?
    else:
        print("Ne yazık ki öyle bir kelime bulamadık")
        time.sleep(0.5)
        #Kelime eşleşmiyorsa ne yapmalıyız?
