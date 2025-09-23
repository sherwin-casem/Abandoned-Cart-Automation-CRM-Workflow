# 🚀 Quick Setup Guide

## Prerequisites
- Python 3.9+
- WhatsApp Business API access
- CRM system (optional)

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/Abish-gupta/Abandoned-Cart-Automation-CRM-Workflow.git
cd Abandoned-Cart-Automation-CRM-Workflow
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create `.env` file:
```env
# WhatsApp Configuration
WHATSAPP_API_KEY=your_whatsapp_api_key
WHATSAPP_PHONE_NUMBER=your_business_number

# CRM Configuration
CRM_API_URL=your_crm_api_url
CRM_API_KEY=your_crm_api_key

# Database
DATABASE_URL=sqlite:///cart_recovery.db

# Settings
ABANDONMENT_THRESHOLD_MINUTES=15
RECOVERY_EMAIL_TEMPLATE=recovery_template.html
```

### 4. Run Application
```bash
python app.py
```

## Integration Steps

### E-commerce Platform
1. Add tracking script to your website
2. Configure cart abandonment detection
3. Set up webhook endpoints

### WhatsApp Business API
1. Get WhatsApp Business API access
2. Configure webhook for message delivery
3. Set up message templates

### CRM Integration
1. Connect with your existing CRM
2. Configure lead assignment rules
3. Set up notification preferences

## Testing

### Test Cart Abandonment
1. Add items to cart
2. Leave without purchasing
3. Check WhatsApp message delivery
4. Verify CRM lead creation

### Monitor Dashboard
1. Open `dashboard.html` in browser
2. Check real-time metrics
3. Review lead assignments
4. Monitor recovery rates

## Production Deployment

### Security
- Use HTTPS for all endpoints
- Implement API authentication
- Encrypt sensitive data

### Scaling
- Use Redis for session management
- Implement queue system for high volume
- Set up monitoring and alerting

### Monitoring
- Track recovery rates
- Monitor system performance
- Set up error notifications

## Support

For questions or issues:
- 📧 Email: support@example.com
- 💬 GitHub Issues: [Create Issue](https://github.com/Abish-gupta/Abandoned-Cart-Automation-CRM-Workflow/issues)
- 📚 Documentation: [Full Docs](./docs/)

---

**Need help?** Check our [FAQ](./FAQ.md) or [contact support](mailto:support@example.com)
