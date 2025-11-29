from pyrogram import Client, filters
import asyncio

api_id = 30995453
api_hash = "1a17c9a2593375bb589709b03ccc9497"
bot_token = "8350441669:AAHk22N62mHBf3hPD_-ujTjzIGJaBtuN6eE"
owner_id = 8488374637

app = Client("spam15", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

replies = {
    "Script1": "7MKB",
    "Script2": "MC B44G",
    "Script3": "K33P 5LI3NT G4R1B",
    "Script4": "5PP3D P4KDD K1D",
    "Script5": "CH4UDH4RY--0N--T0P✌️🥀"
}

data = {"active": False, "mode": "all", "user": "", "script": "Script1"}

@app.on_message(filters.private & filters.user(owner_id))
async def cmds(c, m):
    t = m.text.strip()
    if t == "Start":
        data["active"] = True
        await m.reply("Bot ON ✅\n15× reply ready")
    elif t == "Stop":
        data["active"] = False
        await m.reply("Bot OFF")
    elif t.startswith("@") and t != "@-@-@-@-@":
        data["mode"] = "one"
        data["user"] = t[1:]
        await m.reply(f"Sirf @{data['user']} ko 15× reply")
    elif t == "@-@-@-@-@":
        data["mode"] = "all"
        await m.reply("Sabko 15× reply")
    elif t in replies:
        data["script"] = t
        await m.reply(f"Script → {t}\n→ {replies[t]}")

@app.on_message(filters.private & ~filters.user(owner_id))
async def spam(c, m):
    if not data["active"]: return
    if data["mode"] == "one" and m.from_user.username != data["user"]: return
    txt = replies[data["script"]]
    for i in range(15):
        await c.send_message(m.chat.id, txt)
        await asyncio.sleep(4)

app.run()
