import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8867414185:AAFtthBrTgv4ucd_4eQqYqp-EY2Ci9YBe5w"

PRODUCTS = {
    "1": {
        "name": "🎧 Wireless Headphones",
        "price": "₹1,299",
        "link": "https://example.com/product1",
        "desc": "40hr battery, noise cancellation."
    },
    "2": {
        "name": "⌚ Smart Watch",
        "price": "₹1,999",
        "link": "https://example.com/product2",
        "desc": "Bluetooth calling, heart-rate monitor."
    }
}

logging.basicConfig(level=logging.INFO)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("🛒 Top Products", callback_data="products")]]
    await update.message.reply_text(
        "👋 Namaste! Main <b>DealFinder</b> hoon.\n"
        "Top products dekhne ke liye button dabao 👇",
        reply_markup=InlineKeyboardMarkup(kb),
        parse_mode="HTML"
    )

async def button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "products":
        buttons = [[InlineKeyboardButton(f"{p['name']} - {p['price']}",
                    url=p["link"])] for p in PRODUCTS.values()]
        await query.edit_message_text("🔥 <b>Top Picks:</b>",
                                      reply_markup=InlineKeyboardMarkup(buttons),
                                      parse_mode="HTML")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
