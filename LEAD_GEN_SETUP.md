# UK Energy Lead Gen System

A complete lead capture and quote system for UK Energy Service.

## Files

```
uk-energy-service/
├── quote-form.html      # Lead capture form (user-facing)
├── appsscript.gs        # Google Apps Script (backend)
├── README.md            # This file
└── index.html           # Main website
```

---

## Quick Setup

### Step 1: Create Google Sheet

1. Go to sheets.google.com
2. Create new sheet → Name: "Energy Leads"
3. Create tab named "Leads"
4. Add headers in row 1:
   - A1: Timestamp
   - B1: Name
   - C1: Email
   - D1: Postcode
   - E1: Energy Type
   - F1: Usage
   - G1: Savings

### Step 2: Set Up Google Apps Script

1. Go to script.google.com
2. New Project
3. Paste code from `appsscript.gs`
4. In **Project Settings → Script Properties**, add:
   - `SPREADSHEET_ID` → The ID from the Energy Leads sheet URL
   - `TELEGRAM_BOT_TOKEN` → Your bot token
   - `TELEGRAM_CHAT_ID` → Your Telegram ID
5. Deploy → New Deployment
6. Select: Web app
7. Execute as: Me
8. Who has access: Anyone
9. Copy the Web App URL

### Step 3: Update Form

1. Open `quote-form.html`
2. Find: `const LEAD_ENDPOINT = '';`
3. Replace `''` with your Google Apps Script web-app URL

With an empty endpoint the page stays in explicit demo mode and says that no
lead was sent. It never claims an email was delivered.

---

## How It Works

```
User visits quote-form.html
        ↓
Fills in details
        ↓
Submits form
        ↓
Saves to Google Sheets
        ↓
Telegram notification sent to you
        ↓
User sees comparison links
```

---

## Features

✅ Lead capture form (name, email, postcode, usage)
✅ Auto-save to Google Sheets once the endpoint is configured
✅ Telegram notification with lead details once Script Properties are set
✅ Shows potential savings
✅ Comparison site links (Uswitch, GoCompare, MoneySuperMarket)

---

## To Add Email Quote

After setting up Google Apps Script, add this function:

```javascript
function sendQuoteEmail(data) {
  const subject = 'Your UK Energy Quote - Save up to £' + data.savings;
  const body = `
Hi ${data.name},

Thank you for your interest in saving on your energy bills!

Based on your usage (approx £${data.usage}/year), you could save up to £${data.savings}/year.

Quick ways to compare:
• Uswitch: https://www.uswitch.com
• GoCompare: https://www.gocompare.com
• MoneySuperMarket: https://www.moneysupermarket.com

For personalized help, reply to this email.

Best regards,
UK Energy Saver
  `;
  
  GmailApp.sendEmail(data.email, subject, body);
}
```

---

## Demo

Open `quote-form.html` in browser to test the form (no API needed for demo).
The demo preview is explicitly labelled and sends no lead.

---

*Created: 2026-02-28*
