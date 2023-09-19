import typing

from data.config import private_channels
from database import users

if typing.TYPE_CHECKING:
    import aiogram

    
async def task(bot: 'aiogram.Bot'):
    users_records = await users.get_all()
    channels = [
        await bot.get_chat(private_channels[name]['id']) 
        for name in private_channels.keys()
    ]
    for user in users_records:
        if user.days_sub_end >= 1: continue
    
        for channel in channels:
            member = await bot.get_chat_member(channel.id, user.telegram_id)
            if member.status in ['left', 'creator']: continue
        
            await bot.kick_chat_member(channel.id, user.telegram_id)
            
            
