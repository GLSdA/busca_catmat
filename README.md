# README – Extração de Dados CATMAT – Compras.gov

## Descrição

O **Extrator de Dados CATMAT – Compras.gov** é um projeto desenvolvido em Python para coletar e estruturar informações do catálogo **CATMAT (Catálogo de Materiais)** disponibilizado pelo Governo Federal.

A ferramenta realiza a extração dos itens pertencentes à **Classe 6505 – Drogas e Medicamentos**, processando os dados e gerando arquivos nos formatos **JSON** e **CSV** para utilização em análises, integrações de sistemas, processos de ETL e soluções de Business Intelligence.

## Objetivo

Automatizar a obtenção dos itens catalogados na classe **6505 – Drogas e Medicamentos** do CATMAT, disponibilizando uma base estruturada e de fácil consumo para atividades de:

* Gestão de compras públicas;
* Planejamento de aquisições;
* Governança de dados;
* Inteligência de compras;
* Monitoramento de catálogos de medicamentos;
* Construção de painéis e indicadores.

## Funcionalidades

* Extração automatizada de dados do CATMAT;
* Filtragem específica da **Classe 6505 – Drogas e Medicamentos**;
* Coleta de informações detalhadas dos itens catalogados;
* Geração de arquivos em formato CSV;
* Geração de arquivos em formato JSON;
* Estruturação e padronização dos dados extraídos;
* Suporte para utilização em pipelines de dados e integrações.

## Estrutura dos Dados

Os registros extraídos contêm informações como:

| Campo                       | Descrição                                            |
| --------------------------- | ---------------------------------------------------- |
| codigoItem                  | Identificador único do item CATMAT                   |
| codigoGrupo                 | Código do grupo CATMAT                               |
| nomeGrupo                   | Nome do grupo CATMAT                                 |
| codigoClasse                | Código da classe CATMAT                              |
| nomeClasse                  | Nome da classe CATMAT                                |
| codigoPdm                   | Código do Padrão Descritivo de Material (PDM)        |
| nomePdm                     | Nome do PDM                                          |
| descricaoItem               | Descrição completa do item                           |
| statusItem                  | Indica se o item está ativo                          |
| itemSustentavel             | Indica se o item possui atributo de sustentabilidade |
| codigo\_ncm                 | Código NCM vinculado ao item                         |
| descricao\_ncm              | Descrição da NCM                                     |
| aplica\_margem\_preferencia | Indica aplicação de margem de preferência            |
| dataHoraAtualizacao         | Data e hora da última atualização do item            |

## Exemplo de Saída CSV

```csv
codigoItem;codigoGrupo;nomeGrupo;codigoClasse;nomeClasse;codigoPdm;nomePdm;descricaoItem;statusItem;itemSustentavel;codigo_ncm;descricao_ncm;aplica_margem_preferencia;dataHoraAtualizacao

386846;65;EQUIPAMENTOS E ARTIGOS PARA USO MÉDICO, DENTÁRIO E VETERINÁRIO;6505;DROGAS E MEDICAMENTOS;10956;POLICARBOFILA CÁLCICA;POLICARBOFILA CÁLCICA, CONCENTRAÇÃO: 500 MG;True;False;30049029;;True;2021-10-16T09:43:08.030221
```

## Exemplo de Saída JSON

```json
{
    "codigoItem": 386846,
    "codigoGrupo": 65,
    "nomeGrupo": "EQUIPAMENTOS E ARTIGOS PARA USO MÉDICO, DENTÁRIO E VETERINÁRIO",
    "codigoClasse": 6505,
    "nomeClasse": "DROGAS E MEDICAMENTOS",
    "codigoPdm": 10956,
    "nomePdm": "POLICARBOFILA CÁLCICA",
    "descricaoItem": "POLICARBOFILA CÁLCICA, CONCENTRAÇÃO: 500 MG",
    "statusItem": true,
    "itemSustentavel": false,
    "codigo_ncm": "30049029",
    "descricao_ncm": null,
    "aplica_margem_preferencia": true,
    "dataHoraAtualizacao": "2021-10-16T09:43:08.030221"
}
```

## Requisitos

* Python 3.10 ou superior
* Dependências listadas no arquivo `requirements.txt`

Instalação:

```bash
pip install -r requirements.txt
```

## Execução

Execute o script principal:

```bash
python main.py
```

Após a conclusão do processamento, os arquivos serão gerados no diretório configurado pelo projeto.

## Arquivos Gerados

| Arquivo                 | Descrição                               |
| ----------------------- | --------------------------------------- |
| todos_os_materiais.json | Base completa dos itens em formato JSON |
| todos_os_materiais.csv  | Base completa dos itens em formato CSV  |

## Aplicações

Os dados gerados podem ser utilizados para:

* Estudos de mercado de medicamentos;
* Apoio à elaboração de Termos de Referência;
* Padronização de cadastros de itens;
* Integração com sistemas de compras públicas;
* Construção de dashboards de medicamentos;
* Enriquecimento de bases de contratação pública;
* Análises de compras do Sistema Único de Saúde (SUS).

## Público-Alvo

* Analistas de Dados;
* Analistas de Compras Públicas;
* Analistas de Orçamento;
* Gestores de Aquisições;
* Equipes de Business Intelligence;
* Desenvolvedores de soluções para o setor público;
* Profissionais envolvidos em planejamento e contratação de medicamentos.

## Boas Práticas

* Realizar extrações periódicas para manter a base atualizada.
* Validar os dados antes de sua utilização em processos críticos.
* Armazenar versões históricas para rastreabilidade e auditoria.
* Documentar alterações estruturais caso ocorram mudanças na fonte de dados.
* Garantir a conformidade com as políticas de uso e disponibilização dos dados governamentais.

## Licença

Este projeto tem finalidade de apoio às atividades de tratamento, análise e integração de dados oriundos do CATMAT, observando as políticas de uso dos dados públicos e as normas vigentes da Administração Pública Federal.
