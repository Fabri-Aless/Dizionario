meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }


parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

while True:
    if parola in meme_dict.keys():
        print(parola,":",meme_dict[parola])
    else:
        print("La parola inserita non è nel mio database")
    x input("Vuoi continuare? y or n")
    if x =="n":
        print("Arrivederci")
        break
