# 🚀 Binance Futures CLI Trading Bot (Testnet)

## 📌 Overview

This is a simple CLI-based trading bot built in Python that interacts with the Binance Futures Testnet API.
It allows users to place MARKET and LIMIT orders directly from the command line.

---

## ⚙️ Features

* Place MARKET orders
* Place LIMIT orders
* CLI-based input (user-friendly)
* Logging for debugging (`bot.log`)
* Secure API request signing

---

## 🛠️ Tech Stack

* Python
* Requests library
* Binance Futures Testnet API

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py      # API interaction logic
│   ├── orders.py      # Order execution logic
│
├── cli.py             # Command-line interface
├── config.py          # API keys and config
├── logger.py          # Logging setup
├── requirements.txt
└── README.md
```

---

## 🔑 Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-url>
cd trading_bot
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Setup environment variables

Create a `.env` file in the root directory:

```
API_KEY=your_api_key
SECRET_KEY=your_secret_key
```

---

### 4️⃣ Run the bot

#### ✅ Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

#### ✅ Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📊 Logging

All logs are stored in:

```
bot.log
```

This helps in debugging and tracking order activity.

---

## ⚠️ Notes

* This project uses Binance Futures **Testnet**, not real funds.
* API keys must be generated from Binance Testnet.
* LIMIT orders require a price parameter.

---

## 🧠 Learnings

* API integration using Python
* CLI-based application design
* Request signing and authentication
* Logging and error handling

---

## 📬 Future Improvements

* Add Stop-Limit orders
* Add better validation for inputs
* Improve error handling
* Add unit tests

---

## 🙌 Author

Built as part of an internship assignment to demonstrate API integration, clean code structure, and CLI-based tools.
