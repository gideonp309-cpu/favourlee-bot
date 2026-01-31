import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from engine import SimulationEngine

sim = SimulationEngine()

# --- UI CONSTANTS ---
HEADER = "✨ *VORTEX PROTOCOL v2\.6*\n━━━━━━━━━━━━━━━━━━━━\n"
FOOTER = "\n━━━━━━━━━━━━━━━━━━━━\n📍 _Simulated Environment_"

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📊 Portfolio", callback_data='balance'),
         InlineKeyboardButton("💸 Withdraw", callback_data='withdraw')],
        [InlineKeyboardButton("🌐 Network Status", callback_data='status')]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (f"{HEADER}"
            f"👤 *Identity:* `{sim.safe(update.effective_user.first_name)}`\n"
            f"🛡️ *Node:* `Encrypted Hub`\n\n"
            f"Welcome to the future of paper trading\.")
    await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=main_menu_keyboard())

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # Removes the loading spinner on the button
    
    if query.data == 'balance':
        price = sim.get_market_data()
        text = (f"{HEADER}"
                f"💰 *Balance:* `${sim.safe(f'{sim.balance:,.2f}')} USDT`\n"
                f"₿ *BTC Price:* `${sim.safe(f'{price:,.2f}')}`\n"
                f"📈 *Pnl \(24h\):* `+4\.25%`{FOOTER}")
        await query.edit_message_text(text, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=main_menu_keyboard())

    elif query.data == 'withdraw':
        tx = sim.generate_tx_hash()
        code = sim.generate_access_code()
        link = sim.get_scan_link(tx)
        text = (f"{HEADER}"
                f"📤 *Withdrawal Initialized*\n\n"
                f"🔑 *Access Key:* `{sim.safe(code)}`\n"
                f"🔗 *TXID:* [View on BTC Scan]({link})\n"
                f"⏳ *Estimate:* `~2 mins`{FOOTER}")
        await query.edit_message_text(text, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=main_menu_keyboard(), disable_web_page_preview=True)

    elif query.data == 'status':
        text = (f"{HEADER}"
                f"🟢 *System:* `Operational`\n"
                f"📡 *Latency:* `14ms`\n"
                f"🛰️ *Nodes:* `9,402 Active`{FOOTER}")
        await query.edit_message_text(text, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=main_menu_keyboard())

if __name__ == '__main__':
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    
    print("VORTEX 2026 is LIVE...")
    app.run_polling()
