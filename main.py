#!/usr/bin/env python3
import hashlib, itertools, os, sys, time

# ---------------------------- UTILS ----------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
\033[38;5;51m
  ▄████▄   ▒█████   ██▓███   ▄▄▄       ██▓     ██▓
 ▒██▀ ▀█  ▒██▒  ██▒▓██░  ██▒▒████▄    ▓██▒    ▓██▒
 ▒▓█    ▄ ▒██░  ██▒▓██░ ██▓▒▒██  ▀█▄  ▒██░    ▒██░
 ▒▓▓▄ ▄██▒▒██   ██░▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██░    ▒██░
 ▒ ▓███▀ ░░ ████▓▒░▒██▒ ░  ░ ▓█   ▓██▒░██████▒░██████▒
 ░ ░▒ ▒  ░░ ▒░▒░▒░ ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░
   ░  ▒     ░ ▒ ▒░ ░▒ ░       ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░
 ░        ░ ░ ░ ▒  ░░         ░   ▒     ░ ░     ░ ░
 ░ ░          ░ ░                 ░  ░    ░  ░    ░  ░
 ░
\033[0m
        \033[38;5;214m🔮  HYPER-CRYPTO 4D ENGINE  🔮\033[0m
""")

# ---------------------------- MATEMATIKA ----------------------------
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def matrix_rotate(m):
    """Rotasi matriks 90° searah jarum jam"""
    return [list(row) for row in zip(*m[::-1])]

def fib_mod(n, mod):
    """Fibonacci modulo"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % mod
    return a

def galois_lfsr(seed, taps=[4, 3, 2, 0], n=4):
    """Linear Feedback Shift Register 4-bit"""
    reg = seed & 0xF
    out = []
    for _ in range(n):
        fb = sum([(reg >> t) & 1 for t in taps]) % 2
        reg = ((reg << 1) | fb) & 0xF
        out.append(reg)
    return out

def hyper_hash_4d(inp: str) -> str:
    if not inp.isdigit() or len(inp) != 4:
        raise ValueError("Input harus 4 digit (0000–9999)")

    # 1. SHA-512 hash
    h = hashlib.sha512(inp.encode()).hexdigest()
    h_bytes = bytes.fromhex(h)

    # 2. Buat matriks 4x4 dari 16 byte pertama
    mat = [[h_bytes[i*4 + j] for j in range(4)] for i in range(4)]

    # 3. Rotasi matriks + XOR dengan prima
    for p in PRIMES[:4]:
        mat = matrix_rotate(mat)
        for i in range(4):
            for j in range(4):
                mat[i][j] = (mat[i][j] ^ p) % 97

    # 4. Ambil diagonal utama → jadikan seed
    seed = sum(mat[i][i] for i in range(4)) % 65536

    # 5. Fibonacci transform
    fib_vals = [fib_mod(seed + i, 97) for i in range(4)]

    # 6. LFSR shuffle
    lfsr_out = galois_lfsr(seed & 0xF)
    final_digits = [(fib_vals[i] + lfsr_out[i]) % 10 for i in range(4)]

    return ''.join(map(str, final_digits))

# ---------------------------- CLI ----------------------------
def loading():
    print("\033[38;5;87m  ⏳  Computing hyper-crypto sequence...\033[0m", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

def main():
    clear()
    banner()
    try:
        inp = input("\033[38;5;226m  [>] Masukkan 4 angka terakhir: \033[0m").strip()
        loading()
        result = hyper_hash_4d(inp)
        print(f"\033[38;5;82m  🎯  Hyper-Crypto 4D: \033[1m{result}\033[0m\n")
    except ValueError as e:
        print(f"\033[38;5;196m  ❌  {e}\033[0m\n")
    input("  Tekan Enter untuk keluar...")

if __name__ == "__main__":
    main()
