# CloudCost AI - Enterprise-Grade AI Cloud Pricing Intelligence Platform

A production-ready SaaS web application that helps users compare cloud infrastructure pricing across AWS, Microsoft Azure, and Google Cloud Platform using official pricing APIs and real-time pricing data.

## 🎯 Objective

CloudCost AI combines an AI Chatbot, Infrastructure Requirement Analyzer, Document Intelligence, Pricing Calculator, and Cloud Cost Comparison Engine to help users:

- Compare cloud pricing across AWS, Azure, and GCP
- Retrieve real-time pricing using official provider APIs
- Analyze uploaded infrastructure requirement documents
- Generate architecture recommendations
- Provide cost optimization recommendations
- Convert pricing into different currencies
- Generate downloadable reports
- Save historical comparisons
- Maintain chat history

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3 (with Glassmorphism & Modern Design)
- Vanilla JavaScript (ES6+)

### Backend
- Python (Flask/FastAPI)
- Official Cloud Pricing APIs (AWS, Azure, GCP)

### Database
- MySQL 8.0+

## 📁 Project Structure

```
CloudCost-AI/
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── chat.html
│   ├── pricing-calculator.html
│   ├── document-upload.html
│   ├── reports.html
│   ├── profile.html
│   ├── admin.html
│   ├── css/
│   │   ├── styles.css
│   │   ├── dashboard.css
│   │   ├── chat.css
│   │   └── responsive.css
│   └── js/
│       ├── app.js
│       ├── auth.js
│       ├── chat.js
│       ├── pricing-calculator.js
│       ├── document-upload.js
│       ├── reports.js
│       └── api-client.js
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── sso.py
│   │   └── security.py
│   ├── apis/
│   │   ├── __init__.py
│   │   ├── aws_pricing.py
│   │   ├── azure_pricing.py
│   │   └── gcp_pricing.py
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── chatbot.py
│   │   ├── document_intelligence.py
│   │   └── recommendation_engine.py
│   ├── pricing/
│   │   ├── __init__.py
│   │   ├── pricing_engine.py
│   │   ├── currency_converter.py
│   │   └── report_generator.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── db_manager.py
│   └── routes/
│       ├── __init__.py
│       ├── auth_routes.py
│       ├── chat_routes.py
│       ├── pricing_routes.py
│       ├── document_routes.py
│       ├── report_routes.py
│       └── admin_routes.py
├── database/
│   ├── schema.sql
│   └── migrations/
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── SETUP.md
│   └── DEPLOYMENT.md
├── .env.example
├── docker-compose.yml
└── requirements.txt
```

## 🚀 Key Features

### 1. AI Chatbot System
- Natural Language Understanding
- Multi-turn conversations
- Context awareness
- Cloud architecture recommendations
- Pricing comparison
- Infrastructure analysis

### 2. Dual Input System
- **Chat Interface**: Natural language queries
- **Infrastructure Form**: Structured requirement fields
- **Document Upload**: PDF, DOCX, XLSX, CSV, TXT support

### 3. Cloud Pricing Engine
- Real-time pricing from official APIs
- AWS, Azure, GCP support
- All cloud services supported (Compute, Storage, Databases, etc.)

### 4. AI Recommendation Engine
- Architecture recommendations
- Best practices
- Scalability recommendations
- Security recommendations
- Cost optimization suggestions

### 5. Advanced Features
- Currency conversion (USD, INR, EUR, GBP, AUD, CAD, SGD, AED, JPY)
- Report generation (PDF, CSV, Excel)
- Chat history management
- Cost forecasting
- Carbon footprint estimation
- Budget planning

## 🔐 Security

- SSO Authentication
- Secure Sessions
- CSRF Protection
- XSS Protection
- SQL Injection Protection
- File Validation & Scanning
- API Authentication
- Audit Logging
- Encryption

## 📊 Database Design

MySQL tables for:
- Users & Sessions
- Chats & Messages
- Reports & Pricing Requests
- Uploaded Files & Extracted Requirements
- Cloud Providers & Currencies
- Audit Logs & Notifications

## 🎨 UI/UX Design

- Modern Enterprise SaaS Dashboard
- Glassmorphism effect
- Interactive tables
- Smooth animations
- Advanced search & smart filters
- Responsive design

## 📋 Getting Started

See [SETUP.md](docs/SETUP.md) for detailed installation instructions.

### Quick Start

```bash
# Clone the repository
git clone https://github.com/TejasManikanta/CloudCost-AI.git
cd CloudCost-AI

# Install backend dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Setup database
mysql -u root -p < database/schema.sql

# Run backend
python backend/app.py
```

## 📖 Documentation

- [API Documentation](docs/API.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Setup Guide](docs/SETUP.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 📄 License

MIT License - See LICENSE file for details

## 👨‍💼 Author

Tejas Manikanta

## 🤝 Contributing

Contributions are welcome! Please follow the contribution guidelines.

---

**Built for Enterprise. Powered by AI. Driven by Real-Time Pricing Intelligence.**
