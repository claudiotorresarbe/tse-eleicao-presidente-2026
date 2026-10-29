import sys
import requests

def download(link, filename):
    with requests.get(link, stream=True, timeout=60) as d:
        d.raise_for_status()
        try:
            with open(filename,'wb') as f:
                for chunk in d.iter_content(chunk_size=65536):
                    if chunk:
                        f.write(chunk)
            return 'ok'
        
        except Exception as e:
        
            return e

if __name__ == '__main__':

    link, filename = sys.argv[1], sys.argv[2]
    
    r = download(link,filename)

    if r == 'ok':
        print(f'Arquivo {filename} concluído')
    else:
        print(f'Erro {r} no arquivo {filename}')
