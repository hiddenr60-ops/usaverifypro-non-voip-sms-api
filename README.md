# usaverifypro-non-voip-sms-api
Official Python &amp; Node.js REST API Client for USAVerifyPro.com — Real Tier-1 US Non-VoIP Physical SIM Phone Numbers (AT&amp;T, Verizon, T-Mobile) for Automated SMS OTP Verification &amp; Carrier Lookup.
# USAVerify Pro — Official Non-VoIP SMS Verification & Carrier Lookup REST API

Official developer documentation and client SDK examples for [USAVerify Pro](https://usaverifypro.com/) — the enterprise platform for renting real Tier-1 United States physical SIM phone numbers (AT&T Mobility, Verizon Wireless, T-Mobile USA) for automated SMS OTP verification.

---

## Overview & Key Features

Modern platforms employ strict HLR and carrier line-type lookups that automatically block virtual VoIP numbers (such as Google Voice, TextNow, and public inbox numbers). **USAVerify Pro** provides direct access to physical PSTN mobile SIM hardware across United States area codes.

* **100% Real US Physical SIMs:** Authentic mobile lines on AT&T, Verizon, and T-Mobile networks that pass strict carrier validation checks.
* **Sub-5 Second OTP Delivery:** Direct cellular network parsing delivers incoming SMS verification codes in real time via REST API or Telegram Bot (`@usaverifypro_bot`).
* **Zero Code = Zero Charge Guarantee:** If an SMS verification code does not arrive within the rental window, the order cancels automatically and 100% of the balance is refunded instantly.
* **246+ Supported Platforms:** Built for high-volume verification workflows across [WhatsApp](https://usaverifypro.com/whatsapp-sms-verification), [OpenAI / ChatGPT](https://usaverifypro.com/chatgpt-openai-verification), [Google / Gmail](https://usaverifypro.com/google-gmail-verification), [Telegram](https://usaverifypro.com/telegram-sms-verification), [TikTok](https://usaverifypro.com/tiktok-sms-verification), [Discord](https://usaverifypro.com/discord-sms-verification), and more.
* **Drop-In Migration for Former SMS-Activate & DaisySMS Users:** Designed for developers seeking a reliable [SMS-Activate Alternative](https://usaverifypro.com/sms-activate-alternative) or [DaisySMS Alternative](https://usaverifypro.com/blog/best-daisysms-alternatives-2026) in 2026.

---

## Quick Links & Developer Resources

* **Official Platform:** [https://usaverifypro.com/](https://usaverifypro.com/)
* **API Documentation:** [https://usaverifypro.com/api-docs](https://usaverifypro.com/api-docs)
* **Free USA Carrier & VoIP Lookup Tool:** [https://usaverifypro.com/free-carrier-lookup](https://usaverifypro.com/free-carrier-lookup)
* **2026 Non-VoIP Provider Comparison:** [https://usaverifypro.com/best-non-voip-sms-verification](https://usaverifypro.com/best-non-voip-sms-verification)
* **Service Catalog & Pricing ($0.35+):** [https://usaverifypro.com/services](https://usaverifypro.com/services)
* **Digital Goods & PVA Store:** [https://usaverifypro.com/store](https://usaverifypro.com/store)

---

## Authentication

All API requests require your unique API key. To obtain your key:

1. Create a free account at [https://usaverifypro.com/](https://usaverifypro.com/).
2. Navigate to **Account Settings -> Developer API Key**.
3. Copy your API key and pass it in the `Authorization` header or as an `api_key` query parameter.

```http
Authorization: Bearer YOUR_USAVERIFYPRO_API_KEY
