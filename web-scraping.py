import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re
import csv
import time


def limpar_titulo(title):
    if title:
        title = title.split("|")[0].split("-")[0].split("–")[0]
        return title.strip()
    return "Nome não encontrado"


def normalizar_telefone(telefone):
    return re.sub(r"\D", "", telefone)


cabecalho = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
padrao_email = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
padrao_telefone = re.compile(r"\(?\d{2}\)?\s?(?:9\d{4,5}|\d{4,5})-?\d{4}")


try:
    busca_google = input(
        "O que você quer pesquisar no Google? (ex: construtoras em São Paulo) "
    )
    nome_arquivo_csv = "leads_consolidados.csv"

    if not busca_google:
        print("O termo de busca é necessário.")
    else:
        print(f"\n[PASSO 1] Buscando por '{busca_google}' no Google...")
        lista_de_sites = list(
            search(busca_google, lang="pt-br", num_results=30, sleep_interval=1)
        )

        print(
            f"Encontrados {len(lista_de_sites)} sites. Iniciando a extração de leads..."
        )
        print("-" * 50)

        empresas = {}
        contatos_processados = set()

        for site in lista_de_sites:
            print(f"(*) Analisando: {site}")
            try:
                resposta = requests.get(site, headers=cabecalho, timeout=10)
                if resposta.status_code == 200:
                    soup = BeautifulSoup(resposta.text, "html.parser")

                    nome_empresa = limpar_titulo(soup.title.string)
                    texto_do_site = soup.get_text()

                    emails_encontrados = set(padrao_email.findall(texto_do_site))
                    telefones_encontrados = set(padrao_telefone.findall(texto_do_site))

                    for link in soup.find_all("a", href=True):
                        href = link["href"]
                        if href.startswith("mailto:"):
                            emails_encontrados.add(href.replace("mailto:", ""))
                        elif "wa.me" in href or "api.whatsapp.com" in href:
                            telefones_encontrados.add(href)

                    if emails_encontrados or telefones_encontrados:
                        if nome_empresa not in empresas:
                            empresas[nome_empresa] = {
                                "telefones": set(),
                                "emails": set(),
                            }

                        for email in emails_encontrados:
                            email_limpo = email.lower()
                            if email_limpo not in contatos_processados:
                                empresas[nome_empresa]["emails"].add(email_limpo)
                                contatos_processados.add(email_limpo)

                        for tel in telefones_encontrados:
                            tel_normalizado = normalizar_telefone(tel)
                            if (
                                tel_normalizado
                                and tel_normalizado not in contatos_processados
                            ):
                                empresas[nome_empresa]["telefones"].add(
                                    tel
                                )  # Guarda o original formatado
                                contatos_processados.add(
                                    tel_normalizado
                                )  # Mas verifica pelo normalizado

            except Exception:
                pass

        print("\n" + "=" * 60)
        print("EXTRAÇÃO CONCLUÍDA! GERANDO ARQUIVO CSV CONSOLIDADO...")
        print("=" * 60)

        dados_para_csv = []
        for nome, contatos in empresas.items():
            if contatos["emails"] or contatos["telefones"]:
                dados_para_csv.append(
                    {
                        "Nome": nome,
                        "Telefones": " | ".join(sorted(contatos["telefones"])),
                        "Emails": " | ".join(sorted(contatos["emails"])),
                    }
                )

        if dados_para_csv:
            with open(
                nome_arquivo_csv, "w", newline="", encoding="utf-8"
            ) as arquivo_csv:
                nomes_colunas = ["Nome", "Telefones", "Emails"]
                escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=nomes_colunas)
                escritor_csv.writeheader()
                escritor_csv.writerows(dados_para_csv)

            print(
                f"✅ Sucesso! {len(dados_para_csv)} empresas com contatos únicos foram salvas no arquivo '{nome_arquivo_csv}'"
            )
        else:
            print("❌ Nenhuma informação de contato foi encontrada para salvar.")

        print("\n" + "=" * 60)

except Exception as e:
    print(f"Ocorreu um erro geral: {e}")
