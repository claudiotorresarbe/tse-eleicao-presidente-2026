import time
import subprocess
from pathlib import Path

# variáveis
NUCLEOS = 4 # permite baixar 2 arquivos por vez
LINKS = './source/links.csv'

# inicio do programa
URL = []
DESTINO = Path("downloads") 
DESTINO.mkdir(exist_ok=True)

with open(LINKS,'r') as f:
    for x in f.readlines():
        linha = x.split('|')
        link = linha[0].strip()
        filename = link.split('/')[8].strip()
        URL.append([linha, filename])

processos = []

for y,z in URL:
    while len(processos) >= NUCLEOS:
        processos = [p for p in processos if p.poll() is None]
        time.sleep(0.2)

    link, filename = y[0].strip(), y[1].strip()
    p = subprocess.Popen(['python','download.py',f'{link}', f'{DESTINO/filename}'])
    
    processos.append(p)

for p in processos:
    p.wait()