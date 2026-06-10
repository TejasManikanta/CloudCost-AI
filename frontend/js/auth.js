// Authentication Module
const auth = {
    async login(email, password) {
        try {
            const response = await apiClient.post('/auth/login', { email, password });
            if (response.token) {
                apiClient.setToken(response.token);
                window.location.href = '/dashboard.html';
            }
        } catch (error) {
            console.error('Login error:', error);
        }
    },

    async register(userData) {
        try {
            const response = await apiClient.post('/auth/register', userData);
            if (response.success) {
                window.location.href = '/login.html';
            }
        } catch (error) {
            console.error('Registration error:', error);
        }
    },

    async logout() {
        await apiClient.post('/auth/logout');
        apiClient.logout();
    },

    isAuthenticated() {
        return !!localStorage.getItem('auth_token');
    },

    redirectIfNotAuthenticated() {
        if (!this.isAuthenticated()) {
            window.location.href = '/login.html';
        }
    },
};

// Login Form Handler
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            await auth.login(email, password);
        });
    }
});
