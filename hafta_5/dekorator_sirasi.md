# Görev 2 - Çağrı Sayacı ve Dekoratör Sırası
Halil İbrahim Arslan - 20253004034

## Sonuçlar (`fib(20)`)
- **Yalnızca `@say`**: 21891
- **`@say` üstte, `@lru_cache` altta**: 39
- **`@lru_cache` üstte, `@say` altta**: 21

## Neden Farklıdır?

1. **Yalnızca `@say` (21891 çağrı):**
   Önbellekleme (`lru_cache`) kullanılmadığı için aynı Fibonacci değerleri tekrar tekrar hesaplanır. `fib(20)` çağrıldığında alt dallardaki tüm özyinelemeli çağrılar baştan çalışır ve toplamda 21891 kez fonksiyon çağrılır.

2. **`@say` üstte, `@lru_cache` altta (39 çağrı):**
   Çağrı önce dıştaki `@say` dekoratörüne gelir, ardından `@lru_cache` kontrol edilir. Her `n` değeri (2'den 20'ye kadar 19 düğüm) ilk hesaplandığında `fib(n-1)` ve `fib(n-2)` olmak üzere 2 alt çağrı yapar (`1 + 19 * 2 = 39`). Sonuç önbellekte olsa bile `@say` en dışta olduğu için önbellekten dönen çağrılar da sayılır ve sonuç 39 olur.

3. **`@lru_cache` üstte, `@say` altta (21 çağrı):**
   Çağrı önce dıştaki `@lru_cache` dekoratörüne gelir. Eğer aranan `n` değeri önbellekte varsa içteki `@say` dekoratörüne hiç girilmeden doğrudan önbellekten döndürülür. İçteki `@say` yalnızca 0'dan 20'ye kadar olan 21 farklı sayı ilk kez hesaplanırken çalışır. Bu yüzden sayaç 21 olur ve sayaca `fib.__wrapped__.cagri` ile ulaşılır.
