// API Client Module
const apiClient = {
    baseURL: 'http://localhost:5000/api',
    token: localStorage.getItem('auth_token'),

    async request(method, endpoint, data = null) {
        const url = `${this.baseURL}${endpoint}`;
        const options = {
            method,
            headers: {
                'Content-Type': 'application/json',
            },
        };

        if (this.token) {
            options.headers['Authorization'] = `Bearer ${this.token}`;
        }

        if (data) {
            options.body = JSON.stringify(data);
        }

        try {
            const response = await fetch(url, options);
            if (response.status === 401) {
                this.logout();
            }
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    },

    async get(endpoint) {
        return this.request('GET', endpoint);
    },

    async post(endpoint, data) {
        return this.request('POST', endpoint, data);
    },

    async put(endpoint, data) {
        return this.request('PUT', endpoint, data);
    },

    async delete(endpoint) {
        return this.request('DELETE', endpoint);
    },

    setToken(token) {
        this.token = token;
        localStorage.setItem('auth_token', token);
    },

    logout() {
        this.token = null;
        localStorage.removeItem('auth_token');
        window.location.href = '/login.html';
    },
};
