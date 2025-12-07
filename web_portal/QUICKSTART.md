# 🧬 AMPidentifier Web Portal - Resumo do Projeto

## ✅ O que foi criado

Um portal web completo e elegante para o AMPidentifier com design "liquid glass" inspirado na Apple.

### Arquivos Criados:

```
web_portal/
├── index.html              # Página inicial com features e métricas
├── predict.html            # Interface de predição
├── about.html              # Informações detalhadas do projeto
├── app.py                  # Backend Flask (para uso local/API)
├── requirements.txt        # Dependências do backend
├── README.md              # Documentação completa
├── DEPLOY.md              # Guia de deploy passo-a-passo
└── static/
    ├── css/
    │   └── style.css      # Design system completo com liquid glass
    └── js/
        └── main.js        # Interatividade e animações
```

## 🎨 Características do Design

### Visual
- ✨ **Liquid Glass Effect**: Glassmorphism com blur e transparência
- 🎭 **Animações Suaves**: Hover effects responsivos ao movimento do mouse
- 🌈 **Gradientes Vibrantes**: Paleta inspirada em temas biológicos
- 🌙 **Dark Mode**: Design escuro moderno e elegante
- 📱 **Totalmente Responsivo**: Desktop, tablet e mobile

### Funcionalidades
- 🏠 **Home Page**: Hero section, grid de features, tabela de performance
- 🔬 **Predict Page**: Input FASTA, seleção de modelo, resultados tabulados
- 📊 **Tabelas Elegantes**: Resultados bem organizados com download CSV
- ℹ️ **About Page**: Informações completas sobre o projeto
- ⚡ **Loading States**: Feedback visual durante processamento
- 🎯 **Validação**: Tratamento de erros e mensagens claras

## 🚀 Como Usar

### Opção 1: Visualizar Localmente (Agora!)

O servidor já está rodando! Abra seu navegador em:
```
http://localhost:8080/index.html
```

Para parar o servidor:
```bash
# Pressione Ctrl+C no terminal
```

### Opção 2: Deploy no GitHub Pages

Siga o guia completo em `web_portal/DEPLOY.md`

**Resumo rápido:**

1. **Criar repositório `ampidentifier` no GitHub**

2. **Copiar arquivos para o repositório:**
   ```bash
   # Na raiz do repositório ampidentifier
   cp web_portal/index.html .
   cp web_portal/predict.html .
   cp web_portal/about.html .
   cp -r web_portal/static .
   ```

3. **Commit e push:**
   ```bash
   git add .
   git commit -m "Add AMPidentifier web portal"
   git push origin main
   ```

4. **Ativar GitHub Pages:**
   - Settings → Pages
   - Source: main branch, / (root)
   - Save

5. **Acessar:**
   ```
   https://madsondeluna.github.io/ampidentifier
   ```

## ⚙️ Configuração da API (Opcional)

Por padrão, o site usa **dados mockados** para demonstração.

Para predições reais, você precisa hospedar o backend separadamente:

### Opção Recomendada: Render.com (Grátis)

1. Crie conta em https://render.com
2. Crie Web Service conectado ao repositório
3. Configure:
   - Build: `pip install -r web_portal/requirements.txt`
   - Start: `cd web_portal && gunicorn app:app`
4. Anote a URL da API
5. Edite `predict.html` linha ~280:
   ```javascript
   const API_URL = 'https://sua-api.onrender.com/api/predict';
   ```

Veja instruções detalhadas em `web_portal/DEPLOY.md`

## 📁 Estrutura de Deploy para GitHub Pages

```
seu-repositorio-ampidentifier/
├── index.html          # ← Copiar de web_portal/
├── predict.html        # ← Copiar de web_portal/
├── about.html          # ← Copiar de web_portal/
└── static/             # ← Copiar de web_portal/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

**IMPORTANTE**: Copie APENAS os arquivos HTML e a pasta `static/` para a raiz do repositório GitHub Pages.

## 🎯 Próximos Passos

1. ✅ **Testar localmente** - Já está rodando em http://localhost:8080
2. 📤 **Deploy no GitHub Pages** - Siga `DEPLOY.md`
3. 🔌 **Configurar API** (opcional) - Para predições reais
4. 🎨 **Personalizar** - Ajuste cores/textos conforme necessário
5. 📢 **Compartilhar** - Divulgue para a comunidade científica!

## 🐛 Problemas Comuns

### CSS não carrega no GitHub Pages
**Solução**: Verifique que `static/` está na raiz do repositório

### Predições não funcionam
**Solução**: Normal! Use dados mockados ou configure API backend

### Animações lentas
**Solução**: Ajuste `--transition-*` em `static/css/style.css`

## 📚 Documentação

- `README.md` - Documentação completa do portal
- `DEPLOY.md` - Guia passo-a-passo de deploy
- `../README.md` - Documentação do AMPidentifier CLI

## 🎨 Personalização

### Mudar Cores
Edite `static/css/style.css`:
```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    /* Suas cores aqui */
}
```

### Mudar Conteúdo
Edite os arquivos HTML diretamente. O design é modular e fácil de modificar.

## 📞 Suporte

- **Issues**: https://github.com/madsondeluna/AMPIdentifier/issues
- **Email**: madsondeluna@gmail.com

## 🎉 Pronto!

Seu portal AMPidentifier está pronto para uso!

**Teste agora**: http://localhost:8080/index.html

**Deploy**: Siga `DEPLOY.md` para colocar online

---

**Desenvolvido com ❤️ usando design liquid glass inspirado na Apple**
