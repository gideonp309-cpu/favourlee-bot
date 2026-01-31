import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from engine import SimulationEngine

# Initialize simulation
sim = SimulationEngine()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 **Simulated Trading Bot Active**\n\n"
        "/balance - View simulated funds\n"
        "/wallet - View deposit address\n"
        "/price BTC - Get current mock price"
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (f"💰 **Simulated Balance:** ${sim.balance:,.2f} USDT\n"
           f"📈 **Open Positions:** {len(sim.portfolio)}")
    await update.message.reply_text(msg)

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📥 **Your Simulated Deposit Address:**\n`{sim.get_wallet_address()}`")

if __name__ == '__main__':
    # Render uses environment variables for security
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("wallet", wallet))
    
    print("Bot is running...")
    app.run_polling()
