import csv
import urllib.request

csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQQx0VU7pIYtm5ysb0mcPEcwRxrum9k7deANBFjtPg5fE1rZ_fxAIh9XsUEYehEUNli9ohBzFY9wxYp/pub?output=csv'

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
                .btn-detalhes { background-color: #a93226; color: white; }
                .imovel-card { border: 1px solid #ddd; margin-bottom: 20px; padding: 15px; border-radius: 5px; }
            </style>
        </head>
        <body>
            <header class="bg-light p-3 border-bottom">
                <div class="container"><h1>DMA Imóveis</h1></div>
            </header>
            <div class="container mt-4">
                <div class="row">
                    <div class="col-md-3">
                        <h4>FILTRAR</h4>
                        <div class="p-3 bg-light border">Filtros aqui...</div>
                    </div>
                    <div class="col-md-9">
                        <div class="row">
        """
        
        for row in reader:
            html += f"""
                            <div class="col-md-6">
                                <div class="imovel-card">
                                    <img src="{row['foto']}" class="img-fluid" alt="Imóvel">
                                    <h5>{row['titulo']}</h5>
                                    <p class="text-danger fw-bold">R$ {row['preco']}</p>
                                    <p>{row['descricao']}</p>
                                    <button class="btn btn-detalhes w-100">Detalhar</button>
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
        print("Site gerado com layout estilo DMA!")

if __name__ == "__main__":
    gerar_site()