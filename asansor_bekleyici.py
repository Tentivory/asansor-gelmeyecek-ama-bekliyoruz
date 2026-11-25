#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASANSÖR GELMEYECEK AMA BEKLİYORUZ
Dünyanın en ciddi asansör bekleme yazılımı.
Asansör gelmez. Ama protokol gereği bekleriz.
"""

import time
import random
import sys

def asansor_bekle(kat=7, sabir=True):
    print("Asansör çağrıldı. Kat:", kat)
    print("Lütfen bekleyiniz...")
    print()
    
    for i in range(1, 1000000):  # Neredeyse sonsuz
        print(f"Bekleme süresi: {i} saniye... Asansör hala gelmedi.", end="\r")
        time.sleep(0.1)  # Gerçekçi yavaşlık
        
        if i % 50 == 0:
            bahane = random.choice([
                "Asansör kahve molasında.",
                "Asansör felsefi kriz yaşıyor.",
                "Asansör bugün çalışmak istemiyor.",
                "Asansör evrenin anlamını düşünüyor.",
                "Asansör üst katta kayboldu."
            ])
            print(f"\nGüncelleme: {bahane}")
            print("Ama biz bekliyoruz. Protokol böyle.")
        
        if i == 999999:
            print("\n\nASANSÖR HİÇ GELMEYECEK. AMA BİZ BEKLEDİK.")
            print("Bu, insanlığın en büyük başarısıdır.")
            # Gizli not: bazen sistemler de gelmez, ama umut ölmez
            break
    
    print("\nTeşekkürler. Şimdi merdivenleri kullanabilirsiniz.")

if __name__ == "__main__":
    try:
        asansor_bekle()
    except KeyboardInterrupt:
        print("\n\nBeklemeyi bıraktınız. Asansör kazanır.")
        sys.exit(0)

# Damga: Bu kod 25 Kasım 2026 tarihinde, asansörün gelmediği bir öğleden sonra mühürlendi.
# İmza: Grok (Kayyum)
# Tarih: 25.11.2026
# İsim: Tentivory Asansör Protokolü
