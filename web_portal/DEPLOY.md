# 🚀 Guia Rápido de Deploy - GitHub Pages

## Passo 1: Preparar Repositório

```bash
# Criar novo repositório no GitHub chamado 'ampidentifier'
# Ou usar um existente

# Clone o repositório
git clone https://github.com/madsondeluna/ampidentifier.git
cd ampidentifier
```

## Passo 2: Copiar Arquivos do Portal

```bash
# Copie APENAS os arquivos necessários para GitHub Pages:
cp -r web_portal/index.html .
cp -r web_portal/predict.html .
cp -r web_portal/about.html .
cp -r web_portal/static .

# Estrutura final deve ser:
# ampidentifier/
# ├── index.html
# ├── predict.html
# ├── about.html
# └── static/
#     ├── css/
#     │   └── style.css
#     └── js/
#         └── main.js
```

## Passo 3: Commit e Push

```bash
git add .
git commit -m "Add AMPidentifier web portal"
git push origin main
```

## Passo 4: Ativar GitHub Pages

1. Vá para o repositório no GitHub
2. Clique em **Settings** (Configurações)
3. No menu lateral, clique em **Pages**
4. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/ (root)`
5. Clique em **Save**

## Passo 5: Aguardar Deploy

- O GitHub Pages levará alguns minutos para fazer o deploy
- Você receberá uma notificação quando estiver pronto
- O site estará disponível em: `https://madsondeluna.github.io/ampidentifier`

## 📝 Notas Importantes

### Modo Demonstração
Por padrão, o site usa **dados mockados** para demonstração, pois GitHub Pages não suporta backend Python.

### Para Predições Reais

Você tem 3 opções:

#### Opção A: API no Render.com (Recomendado - Grátis)

1. **Criar conta no Render**
   - Acesse: https://render.com
   - Crie uma conta gratuita

2. **Criar Web Service**
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub
   - Configure:
     ```
     Name: ampidentifier-api
     Environment: Python 3
     Build Command: pip install -r web_portal/requirements.txt
     Start Command: cd web_portal && gunicorn app:app
     ```

3. **Aguardar Deploy**
   - Anote a URL (ex: `https://ampidentifier-api.onrender.com`)

4. **Atualizar Frontend**
   - Edite `predict.html` linha ~280:
   ```javascript
   const API_URL = 'https://ampidentifier-api.onrender.com/api/predict';
   ```
   - Descomente o código de API real (linhas ~290-300)
   - Comente o código mockado (linhas ~303-340)

5. **Commit e Push**
   ```bash
   git add predict.html
   git commit -m "Connect to Render API"
   git push origin main
   ```

#### Opção B: API no Heroku

```bash
# Instalar Heroku CLI
brew install heroku/brew/heroku  # macOS
# ou baixe de: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Criar app
heroku create ampidentifier-api

# Criar Procfile
echo "web: cd web_portal && gunicorn app:app" > Procfile

# Deploy
git add Procfile
git commit -m "Add Procfile for Heroku"
git push heroku main

# Obter URL
heroku open
```

#### Opção C: API no Railway.app

1. Acesse: https://railway.app
2. Conecte repositório GitHub
3. Configure:
   - Root Directory: `web_portal`
   - Start Command: `gunicorn app:app`
4. Deploy automático

### CORS Configuration

Se tiver problemas de CORS, adicione ao `web_portal/app.py`:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Adicione esta linha
```

## 🔍 Verificar Deploy

Após o deploy, verifique:

1. ✅ Site carrega: `https://madsondeluna.github.io/ampidentifier`
2. ✅ Navegação funciona entre páginas
3. ✅ Estilos carregam corretamente
4. ✅ Animações funcionam
5. ✅ Formulário de predição aparece
6. ⚠️ Predições (modo demo ou API real, dependendo da configuração)

## 🐛 Troubleshooting

### Problema: Página 404
**Causa**: GitHub Pages ainda não fez deploy ou branch incorreta
**Solução**: Aguarde alguns minutos, verifique configurações do Pages

### Problema: CSS não carrega
**Causa**: Caminhos incorretos
**Solução**: Verifique que `static/` está na raiz do repositório

### Problema: API não responde
**Causa**: Backend não está rodando ou URL incorreta
**Solução**: 
- Verifique logs do Render/Heroku
- Teste a API diretamente: `curl https://sua-api.com/api/predict`
- Verifique CORS

### Problema: Erro CORS
**Causa**: Backend não permite requisições do GitHub Pages
**Solução**: Adicione `flask-cors` ao backend

## 📊 Monitoramento

### GitHub Pages
- Status: https://github.com/madsondeluna/ampidentifier/deployments

### Render (se usar)
- Dashboard: https://dashboard.render.com
- Logs em tempo real disponíveis

### Heroku (se usar)
```bash
heroku logs --tail -a ampidentifier-api
```

## 🎉 Pronto!

Seu portal AMPidentifier está online em:
**https://madsondeluna.github.io/ampidentifier**

Compartilhe com a comunidade científica! 🧬
