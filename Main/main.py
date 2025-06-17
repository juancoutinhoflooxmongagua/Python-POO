import shutil  # Biblioteca para encontrar caminhos de executáveis
import sys  # Biblioteca para encerrar o script em caso de erro
from selenium import webdriver
from selenium.webdriver.firefox.options import (
    Options,
)  # MUDANÇA: Importa as opções do FIREFOX
import time

# --- ETAPA 1: ENCONTRAR O FIREFOX AUTOMATICAMENTE ---
print("🔎 Procurando o executável do Firefox no seu sistema...")

# O nome padrão do executável do Firefox é simplesmente 'firefox' na maioria dos sistemas
firefox_path = shutil.which("firefox")

# Se o caminho não for encontrado, encerra o script com uma mensagem de erro
if not firefox_path:
    print("\n❌ ERRO: Navegador Firefox não encontrado.")
    print(
        "   Por favor, verifique se o Firefox está instalado e acessível no seu sistema."
    )
    sys.exit()  # Encerra o programa

print(f"✅ Firefox encontrado com sucesso em: {firefox_path}")


# --- ETAPA 2: CONFIGURAR E INICIAR O SELENIUM ---

# Crie um objeto de opções para o Firefox
firefox_options = Options()

# Usa o caminho que encontramos automaticamente
firefox_options.binary_location = firefox_path


# MUDANÇA: Inicia o WebDriver do Firefox
print("🦊 Iniciando o navegador Firefox...")
driver = webdriver.Firefox(options=firefox_options)


# Exemplo de automação: abrir um site
print("✅ Navegador iniciado. Acessando o site da Mozilla...")
driver.get("https://www.mozilla.org/pt-BR/firefox/")


# Espera 10 segundos para você ver a janela aberta
time.sleep(10)


# Fecha o navegador
print("🚪 Fechando o navegador.")
driver.quit()
