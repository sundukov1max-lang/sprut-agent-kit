#!/usr/bin/env python3
import os
"""Telegram Telethon auth - one-time setup"""
from telethon import TelegramClient
import asyncio

api_id = int(os.environ.get("TG_API_ID", "0"))
api_hash = os.environ.get("TG_API_HASH", "")
session_path = "~/.openclaw/tg-stats-session"

async def main():
    client = TelegramClient(session_path, api_id, api_hash)
    await client.start(phone=input("Enter phone number: "))
    me = await client.get_me()
    print(f"✅ Авторизован как: {me.first_name} {me.last_name or ''} (@{me.username})")
    await client.disconnect()

asyncio.run(main())
