# Security Testing Toolkit

Conjunto de ferramentas Python para testes de segurança em aplicações web, com foco em:

- Análise de endpoints de autenticação
- Detecção de Server-Side Template Injection (SSTI)
- Fuzzing de parâmetros via GET/POST/JSON

## 🛠️ Módulos

### 1. Auth Analyzer (`analisis.py`)
- Teste de endpoints de login
- Análise de respostas HTTP
- Geração de relatório estruturado
- Detecção de padrões inseguros

### 2. SSTI Scanner
- `fuzzinssit.py`: Teste de SSTI via parâmetros GET
- `ssti_json_fuzzer.py`: Teste de SSTI em APIs JSON
- Suporte a múltiplas engines de template

## ⚙️ Instalação

```bash
pip install requests



🚀 Como Usar
Auth Analyzer:

bash
python3 auth_analyzer/analisis.py
SSTI Scanner (GET):

bash
python3 ssti_scanner/fuzzinssit.py
SSTI Scanner (JSON):

bash
python3 ssti_scanner/ssti_json_fuzzer.py
