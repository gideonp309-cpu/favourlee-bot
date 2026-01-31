import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from engine import SimulationEngine

sim = SimulationEngine()

# --- UI COMPONENTS ---
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("📊 Portfolio", callback_data='p'), InlineKeyboardButton("💸 Withdraw", callback_data='w')],
        [InlineKeyboardButton("🌐 Network Status", callback_data='s')]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    welcome_text = (
        f"✨ *Welcome to VORTEX v2.6*, {user}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"💎 *Status:* `Verified Simulation`\n"
        f"🛡️ *Security:* `256-bit Mock Encryption`\n\n"
        f"Manage your simulated crypto assets with zero risk."
    )
    await update.message.reply_text(welcome_text, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=get_main_menu())

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        f"💳 *VORTEX WALLET*\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"💰 *Available:* `${sim.balance:,.2f} USDT`\n"
        f"📈 *24h Change:* `+4.25%` \n\n"
        f"📍 _All funds are simulated for testing._"
    )
    await update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN_V2)

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tx_hash = sim.generate_tx_hash()
    access_code = sim.generate_access_code()
    scan_link = sim.get_scan_link(tx_hash)
    
    msg = (
        f"📤 *WITHDRAWAL INITIALIZED*\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🔑 *Access Key:* `{access_code}`\n"
        f"📦 *Status:* `Pending Verification`\n"
        f"🔗 *TXID:* [View on BTC Scan]({scan_link})\n\n"
        f"⚠️ *Note:* This is a simulated transaction. No real assets have been moved."
    )
    await update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN_V2, disable_web_page_preview=True)

if __name__ == '__main__':
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("withdraw", withdraw))
    
    print("VORTEX 2026 Online...")
    app.run_polling()
