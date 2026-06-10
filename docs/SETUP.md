# CloudCost AI - Setup Guide

## Prerequisites

- Python 3.11+
- MySQL 8.0+
- Docker & Docker Compose (optional)
- Node.js (for frontend build tools, optional)

## Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/TejasManikanta/CloudCost-AI.git
cd CloudCost-AI
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your configuration:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=cloudcost_ai

AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret

AZURE_SUBSCRIPTION_ID=your_id
AZURE_CLIENT_ID=your_client_id
AZURE_CLIENT_SECRET=your_secret
AZURE_TENANT_ID=your_tenant_id

GCP_PROJECT_ID=your_project

FLASK_SECRET_KEY=your_secret_key
OAUTH_CLIENT_ID=your_oauth_id
OAUTH_CLIENT_SECRET=your_oauth_secret
```

### 3. Create MySQL Database

```bash
mysql -u root -p < database/schema.sql
```

### 4. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python backend/app.py
```

The application will be available at `http://localhost:5000`

## Docker Installation

### 1. Build and Run with Docker Compose

```bash
docker-compose up -d
```

### 2. Access the Application

- Web UI: http://localhost:5000
- MySQL: localhost:3306

### 3. Stop the Application

```bash
docker-compose down
```

## Configuration

### AWS Configuration

1. Create AWS IAM user with pricing API permissions
2. Get Access Key ID and Secret Access Key
3. Add to `.env` file

### Azure Configuration

1. Register application in Azure AD
2. Create client secret
3. Get subscription ID
4. Add to `.env` file

### GCP Configuration

1. Create GCP project
2. Create service account
3. Download credentials JSON
4. Add to `.env` file

### OAuth/SSO Configuration

1. Register application with OAuth provider
2. Get Client ID and Client Secret
3. Set redirect URI: `http://localhost:5000/auth/callback`
4. Add to `.env` file

## Database Migrations

For schema updates:

```bash
alembic upgrade head
```

## Testing

```bash
pytest tests/
pytest --cov=backend tests/
```

## Troubleshooting

### MySQL Connection Error

```bash
# Check MySQL is running
mysql -u root -p -e "SELECT VERSION();"

# Verify credentials in .env
```

### API Connection Issues

- Verify API keys in `.env`
- Check network connectivity
- Review API quotas and limits

### Port Already in Use

```bash
# Change port in backend/app.py
app.run(host='0.0.0.0', port=5001)
```

## Next Steps

1. Configure cloud provider APIs
2. Set up user authentication
3. Test pricing integrations
4. Deploy to production

See [DEPLOYMENT.md](DEPLOYMENT.md) for production setup.
