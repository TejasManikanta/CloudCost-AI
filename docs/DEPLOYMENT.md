# CloudCost AI - Deployment Guide

## Production Deployment

### Prerequisites

- Ubuntu 20.04+ or Amazon Linux 2
- Python 3.11+
- MySQL 8.0+
- Nginx or Apache
- SSL Certificate

## AWS Deployment (Recommended)

### 1. Launch EC2 Instance

```bash
# Use Ubuntu 20.04 LTS AMI
# Instance type: t3.medium or larger
# Security group: Allow ports 80, 443, 22
```

### 2. Install Dependencies

```bash
sudo apt-get update
sudo apt-get install -y python3.11 python3-pip mysql-server nginx git

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configure MySQL

```bash
sudo mysql -u root -p < database/schema.sql

# Create application user
CREATE USER 'cloudcost'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON cloudcost_ai.* TO 'cloudcost'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Configure Nginx

```nginx
server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /home/ubuntu/CloudCost-AI/frontend/;
    }
}

server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}
```

### 5. Create Systemd Service

```bash
sudo nano /etc/systemd/system/cloudcost.service
```

```ini
[Unit]
Description=CloudCost AI Application
After=network.target

[Service]
Type=notify
User=ubuntu
WorkingDirectory=/home/ubuntu/CloudCost-AI
Environment="PATH=/home/ubuntu/CloudCost-AI/venv/bin"
ExecStart=/home/ubuntu/CloudCost-AI/venv/bin/gunicorn --workers 4 --bind 127.0.0.1:5000 backend.app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

### 6. Start Service

```bash
sudo systemctl daemon-reload
sudo systemctl start cloudcost
sudo systemctl enable cloudcost
```

## Docker Deployment

### Build and Run

```bash
docker-compose up -d
```

### Monitor

```bash
docker-compose logs -f app
```

## Environment Configuration

Create `.env` in production:

```bash
FLASK_ENV=production
DB_HOST=database.endpoint
DB_USER=cloudcost
DB_PASSWORD=secure_password

AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AZURE_SUBSCRIPTION_ID=your_id
GCP_PROJECT_ID=your_project

OAUTH_CLIENT_ID=your_id
OAUTH_CLIENT_SECRET=your_secret
```

## Database Backups

```bash
# Daily backup
mysqldump -u cloudcost -p cloudcost_ai > backup_$(date +%Y%m%d).sql

# Automated backup
0 2 * * * /home/ubuntu/backup.sh >> /var/log/backup.log 2>&1
```

## Monitoring

### Application Monitoring
- Use CloudWatch (AWS)
- Monitor CPU, Memory, Disk
- Set up alerts for errors

### API Monitoring
- Monitor response times
- Track error rates
- Monitor API quota usage

## Scaling

### Horizontal Scaling

1. Use AWS Auto Scaling Groups
2. Set up load balancer (ALB/NLB)
3. Configure RDS read replicas
4. Use ElastiCache for caching

### Vertical Scaling

- Increase instance size
- Optimize database queries
- Implement caching

## Security Best Practices

1. Keep dependencies updated
2. Use strong passwords
3. Enable 2FA for admin accounts
4. Regular security audits
5. Enable CloudTrail logging
6. Use IAM roles for EC2
7. Encrypt data at rest and in transit

## Troubleshooting

### Application won't start
```bash
journalctl -u cloudcost -n 50
```

### Database connection issues
```bash
mysql -h database.endpoint -u cloudcost -p
```

### Nginx errors
```bash
sudo nginx -t
sudo systemctl restart nginx
```

## Performance Tuning

1. Enable gzip compression
2. Implement database query caching
3. Use CDN for static files
4. Optimize images and assets
5. Implement lazy loading

## Cost Optimization

- Use Reserved Instances for database
- Use Spot Instances for non-critical workloads
- Set up CloudWatch cost alerts
- Review unused resources regularly
