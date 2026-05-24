import csv
import urllib.request

csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQQx0VU7pIYtm5ysb0mcPEcwRxrum9k7deANBFjtPg5fE1rZ_fxAIh9XsUEYehEUNli9ohBzFY9wxYp/pub?output=csv'
##
def gerar_site():
    print("Gerando site profissional...")
    with urllib.request.urlopen(csv_url) as response:
        linhas = [l.decode('utf-8') for l in response.readlines()]
        reader = csv.DictReader(linhas)

        html = """
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                :root { --cor-dma: #a93226; }
                header { background-color: white; border-bottom: 3px solid var(--cor-dma); }
                nav { background-color: var(--cor-dma); }
                .nav-link { color: white !important; font-weight: bold; }
                .imovel-card { border: 1px solid #ddd; border-radius: 10px; overflow: hidden; transition: 0.3s; }
                .imovel-card:hover { box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
                .btn-dma { background-color: var(--cor-dma); color: white; border-radius: 0; }
                .filtro-box { background: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6; }
            </style>
        </head>
        <body>
            <header class="p-3">
                <div class="container"><h1>DMA Imóveis</h1></div>
            </header>
            <nav class="navbar navbar-expand-lg">
                <div class="container"><a class="nav-link" href="#">Principal</a><a class="nav-link" href="#">Comprar</a><a class="nav-link" href="#">Alugar</a></div>
            </nav>
            <div class="container mt-4">
                <div class="row">
                    <div class="col-md-3">
                        <div class="filtro-box">
                            <h4>FILTRAR</h4>
                            <input type="text" class="form-control mb-2" placeholder="Referência...">
                            <select class="form-select mb-2"><option>Venda</option><option>Aluguel</option></select>
                            <button class="btn btn-dma w-100">Buscar</button>
                        </div>
                    </div>
                    <div class="col-md-9">
                        <div class="row">
        """
        
        for row in reader:
            html += f"""
                            <div class="col-md-4 mb-4">
                                <div class="imovel-card">
                                    <img src="{row.get('foto', '')}" class="img-fluid" alt="Imóvel">
                                    <div class="p-3">
                                        <h6 class="text-muted">Casa</h6>
                                        <h5>{row['titulo']}</h5>
                                        <p class="text-danger fw-bold">R$ {row['preco']}</p>
                                        <button class="btn btn-dma w-100">Detalhar</button>
                                    </div>
                                </div>
                            </div>
            """
        
        html += """
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Site gerado com sucesso!")

if __name__ == "__main__":
    gerar_site()