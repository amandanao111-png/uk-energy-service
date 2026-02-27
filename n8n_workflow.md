# n8n UK Energy Automation Workflow

## What is n8n?

n8n is a free, open-source workflow automation tool.
- Self-hosted (free)
- Connect APIs, apps, AI
- Automate repetitive tasks

---

## UK Energy Service - Automation Ideas

### 1. Price Alert Workflow

```
[Scheduler: Daily 9AM]
      ↓
[HTTP Request: Get Ofgem prices]
      ↓
[Compare with stored prices]
      ↓
[IF price dropped >5%]
      ↓
[Send Email/SMS to user]
```

### 2. Lead Capture Flow

```
[Webhook: Form submission]
      ↓
[Validate email]
      ↓
[Add to Google Sheets]
      ↓
[Send to Telegram]
      ↓
[Add to email marketing]
```

### 3. Weekly Report Flow

```
[Scheduler: Every Monday]
      ↓
[Get latest energy prices]
      ↓
[Generate PDF report]
      ↓
[Email to subscribers]
```

---

## Quick Start

### Install n8n (Self-hosted)

```bash
# Using Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### Or use cloud version
- n8n.cloud (free tier available)

---

## Simple Workflow: Price Monitor

1. Create new workflow
2. Add "Schedule Trigger" (daily at 9am)
3. Add "HTTP Request" (fetch Ofgem API)
4. Add "IF" (check price change)
5. Add "Telegram" (send alert)

---

## For UK Energy Service

I can create:
1. ✅ Lead capture webhook
2. ✅ Daily price check
3. ✅ Email notifications

---

*Created: Feb 2026*
