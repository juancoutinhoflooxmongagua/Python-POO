# type: ignore
# Selenium - Automatizando tarefas no navegador Brave (Versão Moderna)
from time import sleep
import shutil  # Importado para encontrar o executável do Brave
import sys  # Importado para encerrar o script se o Brave não for encontrado

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Importa a tecla ENTER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Não precisamos mais do caminho manual para o driver.


def make_brave_browser(*options: str) -> webdriver.Chrome:
    """
    Cria uma instância do Brave Browser com gerenciamento automático do driver.
    """
    brave_options = webdriver.ChromeOptions()

    # --- NOVO: Encontra o Brave automaticamente ---
    brave_path = shutil.which("brave-browser") or shutil.which("brave")
    if not brave_path:
        print("❌ ERRO: Navegador Brave não encontrado.")
        print("   Verifique se o Brave está instalado e acessível no seu sistema.")
        sys.exit()

    # Aponta para o executável do Brave que encontramos
    brave_options.binary_location = brave_path
    # --- FIM DA NOVIDADE ---

    if options:
        for option in options:
            brave_options.add_argument(option)

    # O Selenium vai usar o driver correto para a sua versão do Brave
    # automaticamente, sem precisar do 'Service'.
    browser = webdriver.Chrome(options=brave_options)

    return browser


if __name__ == "__main__":
    TIME_TO_WAIT = 10
    options = ()
    browser = make_brave_browser(*options)

    # O resto da automação funciona exatamente como antes
    browser.get("https://www.google.com")
    print("✅ Navegador Brave iniciado. Acessando o Google...")

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_input.send_keys("Hello Brave Browser!")
    search_input.send_keys(Keys.ENTER)  # Pressiona Enter para buscar

    # Espera pelos resultados
    WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    print("✅ Busca realizada com sucesso. A janela fechará em 10 segundos.")
    sleep(TIME_TO_WAIT)

    # Fecha o navegador
    browser.quit()
