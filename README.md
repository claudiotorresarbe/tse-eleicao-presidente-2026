# TSE - Eleição Presidente 2026

Repositório com scripts para download dos **arquivos oficiais de totalização** das Eleições 2026 disponibilizados pelo Tribunal Superior Eleitoral (TSE).

## Estrutura do projeto

```
tse-eleicao-presidente-2026/
├── source/
│   └── links.csv          # Lista de URLs oficiais do TSE
├── download.py            # Script responsável por baixar um arquivo
├── run.py                 # Orquestrador (controla downloads paralelos)
└── README.md
```

## Como usar

### 1. Clonar o repositório

```bash
git clone https://github.com/claudiotorresarbe/tse-eleicao-presidente-2026.git
cd tse-eleicao-presidente-2026
```

### 2. Requisitos

```bash
pip install requests
```

### 3. Executar o download

```bash
python run.py
```

O script irá:
- Ler todos os links do arquivo `source/links.csv`
- Baixar os arquivos em paralelo (padrão: 2 downloads simultâneos)
- Salvar tudo na pasta `downloads/`

### 4. Configurações

Você pode alterar a quantidade de downloads simultâneos editando a variável no arquivo `run.py`:

```python
NUCLEOS = 2   # Altere para 4, 6, 8 etc. conforme sua conexão
```

## Fonte dos dados

Os arquivos são baixados diretamente do CDN oficial do TSE:

```
https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/arqurnatot/
```

## Observações

- Os arquivos são grandes. Certifique-se de ter espaço em disco suficiente.
- O script ignora arquivos que já existem na pasta `downloads/`.
- Em caso de erro de conexão, basta executar novamente o `run.py`.

## Licença

Os dados pertencem ao **Tribunal Superior Eleitoral**.  
Este repositório apenas facilita o download automatizado dos arquivos públicos.
```