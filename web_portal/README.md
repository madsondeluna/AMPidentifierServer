# AMPidentifier Web Portal

Portal web elegante para o AMPidentifier com design "liquid glass" inspirado na Apple.

## 🌐 Acesso Online

O portal está disponível em: **https://madsondeluna.github.io/ampidentifier**

## 📁 Estrutura

```
web_portal/
├── index.html          # Página inicial
├── predict.html        # Interface de predição
├── about.html          # Sobre o projeto
├── static/
│   ├── css/
│   │   └── style.css   # Estilos com efeito liquid glass
│   └── js/
│       └── main.js     # Interatividade e animações
└── app.py             # Backend Flask (para uso local)
```

## 🎨 Características do Design

- **Liquid Glass Effect**: Efeito glassmorphism com blur e transparência
- **Animações Suaves**: Transições e hover effects responsivos ao mouse
- **Gradientes Vibrantes**: Paleta de cores inspirada em temas biológicos/moleculares
- **Responsivo**: Funciona perfeitamente em desktop, tablet e mobile
- **Dark Mode**: Design escuro moderno e elegante

## 🚀 Deploy no GitHub Pages

### Opção 1: Hospedar apenas o frontend (Modo Demonstração)

1. Copie os arquivos do `web_portal/` para um repositório chamado `ampidentifier`
2. Ative o GitHub Pages nas configurações do repositório
3. O site estará disponível em `https://madsondeluna.github.io/ampidentifier`

**Nota**: Neste modo, a predição usa dados mockados para demonstração.

### Opção 2: Frontend + Backend API Separado

Para predições reais, você precisa hospedar o backend Python separadamente:

#### Backend (escolha uma opção):

**A. Render.com (Recomendado - Grátis)**
1. Crie conta no [Render](https://render.com)
2. Crie um novo Web Service
3. Conecte ao repositório
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn web_portal.app:app`
5. Anote a URL da API (ex: `https://ampidentifier-api.onrender.com`)

**B. Heroku**
1. Instale Heroku CLI
2. Crie app: `heroku create ampidentifier-api`
3. Deploy: `git push heroku main`

**C. Railway.app**
1. Conecte repositório no Railway
2. Configure variáveis de ambiente
3. Deploy automático

#### Frontend:
1. No arquivo `predict.html`, atualize a linha:
   ```javascript
   const API_URL = 'https://sua-api.onrender.com/api/predict';
   ```
2. Descomente o código de chamada real da API
3. Comente o código de dados mockados

## 🛠️ Desenvolvimento Local

### Apenas Frontend (HTML/CSS/JS)
```bash
cd web_portal
python3 -m http.server 8000
```
Acesse: http://localhost:8000

### Com Backend Flask
```bash
# Instalar dependências
pip install flask pandas

# Executar servidor
cd web_portal
python app.py
```
Acesse: http://localhost:5000

## 📦 Dependências do Backend

```txt
Flask==3.0.0
pandas==2.1.0
```

## 🔧 Configuração da API

Para conectar o frontend ao backend, edite `predict.html`:

```javascript
// Substitua pela URL da sua API
const API_URL = 'https://sua-api-backend.com/api/predict';
```

## 🎯 Funcionalidades

### Página Inicial (`index.html`)
- Hero section com título animado
- Grid de features com ícones
- Tabela de performance dos modelos
- Seção "Como Funciona"
- Call-to-action

### Página de Predição (`predict.html`)
- Input de sequências FASTA
- Botão para carregar exemplo
- Seleção de modelo (RF, SVM, GB, Ensemble)
- Tabelas de resultados elegantes
- Download de resultados em CSV
- Estados de loading e erro

### Página About (`about.html`)
- Informações detalhadas sobre o projeto
- Fluxo de trabalho
- Características principais
- Performance e métricas
- Equipe e colaboradores
- Financiamento e propriedade intelectual
- Como citar

## 🎨 Personalização

### Cores
Edite as variáveis CSS em `static/css/style.css`:

```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    /* ... */
}
```

### Animações
Ajuste as transições em `static/css/style.css`:

```css
:root {
    --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    /* ... */
}
```

## 📱 Responsividade

O design é totalmente responsivo com breakpoints em:
- Desktop: > 768px
- Tablet: 768px
- Mobile: < 768px

## 🐛 Troubleshooting

### Problema: Predições não funcionam
**Solução**: Verifique se a API está configurada corretamente ou use o modo demonstração com dados mockados.

### Problema: Estilos não carregam
**Solução**: Verifique os caminhos relativos dos arquivos CSS/JS.

### Problema: CORS error ao chamar API
**Solução**: Configure CORS no backend Flask:
```python
from flask_cors import CORS
CORS(app)
```

## 📄 Licença

Este projeto segue a mesma licença do AMPidentifier principal.

## 👥 Autores

- **Madson A. de Luna Aragão** - Desenvolvimento e Design
- Veja [about.html](about.html) para a equipe completa

## 🔗 Links

- [Repositório Principal](https://github.com/madsondeluna/AMPIdentifier)
- [Documentação](https://github.com/madsondeluna/AMPIdentifier/blob/main/README.md)
- [Issues](https://github.com/madsondeluna/AMPIdentifier/issues)
