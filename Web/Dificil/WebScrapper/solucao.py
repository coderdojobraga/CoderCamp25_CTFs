import requests
import urllib3

def verificar_subdiretorias(arquivo):
    with open(arquivo, 'r') as f:
        subdiretorias = f.readlines()
        subdiretorias = [subdiretoria.strip() for subdiretoria in subdiretorias]

        for subdiretoria in subdiretorias:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            
            url = f'https://www.marcoslobo.xyz/rotas/{subdiretoria}.html'
            resposta = requests.get(url, verify=False)

            if resposta.status_code == 200:
                print(f"A subdiretoria '/{subdiretoria}.html' existe.")
                
if __name__ == "__main__":
    arquivo_subdiretorias = "/home/bernas/CoderCamp25_CTFs/Web/Dificil/WebScrapper/subdiretorias.txt"
    verificar_subdiretorias(arquivo_subdiretorias)