from aiogram import F, Router, md
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from .config import config
from xls_parser import XlsParser

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer((
        f"Привет, {md.bold(message.from_user.full_name)}\!\n"
        "Загрузи файл excel в формате таблицы с полями:\n"
        "`title` \- название\n"
        "`url` \- ссылка на сайт источник\n"
        "`xpath` \- путь к элементу с ценой"),
        parse_mode=ParseMode.MARKDOWN_V2
    )


@router.message(F.text)
async def text_handler(message: Message) -> None:
    await message.answer((
        "Используй кнопку 📎 слева для загрузки файла\.\n"
        "Загрузи файл excel в формате таблицы с полями:\n"
        "`title` \- название\n"
        "`url` \- ссылка на сайт источник\n"
        "`xpath` \- путь к элементу с ценой"),
        parse_mode=ParseMode.MARKDOWN_V2
    )


@router.message(F.document)
async def file_handler(message: Message) -> None:
    allowed_extensions = {".xls", ".xlsx"}
    file_name = message.document.file_name
    file_path = f"{config.media_path}/{file_name}"

    if not any(file_name.endswith(ext) for ext in allowed_extensions):
        await message.answer("Пожалуйста, загрузи файл в формате Excel (.xls или .xlsx).")
        return

    await message.bot.download(message.document, file_path)

    print(XlsParser.parse_file(file_path))
