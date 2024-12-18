import os
from flask import Flask, send_file, request, render_template

app = Flask(__name__)

# Sözlük ve görsel bilgileri
sozlukler = [
    {"ruj": {"anlam": "lipstick", "gorsel": "images/ruj.jpg"}},
    {"rimel": {"anlam": "mascara", "gorsel": "images/rimel.jpg"}},
    {"allık": {"anlam": "blush", "gorsel": "images/allık.jpg"}},
    {"fondöten": {"anlam": "foundation", "gorsel": "images/fondöten.jpg"}},
    {"dudak kalemi": {"anlam": "lip liner", "gorsel": "images/dudakkalemi.jpg"}},
    {"far paleti": {"anlam": "eyeshadow palette", "gorsel": "images/farpaleti.jpg"}},
]

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/sozluk")
def sozluk():
    # Tüm sözlüğü render_template ile sozluk.html'e gönderiyoruz
    return render_template("sozluk.html", data=sozlukler)

@app.route("/arama", methods=["GET"])
def arama():
    # Kullanıcıdan gelen anahtar kelimeyi al ve küçük harfe çevir
    anahtar_kelime = request.args.get("anahtarKelime", "").strip().lower()
    
    if not anahtar_kelime:
        return "Lütfen bir anahtar kelime giriniz."
    
    # Sözlüklerde küçük harflerle arama yap
    for sozluk in sozlukler:
        for key in sozluk:
            if anahtar_kelime == key.lower():  # Küçük harf karşılaştırması
                kelime_bilgisi = sozluk[key]
                return render_template(
                    "sonuc.html",
                    kelime=key.capitalize(),  # Görünümü güzelleştirmek için ilk harfi büyük yapıyoruz
                    anlam=kelime_bilgisi["anlam"],
                    gorsel=f"/static/{kelime_bilgisi['gorsel']}"
                )
    
    # Kelime bulunamadığında
    return f"{anahtar_kelime} kelimesi sözlükte bulunamadı."

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()