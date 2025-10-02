[🇧🇷 Português](#funcionalidades) | [🇺🇸 English](#features)

# Bot Telegram para alertas de preço do ₿itcoin 

Bot simples para alertas de preço de Bitcoin. Observa o preço e envia notificações quando um alerta configurado é disparado.

## 🚀 Funcionalidades

- Monitora o preço do Bitcoin a cada 15 minutos via [API CoinGecko](https://www.coingecko.com/pt-br).
- Envia alertas via bot no Telegram quando o preço atinge o valor configurado.
- Funciona 24/7 sem precisar de servidor local, usando GitHub Actions.

[![BTC Alert](https://github.com/ardnaile/btc-alert/actions/workflows/btc-alert.yml/badge.svg)](https://github.com/ardnaile/btc-alert/actions/workflows/btc-alert.yml)

## ⚙️ Como copiar esse projeto para usar suas funcioalidades

### 1. Fork o repositório

Clique em Fork no GitHub para ter seu próprio repositório.

### 2. Configurar Secrets

Vá em Settings → Secrets and variables → Actions → New repository secret e adicione:

- TOKEN → token do bot do Telegram
  - Crie um bot no Telegram com o [BotFather](https://t.me/botfather)
  - Siga as instruções do BotFather e copie o token.

- CHAT_ID → ID do chat para receber alertas
  - Abra o Telegram e pesquise por [@UserInfeBot](https://web.telegram.org/k/#@UserInfeBot)
  - Inicie uma conversa com ele clicando em Start.
  - O bot vai te enviar uma mensagem mostrando seu User ID.
  - Esse User ID é o valor que você usa como CHAT_ID no workflow.
  
💡 Dica para grupos:

- Adicione o bot a um grupo para que várias pessoas recebam os alertas.
- O ID do grupo é um número negativo. Pode ser obtido pela URL do grupo ou via `API getUpdates`.

### 3. Aguardar

- O workflow roda automaticamente a cada 15 minutos.

- Alertas chegarão no Telegram quando o preço atingir ou ultrapassar o valor configurado.

- Também é possível rodar manualmente em Actions → BTC Alert → Run workflow.

## ⚠ Editando os alertas (alert.json)
O arquivo alert.json define os alertas de preço do BTC. Cada alerta possui:

| Campo    | Descrição                                                                       |
| -------- | ------------------------------------------------------------------------------- |
| `id`     | Identificador único do alerta                                                   |
| `type`   | Tipo do alerta: `"above"` (acima), `"below"` (abaixo) ou outros tipos especiais |
| `price`  | Preço que dispara o alerta                                                      |
| `active` | `true` para ativar, `false` para desativar                                      |
| `once`   | `true` para disparar apenas uma vez, `false` para alertas contínuos             |

**Exemplo rápido**

```
{
  "id": 1,
  "type": "above",
  "price": 116000,
  "active": true,
  "once": false
}

```
- Altere o price para definir o valor que deseja monitorar.

- Mude active para false se quiser desativar temporariamente o alerta.

- Use once: true se o alerta deve disparar apenas uma vez.

💡 Dica: Cada novo alerta precisa de um id único.

---

# Bitcoin Alert Telegram Bot

A simple bot for Bitcoin price alerts. It monitors the price and sends notifications via Telegram when a configured alert is triggered.

---

## 🚀 Features

* Monitors the Bitcoin price every 15 minutes via **CoinGecko API**.
* Sends alerts via a Telegram bot when the price reaches the configured value.
* Runs 24/7 without a local server, using **GitHub Actions**.

---

## ⚙️ How to use this project

### 1. Fork the repository

Click **Fork** on GitHub to create your own copy of the repository.

---

### 2. Configure Secrets

Go to **Settings → Secrets and variables → Actions → New repository secret** and add:

* **TOKEN** → your Telegram bot token

  1. Create a bot on Telegram using [BotFather](https://t.me/botfather).
  2. Follow the instructions and copy the token.

* **CHAT_ID** → the chat ID where alerts will be sent

  1. Open Telegram and chat with [@UserInfoBot](https://t.me/userinfobot).
  2. Click **Start**.
  3. The bot will show your **User ID**. Use this number as `CHAT_ID`.

💡 **Tip for groups:**

* Add the bot to a Telegram group to send alerts to multiple people.
* The **group ID is a negative number** and can be obtained from the group URL or via the `getUpdates` API.

---

### 3. Wait

* The workflow runs automatically every 15 minutes.
* Alerts will arrive in Telegram when the price reaches or exceeds the configured value.
* You can also run it manually in **Actions → BTC Alert → Run workflow**.

---

## ⚠ Editing alerts (`alert.json`)

The `alert.json` file defines Bitcoin price alerts. Each alert has:

| Field    | Description                                                                                    |
| -------- | ---------------------------------------------------------------------------------------------- |
| `id`     | Unique identifier for the alert                                                                |
| `type`   | Alert type: `"above"` (price goes above), `"below"` (price goes below), or other special types |
| `price`  | Price that triggers the alert                                                                  |
| `active` | `true` to enable, `false` to disable                                                           |
| `once`   | `true` to trigger only once, `false` for continuous alerts                                     |

#### Quick example

```json
{
  "id": 1,
  "type": "above",
  "price": 116000,
  "active": true,
  "once": false
}
```

* Change `price` to set the target price.
* Set `active` to `false` to temporarily disable an alert.
* Use `once: true` if the alert should trigger only once.

💡 **Tip:** Each new alert must have a **unique `id`**.

