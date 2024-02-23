"""Python ile FBP Paradigması ile Örnek Uygulama: Dosya İşleme
Bu Python örneğinde, FBP prensiplerine uygun olarak bir dosya işleme akışı oluşturdum.
Belirli bir klasördeki metin dosyalarını okuyor, bu dosyaları işleyerek (burada sadece büyük harflere dönüştürme işlemi yapıyoruz) ve sonuçları başka bir dosyaya yazıyoruz.
Bu örnek, FBP'nin temel özelliklerini ve Python dilinin esnekliğini bir araya getirerek veri işleme akışlarını nasıl oluşturabileceğimizi göstermektedir.
"""

import os
from datetime import datetime


# Veri okuma bileşeni
def read_data(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Veri işleme bileşeni
def process_data(data):
    return data.upper()


# Sonuç yazma bileşeni
def write_result(result, output_file):
    with open(output_file, 'a') as file:
        file.write(result + '\n')


# Ana akış fonksiyonu
def main():
    input_folder = "input_data"
    output_file = "output.txt"

    # Sonuç dosyasını temizle
    open(output_file, 'w').close()

    # Klasördeki dosyaları işle
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)

            # Veri okuma
            data = read_data(file_path)

            # Veri işleme
            processed_data = process_data(data)

            # Sonuç yazma
            write_result(processed_data, output_file)
            print(f"[{datetime.now()}] {filename} işlendi.")


if __name__ == "__main__":
    main()
