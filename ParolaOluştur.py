import random
import string 

def parola_olustur(uzunluk):
    parola = ""
    for i in range(uzunluk):
        parola += random.choice(string.ascii_letters)
    return parola

def main():
  uzunluk = int(input("Parola uzunluğunu giriniz: "))
  parola = parola_olustur(uzunluk)
  print(f"Oluşturulan Parola : {parola}")

if __name__ == "__main__":
   main()
  
