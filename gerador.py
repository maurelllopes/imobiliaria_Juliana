import csv
import urllib.request

csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQQx0VU7pIYtm5ysb0mcPEcwRxrum9k7deANBFjtPg5fE1rZ_fxAIh9XsUEYehEUNli9ohBzFY9wxYp/pub?output=csv'

def gerar_site():
    print("Gerando site completo...")
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
                header {{ background-color: white; border-bottom: 3px solid var(--cor-dma); }}
                nav {{ background-color: var(--cor-dma); padding: 10px 0; }}
                .nav-link {{ color: white !important; font-weight: bold; margin-right: 20px; }}
                .imovel-card {{ border: 1px solid #eee; border-radius: 10px; transition: 0.3s; height: 100%; }}
                .imovel-card:hover {{ box-shadow: 0 10px 20px rgba(0,0,0,0.15); }}
                .btn-dma {{ background-color: var(--cor-dma); color: white; border: none; }}
                .filtro-box {{ background: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px solid #ddd; }}
            </style>
        </head>
        <body>
            <header class="p-3"><div class="container"><h1>DMA Imóveis</h1></div></header>
            <nav><div class="container d-flex"><a class="nav-link" href="#">Comprar</a><a class="nav-link" href="#">Alugar</a></div></nav>
            <div class="container mt-4">
                <div class="row">
                    <div class="col-md-3">
                        <div class="filtro-box">
                            <h4>FILTRAR</h4>
                            <input type="text" id="filtroInput" class="form-control mb-3" placeholder="Buscar imóvel...">
                        </div>
                    </div>
                    <div class="col-md-9">
                        <div class="row" id="listaImoveis">
        """
        
        for row in reader:
            html += f"""
                            <div class="col-md-4 mb-4 imovel-item">
                                <div class="imovel-card p-3">
                                    <img src="{row.get('foto', '')}" class="img-fluid rounded mb-2" alt="Foto">
                                    <h5>{row.get('titulo', 'Sem Título')}</h5>
                                    <p class="text-danger fw-bold">R$ {row.get('preco', '0')}</p>
                                    <button class="btn btn-dma w-100">Detalhar</button>
                                </div>
                            </div>
            """
        
        html += """
                        </div>
                    </div>
                </div>
            </div>
            <script>
                document.getElementById('filtroInput').addEventListener('keyup', function() {
                    let termo = this.value.toLowerCase();
                    document.querySelectorAll('.imovel-item').forEach(card => {
                        let titulo = card.querySelector('h5').innerText.toLowerCase();
                        card.style.display = titulo.includes(termo) ? '' : 'none';
                    });
                });
            </script>
        </body>
        </html>
        """
        with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
        print("Site completo gerado com sucesso!")

if __name__ == "__main__":
    gerar_site()