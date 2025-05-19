import requests

# URL de destino
url = "seualvoaqui"

# Cabeçalhos da requisição (mantenha o necessário, mas limpo, já que estamos como visitante)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Content-Type": "application/json",  # ou "application/x-www-form-urlencoded" se for o caso
}

# Corpo da requisição (vazio ou com algo genérico, pois ainda não vamos testar payloads)
data = {
    "username": "teste",  # substitua ou deixe vazio conforme a plataforma exige
    "password": "123456"
}

# Envio da requisição
try:
    response = requests.post(url, headers=headers, json=data, timeout=10)

    # Criação do relatório
    with open("rei_auth_response.txt", "w", encoding="utf-8") as file:
        file.write("===== REQUISIÇÃO =====\n")
        file.write(f"URL: {url}\n")
        file.write(f"Headers: {headers}\n")
        file.write(f"Body enviado: {data}\n\n")

        file.write("===== RESPOSTA =====\n")
        file.write(f"Status Code: {response.status_code}\n")
        file.write(f"Headers: {response.headers}\n\n")
        file.write("Corpo da resposta:\n")
        file.write(response.text)

    print("[+] Resultado salvo em 'rei_auth_response.txt'.")

except requests.exceptions.RequestException as e:
    print(f"[!] Erro ao fazer a requisição: {e}")
