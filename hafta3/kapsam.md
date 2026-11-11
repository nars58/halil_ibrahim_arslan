# Görev 4 - Kapsam (Scope) Tahminleri ve Açıklamaları
Halil İbrahim Arslan - 20253004034

## Örnek 1: Global Değişkeni Okuma
```python
yakit = 100

def goster():
    print(yakit)

goster()
```
- **Tahmin:** `100`
- **Gerçek Sonuç:** `100`
- **Nedeni:** Fonksiyon içinde `yakit` adında yerel bir değişken tanımlanmadığı için Python LEGB (Local -> Enclosing -> Global -> Built-in) kuralına göre bir üst kapsam olan global kapsama bakar ve `100` değerini bulup yazdırır.

## Örnek 2: Yerel Değişken ile Gölgeleme (Shadowing)
```python
yakit = 100

def degistir():
    yakit = 50
    print("Fonksiyon içi:", yakit)

degistir()
print("Global:", yakit)
```
- **Tahmin:** Fonksiyon içi `50`, Global `100`
- **Gerçek Sonuç:** Fonksiyon içi `50`, Global `100`
- **Nedeni:** Fonksiyon içindeki `yakit = 50` ataması global değişkeni değiştirmez; yalnızca fonksiyonun yerel (Local) kapsamında yeni bir `yakit` değişkeni oluşturur. Fonksiyon bittiğinde yerel değişken silinir ve global `yakit` `100` olarak kalır.

## Örnek 3: `UnboundLocalError` Tuzağı
```python
yakit = 100

def harca():
    yakit = yakit - 10
    print(yakit)

harca()
```
- **Tahmin:** `UnboundLocalError` hatası verir.
- **Gerçek Sonuç:** `UnboundLocalError: cannot access local variable 'yakit' where it is not associated with a value`
- **Nedeni:** Python fonksiyonu derlerken `yakit = ...` atama satırını gördüğü anda `yakit` değişkenini yerel (Local) değişken olarak işaretler. Ancak eşitliğin sağ tarafındaki `yakit - 10` hesaplanırken yerel `yakit` değişkenine henüz bir değer atanmadığı için `UnboundLocalError` fırlatılır.
