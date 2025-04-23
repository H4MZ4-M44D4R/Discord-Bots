# Discord-Bots Controller

A lightweight Python tool to control multiple Discord bots simultaneously — ideal for tasks like having bots join and leave voice channels in unison.

This example includes **14 bots**, each running from a separate script, all launched together via `main.py`.

---

## 🚀 Features

- Control multiple bots with a single command  
- Bots perform synchronized actions (e.g., join/leave VC)  
- Simple setup using `.env` for token management  
- Easily extendable — add more bots if needed  

---

## 🗂️ Project Structure

```
Discord-Bots/
├── bots/
│   ├── bot1.py
│   ├── bot2.py
│   ├── ...
│   └── bot14.py
├── .env
├── main.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/H4MZ4-M44D4R/Discord-Bots.git
cd Discord-Bots
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your bot tokens

Create or edit the `.env` file in the root directory and add your bot tokens like this:

```
DISCORD_BOT1_TOKEN=your_first_bot_token
DISCORD_BOT2_TOKEN=your_second_bot_token
...
DISCORD_BOT14_TOKEN=your_fourteenth_bot_token
```

### 4. Run all bots

```bash
python main.py
```

---

## 🧠 Notes

- Ensure all bots are invited to your server and have the necessary permissions.
- You can customize each bot's behavior by modifying the respective `botX.py` file inside the `bots/` folder.

