import csv
import urllib.request

csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQQx0VU7pIYtm5ysb0mcPEcwRxrum9k7deANBFjtPg5fE1rZ_fxAIh9XsUEYehEUNli9ohBzFY9wxYp/pub?output=csv'

def gerar_site():
    print("Baixando dados e gerando site...")
    with urllib.request.urlopen(csv_url) as response:
        linhas = [l.decode('utf-8') for l in response.readlines()]
        reader = csv.DictReader(linhas)

        html = """
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body { font-family: sans-serif; margin: 0; padding: 0; background: #f0f2f5; }
                header { background: #1a73e8; color: white; padding: 20px; text-align: center; }
                nav { background: #333; color: white; padding: 10px; text-align: center; }
                nav a { color: white; margin: 0 15px; text-decoration: none; }
                .container { max-width: 800px; margin: 20px auto; min-height: 400px; }
                .imovel { background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
                footer { background: #333; color: white; text-align: center; padding: 15px; margin-top: 20px; }
            </style>
        </head>
        <body>
            <header>
                <h1>Imobiliária da Família</h1>
            </header>
            <nav>
                <a href="#">Início</a>
                <a href="#">Comprar</a>
                <a href="#">Alugar</a>
                <a href="#">Contato</a>
            </nav>
            <div class="container">
        """
        
        # Aqui o loop insere os imóveis dinamicamente
        for row in reader:
            html += f"""
            <div class="imovel">
                <h2>{row['titulo']}</h2>
                <p><strong>Preço:</strong> R$ {row['preco']}</p>
                <p>{row['descricao']}</p>
            </div>
            """
        
        # Fechamento do container, rodapé e documento
        html += """
            </div>
            <footer>
                <p>&copy; 2026 Imobiliária da Família - Todos os direitos reservados</p>
            </footer>
        </body>
        </html>
        """

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Site gerado com Header, Menu e Rodapé!")

if __name__ == "__main__":
    gerar_site()