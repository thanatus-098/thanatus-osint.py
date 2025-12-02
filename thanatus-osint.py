#!/usr/bin/env python3
import os
import requests
import sys
from datetime import datetime

BANNER = r"""
████████╗██╗  ██╗ █████╗ ███╗   ██╗ █████╗ ████████╗██╗   ██╗███████╗
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██║   ██║██╔════╝
   ██║   ███████║███████║██╔██╗ ██║███████║   ██║   ██║   ██║█████╗  
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔══██║   ██║   ╚██╗ ██╔╝██╔══╝  
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██║   ██║    ╚████╔╝ ███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝     ╚═══╝  ╚══════╝
                       Telegram: @thanatus098
"""

print(BANNER)
print("OSINT Tool Başladı...\n")

def ip_lookup(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        data = requests.get(url).json()
        return data
    except:
        return None

def username_lookup(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter": f"https://x.com/{username}",
    }

    result = {}
    for site, url in sites.items():
        try:
            r = requests.get(url)
            if r.status_code == 200:
                result[site] = "Kullanıcı bulunuyor → " + url
            else:
                result[site] = "Bulunamadı"
        except:
            result[site] = "Hata oluştu"

    return result


def menu():
    print("""
[1] IP Bilgisi Toplama
[2] Kullanıcı Adı OSINT (User Recon)
[3] Çıkış
""")

    secim = input("Seçim yap: ")

    if secim == "1":
        ip = input("Sorgulanacak IP: ")
        print(ip_lookup(ip))
    elif secim == "2":
        user = input("Kullanıcı adı: ")
        res = username_lookup(user)
        for k,v in res.items():
            print(f"{k}: {v}")
    else:
        print("Çıkılıyor...")
        sys.exit()

while True:
    menu()
