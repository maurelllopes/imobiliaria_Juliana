import csv
import urllib.request

csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQQx0VU7pIYtm5ysb0mcPEcwRxrum9k7deANBFjtPg5fE1rZ_fxAIh9XsUEYehEUNli9ohBzFY9wxYp/pub?output=csv'

def gerar_site():
    print("Gerando site estilo DMA...")
    with urllib.request.urlopen(csv_url) as response:
        linhas = [l.decode('utf-8') for l in response.readlines()]
        reader = list(csv.DictReader(linhas))

        html = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                :root {{ --cor-dma: #a93226; }}
                body {{ background-color: #f9f9f9; }}
                .header-dma {{ background-color: white; border-bottom: 4px solid var(--cor-dma); padding: 20px 0; }}
                .navbar-dma {{ background-color: var(--cor-dma); color: white; padding: 10px 0; font-weight: bold; }}
                .imovel-card {{ background: white; border: 1px solid #e0e0e0; border-radius: 4px; height: 100%; transition: 0.3s; }}
                .imovel-card:hover {{ box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
                .tag-tipo {{ background: var(--cor-dma); color: white; padding: 2px 8px; font-size: 0.8rem; display: inline-block; }}
                .btn-detalhes {{ background-color: var(--cor-dma); color: white; border-radius: 0; }}
            </style>
        </head>
        <body>
            <header class="header-dma text-center"><h1>DMA Imóveis</h1></header>
            <nav class="navbar-dma text-center">Principal | Comprar | Alugar | Contato</nav>
            <div class="container mt-5">
                <h4 class="mb-4">IMÓVEIS EM DESTAQUE</h4>
                <div class="row">
        """
        
        for row in reader:
            html += f"""
                    <div class="col-md-4 mb-4">
                        <div class="imovel-card p-3">
                            <img src="{row.get('foto', '')}" class="img-fluid mb-3" alt="Imóvel">
                            <div class="tag-tipo">{row.get('tipo', 'Casa')}</div>
                            <h5 class="mt-2">{row.get('titulo', 'Sem Título')}</h5>
                            <p class="text-muted small">{row.get('bairro', 'Maricá - RJ')}</p>
                            <hr>
                            <p class="fw-bold">R$ {row.get('preco', '0')}</p>
                            <button class="btn btn-detalhes w-100">Detalhar</button>
                        </div>
                    </div>
            """
        
        html += """
                </div>
            </div>
        </body>
        </html>
        """
        with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
        print("Site gerado com sucesso!")

if __name__ == "__main__":
    gerar_site()