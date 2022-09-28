from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import InputPeerUser
from telegram import ParseMode
import threading
from streamlit.runtime.scriptrunner import add_script_run_ctx

def support_bot():
    @Bot.on(events.NewMessage(incoming=True))
    async def NewMessage(event):
        if not event.message.is_private: return
        user_info = await event.get_input_chat()
        cont=0

        async for m in Bot.iter_messages(user_info):
            if cont>=2:
                return
            cont+=1

        cippa = cippa = event.chat if event.chat is not None else await event.get_sender()
        username = cippa.username if cippa.username!=None else cippa.first_name+' '+cippa.last_name
    
        await Bot.send_message(InputPeerUser(user_info.user_id, user_info.access_hash),  
        message=("<b>👋WELCOME TO VORTEX SUPPORT!</b>\n\n"+
                "Hi <b>{}</b>, I hope you’re well!\n"+
                "This is an automatic message that gives you informations about how to buy a service and how to join our VIP channel!\n\n"+
                "<b>🔥HOW TO JOIN THE VIP CHANNELS?</b>\n\n"+
                "Once you buy one of our services, you will find out all the instructions you need to join on the respective channel or activating our telegram bot <b>@vort3xbot</b>\n\n"+
                "👉Click <b>/start</b> to activate the bot, then click button: <b>🌀Channels</b>\n\n"+
                "🤖Other Bot Features:\n"+
                "    <i>•View services status\n"+
                "    •Unsubscribe services\n"+
                "    •Manage renewal method\n"+
                "    •Download our forex guide\n"+
                "    •Link to get <u>14-day free trial</u></i>\n\n"+
                "🌐Visit our <b><a href='https://vortexproject.net'>website</a></b> and find all the information you need, you can also purchase one of our services\n\n"+
                "👇Write us for more questions").format(username)
        ,parse_mode=ParseMode.HTML)

try:
    cont= open('conf.ini').read()
    config=eval(cont)
    Bot = TelegramClient(StringSession(config['session']), config['api_id'],config['api_hash'])
    Bot.start()
    support_bot()
    print("Support Bot started.")
    Bot.run_until_disconnected()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit()

t1= threading.Thread(target=support_bot)
add_script_run_ctx(t1)
t1.start()
