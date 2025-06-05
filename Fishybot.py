import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Получение токена из переменных окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    logger.error("Токен бота не найден! Установите переменную TELEGRAM_TOKEN")
    exit(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# =====================
# ИНЛАЙН-КНОПКИ
# =====================
def main_menu_buttons():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🐠 Обо мне", callback_data="about"),
                InlineKeyboardButton(text="💻 Услуги", callback_data="services")
            ],
            [
                InlineKeyboardButton(text="📂 Портфолио", callback_data="portfolio"),
                InlineKeyboardButton(text="🔐 Принципы", callback_data="principles")
            ],
            [
                InlineKeyboardButton(text="📞 Контакты", callback_data="contacts"),
                InlineKeyboardButton(text="💬 FAQ", callback_data="faq")
            ]
        ]
    )

back_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
        ]
    )

start_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚀 СТАРТ", callback_data="start_main")]
        ]
    )

# =====================
# ТЕКСТОВЫЕ ШАБЛОНЫ
# =====================
WELCOME_TEXT = f"""
{hbold('FishyOcean Portfolio')}

{hbold('Что умеет этот бот?')}

Здесь вы можете узнать о моих услугах разработчика Telegram ботов, 
посмотреть примеры работ и узнать, как со мной сотрудничать.
"""

MAIN_MENU_TEXT = f"""
{hbold('Главное меню')}

Выберите интересующий раздел:
"""

ABOUT_TEXT = f"""
{hbold('🐠 Обо мне')}

Я - разработчик Telegram ботов, специализирующийся на создании:
• Информационных ботов
• Автоматизированных систем уведомлений
• Инструментов для бизнес-коммуникаций

Моя специализация:
- Python 3.11
- Aiogram 3.x
- Асинхронная архитектура

Философия:
«Создаю ботов, которые решают конкретные задачи без излишеств»
"""

SERVICES_TEXT = f"""
{hbold('💻 Услуги')}

Я разрабатываю только информационные боты, которые:
• Не работают с персональными данными
• Не требуют сложной аутентификации
• Решают конкретные бизнес-задачи

Основные направления:
1. Информационные боты (справочники, базы знаний)
2. Боты-уведомления (оповещения о событиях)
3. Автоматизированные помощники (FAQ, поддержка)
4. Интеграции с публичными API

Важно: не занимаюсь разработкой ботов, требующих обработки персональных данных.
"""

PORTFOLIO_TEXT = f"""
{hbold('📂 Портфолио')}

1. MemeBot - Получение мемов из Reddit
   • Технологии: Python, aiogram, Reddit API
   • Особенности: Возможность добавлять мемы в Избранное
   • Ссылка: github.com/TheBusinessFish/telegram-meme-bot

2. Fishybot - Узнайте больше о FishyOcean!
   • Технологии: Python, aiogram
   • Особенности: Распределение информации по категориям
   • Ссылка: github.com/TheBusinessFish/Fishybot
"""

PRINCIPLES_TEXT = f"""
{hbold('🔐 Принципы работы')}

Этапы сотрудничества:

1. Обсуждение:
   • Формулируем задачу и ожидаемый результат
   • Определяем сроки реализации
   • Согласовываем бюджет

2. Реализация:
   • Разработка в соответствии с ТЗ
   • Поэтапное согласование
   • Тестирование

3. Передача решения:

Вариант ① (Разовая оплата):
   • Полный пакет исходного кода
   • Файлы конфигурации
   • Инструкция по установке
   • Консультация по настройке

Вариант ② (SaaS модель):
   • Размещение бота на моих серверах
   • Техническая поддержка
   • Регулярные обновления
   • Ежемесячная оплата за обслуживание
"""

CONTACTS_TEXT = f"""
{hbold('📞 Контакты')}

Для обсуждения проекта:
• Telegram: @FishyOcean
• GitHub: github.com/TheBusinessFish

Все коммуникации только через защищенные каналы. 
Не предоставляю личных данных и не использую email.
"""

FAQ_TEXT = f"""
{hbold('💬 Частые вопросы')}

{hbold('Сколько стоит разработка?')}
• Простые боты: от 5000₽
• Средней сложности: 10000-25000₽
• Сложные проекты: индивидуальный расчет

{hbold('Сроки разработки?')}
• Зависит от сложности проекта
• Минимальный срок: 3 рабочих дня
• Средние проекты: 1-2 недели

{hbold('Какие гарантии?')}
• Тестирование перед передачей
• Исправление критичных ошибок в течение 7 дней
• Консультация по установке (для варианта ①)
"""

# =====================
# ОБРАБОТЧИКИ КОМАНД
# =====================
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        WELCOME_TEXT,
        reply_markup=start_kb,
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "start_main")
async def start_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        MAIN_MENU_TEXT,
        reply_markup=main_menu_buttons(),
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        MAIN_MENU_TEXT,
        reply_markup=main_menu_buttons(),
        parse_mode="HTML"
    )

# Обработчики для разделов
@dp.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.edit_text(
        ABOUT_TEXT,
        reply_markup=back_button,
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "services")
async def services(callback: types.CallbackQuery):
    await callback.message.edit_text(
        SERVICES_TEXT,
        reply_markup=back_button,
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "portfolio")
async def portfolio(callback: types.CallbackQuery):
    await callback.message.edit_text(
        PORTFOLIO_TEXT,
        reply_markup=back_button,
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "principles")
async def principles(callback: types.CallbackQuery):
    await callback.message.edit_text(
        PRINCIPLES_TEXT,
        reply_markup=back_button,
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "contacts")
async def contacts(callback: types.CallbackQuery):
    await callback.message.edit_text(
        CONTACTS_TEXT,
        reply_markup=back_button,
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "faq")
async def faq(callback: types.CallbackQuery):
    await callback.message.edit_text(
        FAQ_TEXT,
        reply_markup=back_button,
        parse_mode="HTML"
    )

# =====================
# ЗАПУСК БОТА
# =====================
async def main():
    logger.info("Запуск бота FishyOcean...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    logger.info("Бот остановлен")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Работа бота прервана")
    except Exception as e:
        logger.exception(f"Критическая ошибка: {str(e)}")
