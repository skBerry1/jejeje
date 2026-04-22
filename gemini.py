# Coded by @SKBERRYXXX
# Powered by Bunker Recovery Logic

import requests
from telethon import events
from .. import loader, utils  # Стандартные импорты для Heroku-UB

@loader.tds
class GeminiBunkerMod(loader.Module):
    """Модуль для связи с Gemini через локальный прокси Бункера"""
    strings = {"name": "GeminiBunker"}

    async def client_ready(self, client, db):
        self.endpoint = "http://localhost:8080/api/gemini-prompt"

    @loader.command()
    async def gask(self, message):
        """<промпт> - Задать вопрос Gemini (через Бункер)"""
        args = utils.get_args_raw(message)
        if not args:
            await message.edit("<b>[!] Введите текст вопроса.</b>")
            return

        await message.edit("<b>[📡] Установка связи с Бункером...</b>")
        
        try:
            payload = {"prompt": args}
            response = requests.post(self.api_url, json=payload, timeout=60)
            
            if response.status_code == 200:
                text = response.json().get("text", "Нет ответа")
                await message.edit(f"<b>🤖 Gemini:</b>\n\n{text}")
            else:
                await message.edit(f"<b>❌ Ошибка сервера:</b> {response.status_code}")
        except Exception as e:
            await message.edit(f"<b>⚠️ Ошибка подключения:</b> {str(e)}")

    @loader.command()
    async def ginfo(self, message):
        """Проверить статус подключения к Бункеру"""
        await message.edit(f"<b>🛠 Модуль:</b> Gemini Bunker\n<b>👤 Автор:</b> @SKBERRYXXX\n<b>🌐 Endpoint:</b> <code>{self.endpoint}</code>")
