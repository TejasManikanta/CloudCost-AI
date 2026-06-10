# CloudCost AI - API Documentation

## Base URL

```
http://localhost:5000/api
```

## Authentication

All endpoints (except login/register) require JWT token in Authorization header:

```
Authorization: Bearer <token>
```

## Response Format

All responses are JSON:

```json
{
  "success": true,
  "data": {},
  "error": null,
  "timestamp": "2026-06-10T10:00:00Z"
}
```

## Error Handling

```json
{
  "error": "Error message",
  "code": "ERROR_CODE",
  "details": {}
}
```

## Endpoints

### Authentication

#### POST /auth/login
User login

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "success": true,
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user_id": 1,
  "email": "user@example.com"
}
```

#### POST /auth/register
User registration

**Request:**
```json
{
  "email": "newuser@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe",
  "organization": "Company Name"
}
```

**Response:**
```json
{
  "success": true,
  "message": "User registered successfully",
  "user_id": 2
}
```

#### POST /auth/logout
User logout

**Response:**
```json
{
  "success": true,
  "message": "Logged out successfully"
}
```

#### GET /auth/me
Get current user

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "organization": "Company"
}
```

### Chat

#### POST /chat/create
Create new chat

**Request:**
```json
{
  "title": "AWS vs Azure Comparison",
  "chat_type": "pricing_comparison"
}
```

**Response:**
```json
{
  "success": true,
  "id": 1,
  "title": "AWS vs Azure Comparison",
  "created_at": "2026-06-10T10:00:00Z"
}
```

#### POST /chat/{id}/message
Send message in chat

**Request:**
```json
{
  "content": "Compare AWS and Azure pricing for a web application"
}
```

**Response:**
```json
{
  "success": true,
  "user_message": "Compare AWS and Azure pricing...",
  "assistant_message": "I'll help you compare AWS and Azure pricing...",
  "timestamp": "2026-06-10T10:00:00Z"
}
```

#### GET /chat/{id}
Get chat with messages

**Response:**
```json
{
  "id": 1,
  "title": "AWS vs Azure Comparison",
  "messages": [
    {
      "id": 1,
      "message_type": "user",
      "content": "Compare pricing...",
      "created_at": "2026-06-10T10:00:00Z"
    }
  ]
}
```

#### GET /chat/list
List all chats

**Response:**
```json
{
  "chats": [
    {"id": 1, "title": "AWS vs Azure", "created_at": "2026-06-10T10:00:00Z"},
    {"id": 2, "title": "Cost Optimization", "created_at": "2026-06-10T09:30:00Z"}
  ]
}
```

#### DELETE /chat/{id}
Delete chat

**Response:**
```json
{
  "success": true,
  "message": "Chat deleted successfully"
}
```

### Pricing

#### POST /pricing/compare
Compare cloud pricing

**Request:**
```json
{
  "cpu": 4,
  "memory": 8,
  "region": "us-east-1",
  "currency": "USD"
}
```

**Response:**
```json
{
  "success": true,
  "request_id": 1,
  "pricing": {
    "aws": {
      "provider": "AWS",
      "monthly_cost": 95.50,
      "yearly_cost": 1146.00,
      "3yr_cost": 3438.00
    },
    "azure": {
      "provider": "Azure",
      "monthly_cost": 110.00,
      "yearly_cost": 1320.00,
      "3yr_cost": 3960.00
    },
    "gcp": {
      "provider": "GCP",
      "monthly_cost": 88.00,
      "yearly_cost": 1056.00,
      "3yr_cost": 3168.00
    },
    "cheapest": "gcp"
  },
  "currency": "USD"
}
```

#### GET /pricing/history
Get pricing history

#### POST /pricing/forecast
Forecast costs

**Request:**
```json
{
  "monthly_cost": 1000,
  "growth_rate": 0.1,
  "months": 12
}
```

### Documents

#### POST /documents/upload
Upload document

**Request:** (multipart/form-data)
- file: [binary file]

**Response:**
```json
{
  "success": true,
  "file_id": 1,
  "filename": "architecture.pdf",
  "uploaded_at": "2026-06-10T10:00:00Z"
}
```

#### GET /documents/{id}
Get document

#### GET /documents/{id}/extract
Get extracted data

#### DELETE /documents/{id}
Delete document

### Reports

#### POST /reports/generate
Generate report

**Request:**
```json
{
  "type": "comparison",
  "pricing_request_id": 1
}
```

#### GET /reports/{id}
Get report

#### GET /reports/list
List reports

#### POST /reports/{id}/download
Download report

**Request:**
```json
{
  "format": "pdf"
}
```

## Rate Limiting

- 1000 requests per hour per user
- Pricing API calls: 100 per day

## Status Codes

- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 429: Too Many Requests
- 500: Internal Server Error
