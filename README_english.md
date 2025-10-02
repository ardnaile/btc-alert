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
