from telethon import TelegramClient, events

# بيانات الدخول (بتاخدها من موقع تليجرام)
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    print("📡 Telegram Hunter is active... Searching in channels.")
    # البحث عن قنوات بتنزل تسريبات
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            # هنا السكريبت بيراقب أي رسالة فيها "عصام صاصا" أو "تسريب"
            @client.on(events.NewMessage(chats=dialog.id))
            async def handler(event):
                if 'عصام صاصا' in event.text or 'تسريب' in event.text:
                    print(f"🔥 NEW LEAK FOUND: {event.text}")
                    if event.media:
                        print("Downloading the file...")
                        await event.download_media(file='/sdcard/Download/')

with client:
    client.loop.run_until_complete(main())

