from config import 5932720758
from database import load_db, save_db

async def admin(update, context):
    if update.effective_user.id != ADMIN_ID:
        return await update.message.reply_text("❌ Access denied")

    await update.message.reply_text("👑 Admin Panel")

async def addbalance(update, context):
    pass

async def users(update, context):
    pass
