#O relatório gera 14 páginas ao todo de itens
import requests
import json
import csv
import time

#URL da consulta indicada no swagger dos dados abertos para consultar 
url_base = "https://dadosabertos.compras.gov.br/modulo-material/4_consultarItemMaterial"

headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


#Inicialização das variaáveis de contador para puxar todas as páginas
todos_os_itens = []
pagina_atual = 1
total_paginas = 1  # Começa em 1 e será atualizado dinamicamente na primeira resposta

print("=== INICIANDO A EXTRAÇÃO AUTOMÁTICA DE TODAS AS PÁGINAS ===")


#Laço de repetição para buscar os dados
while pagina_atual <= total_paginas:
    # Parâmetros para buscar os dados
    params = {
        "pagina": pagina_atual,
        "tamanho-pagina": 500,  # Mantém 500 registros por página para andar rápido
        #identifica apenas itens ativos
        "statusItem": 1,
        #identifica a classe dos itens, no caso "DROGAS E MEDICAMENTOS"
        "codigoGrupo":65        
    }
    
    #Retorno sobre o andamento da leitura e compilação das páginas
    print(f"Baixando página {pagina_atual} de {total_paginas}...", end="", flush=True)
    
    try:
        response = requests.get(url_base, params=params, headers=headers, timeout=30)
        
        #Testa se a conexão está 5.5
        if response.status_code == 200:
            dados = response.json()
            
            # Se for a primeira página, atualiza o total real de páginas do servidor
            if pagina_atual == 1:
                total_paginas = dados.get("totalPaginas", 1)
                total_registros = dados.get("totalRegistros", 0)
                print(f"\n[Info] Total de registros na base do governo: {total_registros}")
                print(f"[Info] Total de páginas identificadas: {total_paginas}\n")
                print(f"Baixando página {pagina_atual} de {total_paginas}...", end="", flush=True)
            
            # Identifica automaticamente onde a lista de materiais está guardada no JSON
            chave_lista = None
            for chave, valor in dados.items():
                if isinstance(valor, list):
                    chave_lista = chave
                    break
            
            if chave_lista:
                itens_pagina = dados[chave_lista]
                todos_os_itens.extend(itens_pagina)
                print(f" Sucesso! (+{len(itens_pagina)} itens adicionados. Total: {len(todos_os_itens)})")
            else:
                print(" Erro: Não foi possível localizar a lista de dados dentro do JSON.")
            
            # Avança para a próxima página
            pagina_atual += 1
            
            # IMPORTANTE: Pausa de 0.5 segundos para o servidor do governo não bloquear seu IP por excesso de acessos
            time.sleep(0.5)
            
        else:
            print(f"\n[Erro de Servidor] Status {response.status_code} na página {pagina_atual}. Tentando novamente em 5 segundos...")
            time.sleep(5)
            
    except requests.exceptions.RequestException as e:
        print(f"\n[Erro de Conexão] {e}. Tentando novamente em 5 segundos...")
        time.sleep(5)

print("\n=== PROCESSO DE DOWNLOAD CONCLUÍDO! ===")
print(f"Total geral de materiais acumulados: {len(todos_os_itens)}")

# --- ARQUIVO 1: SALVANDO TUDO JUNTO EM UM ÚNICO JSON ---
print("\nSalvando banco de dados unificado em JSON...")
with open("todos_os_materiais.json", "w", encoding="utf-8") as f:
    json.dump(todos_os_itens, f, indent=4, ensure_ascii=False)
print("-> Arquivo 'todos_os_materiais.json' gerado com sucesso!")

# --- ARQUIVO 2: SALVANDO EM CSV EM PORTUGUÊS (PRONTO PARA O EXCEL) ---
if todos_os_itens:
    print("\nConvertendo dados para abrir direto no Excel...")
    # Extrai os nomes das colunas baseados nas chaves do primeiro item carregado
    colunas = todos_os_itens[0].keys()
    
    # 'utf-8-sig' força o Excel brasileiro a reconhecer os acentos (DRÁGEA, MEDICAÇÃO, etc.) sem bugar
    with open("todos_os_materiais.csv", "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.DictWriter(f, fieldnames=colunas, delimiter=";")
        escritor.writeheader()
        escritor.writerows(todos_os_itens)
    print("-> Arquivo 'todos_os_materiais.csv' gerado com sucesso!")
    print("\n[Pronto] Agora você pode abrir o arquivo '.csv' diretamente no seu Excel!")
