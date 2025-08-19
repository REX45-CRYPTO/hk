#!/usr/bin/env python3
#  ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗ ████████╗
#  ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔═══██╗╚══██╔══╝
#  ███████╗██║   ██║██║   ██║██████╔╝██║   ██║   ██║
#  ╚════██║██║   ██║██║   ██║██╔══██╗██║   ██║   ██║
#  ███████║╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝   ██║
#  ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝
#  HOKIDRAW 4D — NEXT NUMBER PREDICTOR v2.0
import hashlib, time, os, sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
\033[38;5;51m
  ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗ ████████╗
  ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔═══██╗╚══██╔══╝
  ███████╗██║   ██║██║   ██║██████╔╝██║   ██║   ██║
  ╚════██║██║   ██║██║   ██║██╔══██╗██║   ██║   ██║
  ███████║╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝   ██║
  ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝\033[0m
         \033[38;5;214m🔮  HOKIDRAW 4D PREDICTOR  🔮\033[0m
    """)

def loading():
    print("\033[38;5;87m  ⏳  Menghitung prediksi...\033[0m", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

def generate_next_4d(last_4d: str) -> str:
    if not last_4d.isdigit() or len(last_4d) != 4:
        raise ValueError("Input harus 4 digit (0000–9999)")
    hash_digest = hashlib.sha256(last_4d.encode()).hexdigest()
    indices = [5, 10, 15, 20]
    digits = [int(hash_digest[i], 16) % 10 for i in indices]
    last_digit = int(last_4d[-1])
    final_digits = [(d + last_digit) % 10 for d in digits]
    return ''.join(map(str, final_digits))

def main():
    clear()
    banner()
    try:
        last = input("\033[38;5;226m  [>] Masukkan 4 angka terakhir: \033[0m").strip()
        loading()
        prediksi = generate_next_4d(last)
        print(f"\033[38;5;82m  🎯  Prediksi 4D berikutnya: \033[1m{prediksi}\033[0m\n")
    except ValueError as e:
        print(f"\033[38;5;196m  ❌  {e}\033[0m\n")
    input("  Tekan Enter untuk keluar...")

if __name__ == "__main__":
    main()
