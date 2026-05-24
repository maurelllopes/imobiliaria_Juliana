import csv
import urllib.request

# Link da sua planilha publicada
csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQQx0VU7pIYtm5ysb0mcPEcwRxrum9k7deANBFjtPg5fE1rZ_fxAIh9XsUEYehEUNli9ohBzFY9wxYp/pub?output=csv'

def gerar_site():
    print("Gerando site com estrutura ajustada...")
    try:
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
        .top-bar {{ background: white; padding: 20px 0; border-bottom: 1px solid #eee; }}
        .navbar-dma {{ background-color: var(--cor-dma); color: white; padding: 15px 0; font-weight: bold; display: flex; justify-content: center; gap: 80px; }}
        .nav-item {{ color: white !important; text-decoration: none; font-size: 1rem; }}
        .hero-image {{ width: 100%; height: 400px; object-fit: cover; }}
        /* Buscador ajustado para ficar abaixo do menu */
        .search-box {{ background: white; padding: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin: 20px auto; border-radius: 4px; max-width: 1100px; }}
        .imovel-card {{ background: white; border: 1px solid #e0e0e0; border-radius: 4px; height: 100%; transition: 0.3s; }}
        .btn-detalhes {{ background-color: var(--cor-dma); color: white; border-radius: 0; }}
        .tag-tipo {{ background: var(--cor-dma); color: white; padding: 3px 10px; font-size: 0.75rem; font-weight: bold; display: inline-block; margin-bottom: 10px; }}
    </style>
</head>
<body>
    <div class="top-bar text-center"><h1>DMA Imóveis</h1></div>
    <nav class="navbar-dma">
        <a href="#" class="nav-item">Principal</a>
        <a href="#" class="nav-item">Comprar</a>
        <a href="#" class="nav-item">Alugar</a>
        <a href="#" class="nav-item">Informações</a>
        <a href="#" class="nav-item">Contato</a>
    </nav>
    
    <div class="container">
        <div class="search-box">
            <div class="row g-2 align-items-center">
                <div class="col-md-3"><input type="text" class="form-control" placeholder="Ref..."></div>
                <div class="col-md-3"><select class="form-select"><option>Operação</option></select></div>
                <div class="col-md-2"><select class="form-select"><option>Maricá</option></select></div>
                <div class="col-md-3"><select class="form-select"><option>Bairros</option></select></div>
                <div class="col-md-1"><button class="btn btn-secondary w-100">🔍</button></div>
            </div>
        </div>
    </div>

    <img src="assets/hero-home.jpg" class="hero-image" alt="Destaque">
    
    <div class="container mt-5">
        <h4 class="mb-4">IMÓVEIS EM DESTAQUE</h4>
        <div class="row">
"""
            # Adiciona os cards dos imóveis
            for row in reader:
                html += f"""
            <div class="col-md-4 mb-4">
                <div class="imovel-card p-3">
                    <img src="{row.get('foto', '')}" class="img-fluid mb-3" alt="Imóvel">
                    <div class="tag-tipo">{row.get('titulo', 'Imóvel')}</div>
                    <h5>{row.get('bairro', 'Centro')}</h5>
                    <p class="text-muted small">{row.get('descricao', '')}</p>
                    <hr>
                    <div class="row text-center mb-3">
                        <div class="col"><strong>{row.get('quartos', '0')}</strong><br><small>Quartos</small></div>
                        <div class="col"><strong>{row.get('suites', '0')}</strong><br><small>Suítes</small></div>
                        <div class="col"><strong>{row.get('vagas', '0')}</strong><br><small>Vagas</small></div>
                    </div>
                    <div class="d-flex justify-content-between mb-3">
                        <small>Ref: {row.get('ref', '-')}</small>
                        <small>Área: {row.get('area', '0')}m²</small>
                    </div>
                    <p class="text-danger fw-bold fs-5">R$ {row.get('preco', '0')}</p>
                    <button class="btn btn-detalhes w-100">Detalhar</button>
                </div>
            </div>
"""
            html += "</div></div></body></html>"
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print("Site gerado com sucesso!")
            
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    gerar_site()