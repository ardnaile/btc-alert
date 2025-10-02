# Bitcoin Alert Telegram Bot

Bot simples para alertas de preço de Bitcoin. Observa o preço e envia notificações quando um alerta configurado é disparado.

## 🚀 Funcionalidades

- Monitora o preço do Bitcoin a cada 15 minutos via [API CoinGecko](https://www.coingecko.com/pt-br).
- Envia alertas quando o preço atinge o valor configurado.
- Funciona 24/7 sem precisar de servidor local, usando GitHub Actions.

[![BTC Alert](https://github.com/ardnaile/btc-alert/actions/workflows/btc-alert.yml/badge.svg)](https://github.com/ardnaile/btc-alert/actions/workflows/btc-alert.yml)

## ⚙️ Como rodar via Github Actions

### 1. Fork o repositório

Clique em Fork no GitHub para ter seu próprio repositório.

### 2. Configurar Secrets

Vá em Settings → Secrets and variables → Actions → New repository secret e adicione:

- TOKEN → token do bot do Telegram
  - Crie um bot no Telegram com o BotFather
  - Siga as instruções do BotFather e copie o token.

- CHAT_ID → ID do chat para receber alertas
  - Envie uma mensagem para o bot e use a API getUpdates para descobrir o chat ID, ou use um bot helper.

### 3. Aguardar

- O workflow roda automaticamente a cada 15 minutos.

- Alertas chegarão no Telegram quando o preço atingir ou ultrapassar o valor configurado.

- Também é possível rodar manualmente em Actions → BTC Alert → Run workflow.
