# CloudCost AI - Architecture Documentation

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (HTML/CSS/JS)                  │
│  ┌──────────────┬──────────────┬──────────────────────────┐ │
│  │ Login UI     │ Dashboard    │ Chat Interface           │ │
│  │ Calculator   │ Reports      │ Document Upload          │ │
│  │ Profile      │ Admin Panel  │ Settings                 │ │
│  └──────────────┴──────────────┴──────────────────────────┘ │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/REST API
┌────────────────────────▼────────────────────────────────────┐
│                    Flask Backend (Python)                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              API Routes & Controllers                │  │
│  │  ├─ Auth Routes     ├─ Chat Routes                  │  │
│  │  ├─ Pricing Routes  ├─ Report Routes                │  │
│  │  ├─ Document Routes ├─ Admin Routes                 │  │
│  │  └─ User Routes     └─ Settings Routes              │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Business Logic Layer                    │  │
│  │  ├─ Pricing Engine        ├─ AI/Chatbot             │  │
│  │  ├─ Document Intelligence ├─ Recommendation Engine  │  │
│  │  ├─ Currency Converter    ├─ Report Generator       │  │
│  │  └─ Cost Forecasting      └─ Security/Auth         │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │          Cloud Pricing API Integration Layer        │  │
│  │  ┌──────────────┬──────────────┬──────────────────┐ │  │
│  │  │ AWS Pricing  │ Azure Retail │ GCP Pricing      │ │  │
│  │  │ APIs         │ Pricing API  │ Catalog API      │ │  │
│  │  └──────────────┴──────────────┴──────────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │ Database Queries
┌────────────────────────▼────────────────────────────────────┐
│                    MySQL Database                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Users │ Sessions │ Chats │ Messages │ Pricing Data   │  │
│  │ Reports │ Files │ Settings │ Logs │ Notifications   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### Frontend Layer

**Responsibilities:**
- User interface rendering
- Client-side form validation
- API request handling
- Real-time updates
- Local state management

**Files:**
- `frontend/index.html` - Landing/home page
- `frontend/login.html` - Authentication page
- `frontend/dashboard.html` - Main dashboard
- `frontend/chat.html` - Chat interface
- `frontend/css/` - Styling
- `frontend/js/` - Client logic

### Backend Layer

#### API Routes
- `auth_routes.py` - Authentication endpoints
- `chat_routes.py` - Chat operations
- `pricing_routes.py` - Pricing comparison
- `document_routes.py` - Document upload & analysis
- `report_routes.py` - Report generation
- `admin_routes.py` - Admin operations

#### Business Logic
- `pricing_engine.py` - Core pricing calculations
- `chatbot.py` - NLP and conversation handling
- `document_intelligence.py` - File parsing and requirement extraction
- `recommendation_engine.py` - AI-powered recommendations
- `report_generator.py` - PDF/Excel/CSV export
- `currency_converter.py` - Multi-currency support

#### Cloud Integration
- `aws_pricing.py` - AWS API integration
- `azure_pricing.py` - Azure API integration
- `gcp_pricing.py` - GCP API integration

### Database Layer

**Key Tables:**

1. **users** - User accounts and profiles
2. **user_sessions** - Active sessions
3. **chats** - Chat conversations
4. **chat_messages** - Individual messages
5. **pricing_requests** - Pricing calculation requests
6. **pricing_results** - Pricing calculation results
7. **reports** - Generated reports
8. **uploaded_files** - Document uploads
9. **extracted_requirements** - AI-extracted requirements
10. **audit_logs** - Security audit trail
11. **notifications** - User notifications
12. **cloud_providers** - Provider information
13. **currencies** - Currency data

## Data Flow

### Pricing Comparison Flow

```
1. User Input
   ↓
2. API Request (POST /api/pricing/compare)
   ↓
3. Validate Requirements
   ↓
4. Fetch Current Pricing from Cloud APIs
   ├─ AWS Pricing API
   ├─ Azure Retail API
   └─ GCP Pricing API
   ↓
5. Calculate Costs
   ↓
6. Generate Recommendations
   ↓
7. Format Response
   ↓
8. Return Results to Frontend
   ↓
9. Display Results to User
```

### Document Analysis Flow

```
1. File Upload
   ↓
2. File Validation & Scanning
   ↓
3. Extract Text (PDF/DOCX/XLSX)
   ↓
4. Parse with NLP
   ↓
5. Extract Requirements
   ↓
6. Cloud Resource Mapping
   ↓
7. Calculate Pricing
   ↓
8. Generate Report
   ↓
9. Store in Database
```

### Chat Flow

```
1. User Message
   ↓
2. Store in Database
   ↓
3. Process with NLP/Chatbot
   ↓
4. Generate Response
   ↓
5. Call Pricing API if needed
   ↓
6. Format Response
   ↓
7. Store Assistant Message
   ↓
8. Stream/Send to Frontend
```

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/register` - User registration
- `POST /api/auth/callback` - OAuth callback
- `GET /api/auth/me` - Current user info

### Pricing
- `POST /api/pricing/compare` - Compare cloud providers
- `GET /api/pricing/history` - Pricing history
- `POST /api/pricing/forecast` - Cost forecasting

### Chat
- `POST /api/chat/create` - Create new chat
- `POST /api/chat/{id}/message` - Send message
- `GET /api/chat/{id}` - Get chat
- `GET /api/chat/list` - List chats
- `DELETE /api/chat/{id}` - Delete chat

### Documents
- `POST /api/documents/upload` - Upload document
- `GET /api/documents/{id}` - Get document
- `DELETE /api/documents/{id}` - Delete document
- `GET /api/documents/{id}/extract` - Get extracted data

### Reports
- `POST /api/reports/generate` - Generate report
- `GET /api/reports/{id}` - Get report
- `GET /api/reports/list` - List reports
- `POST /api/reports/{id}/download` - Download report

### User
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update profile
- `GET /api/user/settings` - Get settings
- `PUT /api/user/settings` - Update settings

## Security Architecture

1. **Authentication**
   - SSO/OAuth 2.0
   - JWT tokens
   - Secure session management

2. **Authorization**
   - Role-based access control (RBAC)
   - Resource-level permissions

3. **Data Protection**
   - Password hashing (bcrypt)
   - Encryption at rest
   - Encryption in transit (HTTPS)

4. **API Security**
   - Rate limiting
   - CSRF protection
   - XSS protection
   - Input validation
   - SQL injection prevention

5. **Audit & Monitoring**
   - Comprehensive audit logs
   - API monitoring
   - Error tracking
   - Security event logging

## Scalability Considerations

1. **Database**
   - Indexing on frequently queried columns
   - Query optimization
   - Connection pooling

2. **Caching**
   - Cloud provider pricing cache
   - User data cache
   - Report cache

3. **API Optimization**
   - Async request handling
   - Background job processing
   - Request batching

4. **Deployment**
   - Horizontal scaling with load balancer
   - Database replication
   - CDN for static files

## Performance Optimization

- Lazy loading of chat history
- Pagination for lists
- Compression of API responses
- Database query optimization
- Frontend minification
- Caching strategies
