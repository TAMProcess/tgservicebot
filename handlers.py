from aiogram import Bot, Dispatcher, types
import config

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)

# Helper: main menu keyboard
main_menu_keyboard = types.InlineKeyboardMarkup()
main_menu_keyboard.add(types.InlineKeyboardButton("Bot Menu", callback_data="bot_menu"))
main_menu_keyboard.add(types.InlineKeyboardButton("Features", callback_data="features"))
main_menu_keyboard.add(types.InlineKeyboardButton("Purchase & Pricing", callback_data="purchase"))
main_menu_keyboard.add(types.InlineKeyboardButton("Tutorial & Guide", callback_data="tutorial"))
main_menu_keyboard.add(types.InlineKeyboardButton("Vouches", url="https://t.me/vouchesrugbot"))
main_menu_keyboard.add(types.InlineKeyboardButton("Dox Section", callback_data="dox_section"))
main_menu_keyboard.add(types.InlineKeyboardButton("Special Links", callback_data="special_links"))
main_menu_keyboard.add(types.InlineKeyboardButton("How To", callback_data="how_to"))
main_menu_keyboard.add(types.InlineKeyboardButton("Phantom Menu", callback_data="phantom_menu"))

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    """Handle /start command: greets the user as 'Guest' and shows main menu."""
    welcome_text = (
        "-Main Menu-\n"
        "Crypto Services Bot\n"
        "User: 73947211\n"
        "Version: 5.77.00\n"
        "@whatever\n"
        "All in one Crypto Services for Insiders\n"
    )
    purchase_text = (
        "💰 *Purchase & Pricing:*\n"
        "Includes access to all Features and Bots in the Crypto Services Bot\n"
        "3 Day Trial License - 2 SOL\n"
        "Ownership           - 5 SOL\n"
        f"*SOL Address:* `{config.SOL_ADDRESS}`\n\n"
        "Message @whatever for support\n"
        "After sending payment, click Refresh to check for updates.\n"
        "Note: Payment verification is manual. This bot does not automatically verify payments\n"
    )
    # Send welcome message with main menu inline keyboard
    await message.answer(welcome_text, reply_markup=main_menu_keyboard)
    # Send purchase and pricing information
    await message.answer(purchase_text)
    
# Callback handler for main menu navigation (Dashboard and Back both lead to main menu)
@dp.callback_query_handler(lambda c: c.data in ['dashboard', 'back'])
async def back_to_main(callback: types.CallbackQuery):
    """Handles 'Dashboard' and 'Back' button presses by returning to main menu."""
    # Edit the message to show the main menu again
    main_text = (
        "-Main Menu-\n"
        "Crypto Services Bot\n"
        "User: 73947211\n"
        "Version: 5.77.00\n"
        "@whatever\n"
        "All in one Crypto Services for Insiders\n"
    )
    # Re-use the same main menu keyboard
    await callback.message.edit_text(main_text, reply_markup=main_menu_keyboard)
    await callback.answer()

# Callback handler for Features section
@dp.callback_query_handler(lambda c: c.data == 'features')
async def features_section(callback: types.CallbackQuery):
    """Shows the Features section and a back button."""
    features_text = (
        "📋 *Features:*\n\n"
        "MemeCoinRugBot: an all-in-one bundler tool for bundling and rug pulling Solana meme coins. Generate wallets, create coins, launch on Pump.fun, Raydium, or Moonshot, and pull liquidity in a swift 'dump all' feature, eliminating price impact and maximizing profit potential.\n\n"
        "SniperBot: allows you to instantly sniper buy and sell coins at stop loss and take profit that you choose. Use this bot to have a competitive edge on competing traders. Compare your settings to other sniper bots in the profitable snipers section and change your settings and preferences accordingly. Adjust your preferences of purchase in the Buy/Sell Settings and filter out coins that you buy into in the Filters.\n\n"
        "CopyTraderBot: gives you the ability to mimic trades of the largest most profitable wallets on the Solana blockchain. Simply go to the 'profitable wallets' section and select which wallet you would like to copy trade, input this wallet into the wallet tracker. You can copy trade up to 10 wallets that you are wallet tracking. You are able to adjust all of your buy/sell settings.\n\n"
        "Social Media Bot: is used for artificially boosting social media accounts while maintaining the likes/followers/views ratio to mimic an organic thriving account. Select which social media platform you would like to bot, then select what you would like botted: followers, likes, or full package (combination of followers, likes, views, depending on the platform).\n\n"
        "Verification Bot: is a generator for phone numbers and emails, that allows you to temporarily use an email or phone number from any region that you select, for 15 minutes at a time. Giving you enough time to verify anything that you need for setting up accounts that you do not want connected to you.\n\n"
    )
    # Keyboard with only a Back button
    back_btn = types.InlineKeyboardButton("Back", callback_data="back")
    features_kb = types.InlineKeyboardMarkup().add(back_btn)
    await callback.message.edit_text(features_text, reply_markup=features_kb)
    await callback.answer()

# Callback handler for Bot Menu section
@dp.callback_query_handler(lambda c: c.data == 'bot_menu')
async def bot_menu(callback: types.CallbackQuery):
    """Main Bot Menu: Provides access to all bot features."""
    bot_menu_keyboard = types.InlineKeyboardMarkup()
    bot_menu_keyboard.add(types.InlineKeyboardButton("MemeCoinRugBot", callback_data="RugBot"))
    bot_menu_keyboard.add(types.InlineKeyboardButton("SniperBot", callback_data="SniperBot"))
    bot_menu_keyboard.add(types.InlineKeyboardButton("CopyTraderBot", callback_data="CopyTraderBot"))
    bot_menu_keyboard.add(types.InlineKeyboardButton("SocialMediaBot", callback_data="SocialMediaBot"))
    bot_menu_keyboard.add(types.InlineKeyboardButton("VerificationBot", callback_data="VerificationBot"))
    bot_menu_keyboard.add(types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back"))

    await callback.message.edit_text("📌 *Bot Menu:*", reply_markup=bot_menu_keyboard)
    await callback.answer()

# Callback handler for SniperBot section
@dp.callback_query_handler(lambda c: c.data == 'SniperBot')
async def sniperbot_section(callback: types.CallbackQuery):
    """Main SniperBot Menu: Provides access to all SniperBot features."""
    sniperbot_keyboard = types.InlineKeyboardMarkup()
    sniperbot_keyboard.add(types.InlineKeyboardButton("Profitable Snipers", callback_data="authentication_key_required"))
    sniperbot_keyboard.add(types.InlineKeyboardButton("Filters", callback_data="authentication_key_required"))
    sniperbot_keyboard.add(types.InlineKeyboardButton("Buy/Sell Settings", callback_data="authentication_key_required"))
    sniperbot_keyboard.add(types.InlineKeyboardButton("Wallet -> Deposit", callback_data="authentication_key_required"))
    sniperbot_keyboard.add(types.InlineKeyboardButton("Wallet -> Withdraw", callback_data="authentication_key_required"))
    sniperbot_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bot Menu", callback_data="bot_menu"))

    await callback.message.edit_text("📌 *SniperBot Menu:*", reply_markup=sniperbot_keyboard)
    await callback.answer()

# Callback handler for CopyTraderBot section
@dp.callback_query_handler(lambda c: c.data == 'CopyTraderBot')
async def copytraderbot_section(callback: types.CallbackQuery):
    """Main CopyTraderBot Menu: Provides access to all CopyTraderBot features."""
    copytraderbot_keyboard = types.InlineKeyboardMarkup()
    copytraderbot_keyboard.add(types.InlineKeyboardButton("Profitable Wallets", callback_data="authentication_key_required"))
    copytraderbot_keyboard.add(types.InlineKeyboardButton("Wallet Tracker", callback_data="authentication_key_required"))
    copytraderbot_keyboard.add(types.InlineKeyboardButton("Filters", callback_data="authentication_key_required"))
    copytraderbot_keyboard.add(types.InlineKeyboardButton("Buy/Sell Settings", callback_data="authentication_key_required"))
    copytraderbot_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bot Menu", callback_data="bot_menu"))

    await callback.message.edit_text("📌 *CopyTraderBot Menu:*", reply_markup=copytraderbot_keyboard)
    await callback.answer()

# Callback handler for SocialMediaBot section
@dp.callback_query_handler(lambda c: c.data == 'SocialMediaBot')
async def socialmediabot_section(callback: types.CallbackQuery):
    """Main SocialMediaBot Menu: Provides access to all SocialMediaBot features."""
    socialmediabot_keyboard = types.InlineKeyboardMarkup()
    socialmediabot_keyboard.add(types.InlineKeyboardButton("TikTok -> Followers", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("TikTok -> Likes", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("TikTok -> Views", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("TikTok -> Comments", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("TikTok -> Full Package", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Twitter -> Followers", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Twitter -> Views", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Twitter -> Likes", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Twitter -> Retweets", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Twitter -> Comments", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Twitter -> Full Package", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Instagram -> Followers", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Instagram -> Likes", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Instagram -> Views", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Instagram -> Comments", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Instagram -> Full Package", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("YouTube -> Subscribers", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("YouTube -> Views", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("YouTube -> Likes", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("YouTube -> Comments", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("YouTube -> Full Package", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Telegram -> Memebers", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Telegram -> Views", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Telegram -> Reactions", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Telegram -> Group Messages", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("Telegram -> Full Package", callback_data="authentication_key_required"))
    socialmediabot_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bot Menu", callback_data="bot_menu"))

    await callback.message.edit_text("📌 *SocialMediaBot Menu:*", reply_markup=socialmediabot_keyboard)
    await callback.answer()

# Callback handler for VerificationBot section
@dp.callback_query_handler(lambda c: c.data == 'VerificationBot')
async def verificationbot_section(callback: types.CallbackQuery):
    """Main VerificationBot Menu: Provides access to all VerificationBot features."""
    verificationbot_keyboard = types.InlineKeyboardMarkup()
    verificationbot_keyboard.add(types.InlineKeyboardButton("Generate Phone Number", callback_data="authentication_key_required"))
    verificationbot_keyboard.add(types.InlineKeyboardButton("Generate Email", callback_data="authentication_key_required"))
    verificationbot_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bot Menu", callback_data="bot_menu"))

    await callback.message.edit_text("📌 *VerificationBot Menu:*", reply_markup=verificationbot_keyboard)
    await callback.answer()

# Callback handler for Purchase & Pricing section (also handles Refresh)
@dp.callback_query_handler(lambda c: c.data in ['purchase', 'refresh'])
async def purchase_section(callback: types.CallbackQuery):
    """Shows the Purchase & Pricing section with payment info and a refresh option."""
    purchase_text = (
        "💰 *Purchase & Pricing:*\n"
        "3 Day Trial License - 1 SOL.\n"
        "Ownership           - 4 SOL.\n"
        f"*SOL Address:* `{config.SOL_ADDRESS}`\n\n"
        "Message @Rugbothelp for support\n"
        "After sending payment, click Refresh to check for updates.\n"
        "Note: Payment verification is manual. This bot does not automatically verify payments\n"
    )
    # Keyboard with Refresh and Back buttons
    refresh_btn = types.InlineKeyboardButton("Refresh 🔄", callback_data="refresh")
    back_btn = types.InlineKeyboardButton("Back", callback_data="back")
    purchase_kb = types.InlineKeyboardMarkup()
    purchase_kb.add(refresh_btn)
    purchase_kb.add(back_btn)
    await callback.message.edit_text(purchase_text, reply_markup=purchase_kb)
    await callback.answer()

# Callback handler for tutorial section
@dp.callback_query_handler(lambda c: c.data == 'tutorial')
async def tutorial(callback: types.CallbackQuery):
    """shows buttons for downloading tutorial"""
    tutorial_keyboard = types.InlineKeyboardMarkup()
    tutorial_keyboard.add(types.InlineKeyboardButton("Download Tutorial", callback_data="purchase_license"))
    tutorial_keyboard.add(types.InlineKeyboardButton("Download Setup Guide 💬", callback_data="purchase_license"))
    tutorial_keyboard.add(types.InlineKeyboardButton("Access Developer Portal 🤖", callback_data="purchase_license"))
    tutorial_keyboard.add(types.InlineKeyboardButton("Back", callback_data="dashboard"))

    await callback.message.edit_text("*Tutorial & Guide:*", reply_markup=tutorial_keyboard)
    await callback.answer()

# Callback handler for RugBot section (Main RugBot Menu)
@dp.callback_query_handler(lambda c: c.data == 'RugBot')
async def rugbot_section(callback: types.CallbackQuery):
    """Main RugBot Menu: Provides access to all RugBot features."""
    rugbot_keyboard = types.InlineKeyboardMarkup()
    rugbot_keyboard.add(types.InlineKeyboardButton("License Key", callback_data="license_key"))
    rugbot_keyboard.add(types.InlineKeyboardButton("Add Funds", callback_data="add_funds"))
    rugbot_keyboard.add(types.InlineKeyboardButton("Proxys & Node", callback_data="proxys_node"))
    rugbot_keyboard.add(types.InlineKeyboardButton("🏦 Bundler Menu", callback_data="bundler_menu"))
    rugbot_keyboard.add(types.InlineKeyboardButton("🔙 Back to Dashboard", callback_data="dashboard"))

    await callback.message.edit_text("📌 *RugBot Menu:*", reply_markup=rugbot_keyboard)
    await callback.answer()

# Callback handler for License key section
@dp.callback_query_handler(lambda c: c.data == 'license_key')
async def license_key(callback: types.CallbackQuery):
    """Handles license input."""
    await callback.message.edit_text(
        "💰 *Add License Key:*\n\n"
        "Please input your license key below:",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("🔙 Back to Main RugBot Menu", callback_data="RugBot")
        )
    )
    await callback.message.answer(
        "Input License Key:",
        reply_markup=types.ForceReply(selective=True)
    )
    await callback.answer()

# Message handler to capture the license key input
@dp.message_handler(lambda message: message.reply_to_message and message.reply_to_message.text == "Input License Key:")
async def handle_license_key_input(message: types.Message):
    """Processes the license key input from the user."""
    license_key = message.text
    # Process the license key (e.g., validate and store it)
    await message.answer(f"License Key '{license_key}' received and processed.")

# Callback handler for Add Funds section
@dp.callback_query_handler(lambda c: c.data == 'add_funds')
async def add_funds(callback: types.CallbackQuery):
    """Displays the funder wallet address."""
    await callback.message.edit_text(
        "💰 *Add Funds:*\n\n"
        "Generated Wallet: `authentication key required`\n\n"
        "Generated funder wallet is used to fund the bot.",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("🔙 Back to Main RugBot Menu", callback_data="RugBot")
        )
    )
    await callback.answer()

# Callback handler for Proxy & Nodes Menu
@dp.callback_query_handler(lambda c: c.data == 'proxys_node')
async def proxys_node(callback: types.CallbackQuery):
    """menu for Proxy & Nodes."""
    settings_keyboard = types.InlineKeyboardMarkup()
    settings_keyboard.add(types.InlineKeyboardButton("Input Custom Proxy's", callback_data="proxy_not_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Input Custom Node", callback_data="node_not_required"))
    settings_keyboard.add(types.InlineKeyboardButton("🔙 Back to Main RugBot Menu", callback_data="RugBot"))

    await callback.message.edit_text("*Proxy & Nodes:*", reply_markup=settings_keyboard)
    await callback.answer()
    
# Callback handler for Bundler Menu section
@dp.callback_query_handler(lambda c: c.data == 'bundler_menu')
async def bundler_menu(callback: types.CallbackQuery):
    """Main Bundler Menu."""
    bundler_keyboard = types.InlineKeyboardMarkup()
    bundler_keyboard.add(types.InlineKeyboardButton("Settings ⚙️", callback_data="bundler_settings"))
    bundler_keyboard.add(types.InlineKeyboardButton("Generate Wallets", callback_data="generate_wallets"))
    bundler_keyboard.add(types.InlineKeyboardButton("Launch Coin 💰", callback_data="launch_coin"))
    bundler_keyboard.add(types.InlineKeyboardButton("Manage Token", callback_data="manage_token"))
    bundler_keyboard.add(types.InlineKeyboardButton("Export Private Keys", callback_data="export_keys"))
    bundler_keyboard.add(types.InlineKeyboardButton("🔙 Back to Main RugBot Menu", callback_data="RugBot"))

    await callback.message.edit_text("🏦 *Bundler Menu:*", reply_markup=bundler_keyboard)
    await callback.answer()

# Callback handler for Settings Menu
@dp.callback_query_handler(lambda c: c.data == 'bundler_settings')
async def bundler_settings(callback: types.CallbackQuery):
    """Settings menu for Bundler features."""
    settings_keyboard = types.InlineKeyboardMarkup()
    settings_keyboard.add(types.InlineKeyboardButton("Safe Mode 🛟", callback_data="authentication_key_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Experimental Mode ✏️", callback_data="authentication_key_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Custom Commenter 💬", callback_data="authentication_key_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Auto Volume 🤖", callback_data="authentication_key_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Return to Funder 💸", callback_data="insufficient_funds"))
    settings_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))

    await callback.message.edit_text("⚙️ *Settings:*", reply_markup=settings_keyboard)
    await callback.answer()

# Callback handler for Generate Wallets section
@dp.callback_query_handler(lambda c: c.data == 'generate_wallets')
async def generate_wallets(callback: types.CallbackQuery):
    """Handles wallet generation requests."""
    wallets_keyboard = types.InlineKeyboardMarkup()
    wallets_keyboard.add(types.InlineKeyboardButton("Generate Bundler Wallets", callback_data="wallet_input"))
    wallets_keyboard.add(types.InlineKeyboardButton("Generate Wallets", callback_data="authentication_key_required"))
    wallets_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))

    await callback.message.edit_text("💳 *Generate Wallets:*", reply_markup=wallets_keyboard)
    await callback.answer()

# Callback handler for Launch Coin section
@dp.callback_query_handler(lambda c: c.data == 'launch_coin')
async def launch_coin(callback: types.CallbackQuery):
    """Handles token launch setup."""
    token_keyboard = types.InlineKeyboardMarkup()
    token_keyboard.add(types.InlineKeyboardButton("Token Name", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Symbol", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Image", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Description", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Website", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Twitter", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Telegram", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Launch Token", callback_data="insufficient_funds"))
    token_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))

    await callback.message.edit_text("🚀 *Launch Coin:*", reply_markup=token_keyboard)
    await callback.answer()

# Callback handler for Manage Token section
@dp.callback_query_handler(lambda c: c.data == 'manage_token')
async def manage_token(callback: types.CallbackQuery):
    """Handles token management options."""
    manage_keyboard = types.InlineKeyboardMarkup()
    manage_keyboard.add(types.InlineKeyboardButton("Dump All 🏳️", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Dump All %", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Delay Sell 📉", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Delay Sell %", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Single Sell", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Raydium Sell 💰", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Send SPL", callback_data="Token_Balance_0"))
    manage_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))
    
    await callback.message.edit_text("📉 *Manage Token:*", reply_markup=manage_keyboard)
    await callback.answer()

# Callback handler for Export Private Keys section
@dp.callback_query_handler(lambda c: c.data == 'export_keys')
async def export_keys(callback: types.CallbackQuery):
    """Handles private key export requests."""
    export_keyboard = types.InlineKeyboardMarkup()
    export_keyboard.add(types.InlineKeyboardButton("Export Generated Wallets", callback_data="authentication_key_required"))
    export_keyboard.add(types.InlineKeyboardButton("Export Funder Wallet", callback_data="authentication_key_required"))
    export_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))

    await callback.message.edit_text("🔑 *Export Private Keys:*", reply_markup=export_keyboard)
    await callback.answer()

# Callback handler for Dox Section
@dp.callback_query_handler(lambda c: c.data == 'dox_section')
async def dox_section(callback: types.CallbackQuery):
    """Dox Section: Provides access to web scraping and personal information."""
    dox_keyboard = types.InlineKeyboardMarkup()
    dox_keyboard.add(types.InlineKeyboardButton("Web Scrape", callback_data="web_scrape"))
    dox_keyboard.add(types.InlineKeyboardButton("Usernames", callback_data="usernames"))
    dox_keyboard.add(types.InlineKeyboardButton("Phone Numbers", callback_data="phone_numbers"))
    dox_keyboard.add(types.InlineKeyboardButton("Emails", callback_data="emails"))
    dox_keyboard.add(types.InlineKeyboardButton("Addresses", callback_data="addresses"))
    dox_keyboard.add(types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back"))

    await callback.message.edit_text("📌 *Dox Section:*", reply_markup=dox_keyboard)
    await callback.answer()

# Callback handler for Special Links Section
@dp.callback_query_handler(lambda c: c.data == 'special_links')
async def special_links(callback: types.CallbackQuery):
    """Special Links Section: Provides access to login links."""
    special_links_keyboard = types.InlineKeyboardMarkup()
    special_links_keyboard.add(types.InlineKeyboardButton("Telegram Login", callback_data="telegram_login"))
    special_links_keyboard.add(types.InlineKeyboardButton("Discord Login", callback_data="discord_login"))
    special_links_keyboard.add(types.InlineKeyboardButton("Gmail Login", callback_data="gmail_login"))
    special_links_keyboard.add(types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back"))

    await callback.message.edit_text("📌 *Special Links Section:*", reply_markup=special_links_keyboard)
    await callback.answer()

# Callback handler for How To Section
@dp.callback_query_handler(lambda c: c.data == 'how_to')
async def how_to(callback: types.CallbackQuery):
    """How To Section: Provides various guides."""
    how_to_keyboard = types.InlineKeyboardMarkup()
    how_to_keyboard.add(types.InlineKeyboardButton("Bot Guide and Function", callback_data="bot_guide"))
    how_to_keyboard.add(types.InlineKeyboardButton("How to Rug", callback_data="how_to_rug"))
    how_to_keyboard.add(types.InlineKeyboardButton("How to Access Info", callback_data="how_to_access_info"))
    how_to_keyboard.add(types.InlineKeyboardButton("How to Access Accounts", callback_data="how_to_access_accounts"))
    how_to_keyboard.add(types.InlineKeyboardButton("How to Track Wallets", callback_data="how_to_track_wallets"))
    how_to_keyboard.add(types.InlineKeyboardButton("How to Snipe", callback_data="how_to_snipe"))
    how_to_keyboard.add(types.InlineKeyboardButton("How to Wallet Track", callback_data="how_to_wallet_track"))
    how_to_keyboard.add(types.InlineKeyboardButton("How to Copy Trade", callback_data="how_to_copy_trade"))
    how_to_keyboard.add(types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back"))

    await callback.message.edit_text("📌 *How To Section:*", reply_markup=how_to_keyboard)
    await callback.answer()

# Callback handler for Phantom Menu
@dp.callback_query_handler(lambda c: c.data == 'phantom_menu')
async def phantom_menu(callback: types.CallbackQuery):
    """Phantom Menu: Provides access to drainer and wallet functions."""
    phantom_keyboard = types.InlineKeyboardMarkup()
    phantom_keyboard.add(types.InlineKeyboardButton("How to Use Drainer", callback_data="how_to_use_drainer"))
    phantom_keyboard.add(types.InlineKeyboardButton("Input Wallet Address", callback_data="input_wallet_address"))
    phantom_keyboard.add(types.InlineKeyboardButton("Target Address", callback_data="target_address"))
    phantom_keyboard.add(types.InlineKeyboardButton("Input Signature", callback_data="input_signature"))
    phantom_keyboard.add(types.InlineKeyboardButton("Drain All", callback_data="drain_all"))
    phantom_keyboard.add(types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back"))

    await callback.message.edit_text("📌 *Phantom Menu:*", reply_markup=phantom_keyboard)
    await callback.answer()

# Error Messages
@dp.callback_query_handler(lambda c: c.data == 'funder_empty')
async def funder_empty(callback: types.CallbackQuery):
    await callback.answer("Funder Wallet Empty", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'purchase_license')
async def purchase_license(callback: types.CallbackQuery):
    await callback.answer("Purchase license to download tutorials and access rugbot guide", show_alert=True)  

@dp.callback_query_handler(lambda c: c.data == 'node_not_required')
async def node_not_required(callback: types.CallbackQuery):
    await callback.answer("Input License Key To Edit Node, note: custom nodes are optional", show_alert=True)  
        
@dp.callback_query_handler(lambda c: c.data == 'proxy_not_required')
async def proxy_not_required(callback: types.CallbackQuery):
    await callback.answer("Input License Key To Edit Proxy, note: proxy are optional", show_alert=True)        

@dp.callback_query_handler(lambda c: c.data == 'no_tokens')
async def no_tokens(callback: types.CallbackQuery):
    await callback.answer("No tokens created", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'insufficient_funds')
async def insufficient_funds(callback: types.CallbackQuery):
    await callback.answer("Insufficient Funds, Please Add Funds", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'authentication_key_required')
async def authentication_key_required(callback: types.CallbackQuery):
    await callback.answer("Authetication Key Required, Please Input License", show_alert=True)
        
# Universal Back Button Handlers
@dp.callback_query_handler(lambda c: c.data == 'back_to_rugbot')
async def back_to_rugbot(callback: types.CallbackQuery):
    """Returns the user to the Main RugBot Menu."""
    await rugbot_section(callback)

@dp.callback_query_handler(lambda c: c.data == 'back_to_bundler')
async def back_to_bundler(callback: types.CallbackQuery):
    """Returns the user to the Bundler Menu."""
    await bundler_menu(callback)

@dp.callback_query_handler(lambda c: c.data == 'back_to_generate_wallets')
async def back_to_generate_wallets(callback: types.CallbackQuery):
    """Returns the user to the Generate Wallets Menu."""
    await generate_wallets(callback)

# Confirm Handlers Are Loaded
print("RugBot Handlers successfully loaded.")
