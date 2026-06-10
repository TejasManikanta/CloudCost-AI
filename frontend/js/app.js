// Main App Module
const app = {
    theme: localStorage.getItem('theme') || 'light',

    init() {
        this.setupTheme();
        this.setupEventListeners();
    },

    setupTheme() {
        if (this.theme === 'dark') {
            document.body.classList.add('dark-mode');
        }
    },

    setupEventListeners() {
        const themeToggle = document.getElementById('themeToggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', () => this.toggleTheme());
        }

        const currencySelect = document.getElementById('currencySelect');
        if (currencySelect) {
            currencySelect.addEventListener('change', (e) => this.changeCurrency(e.target.value));
        }
    },

    toggleTheme() {
        this.theme = this.theme === 'light' ? 'dark' : 'light';
        localStorage.setItem('theme', this.theme);
        document.body.classList.toggle('dark-mode');
    },

    changeCurrency(currency) {
        localStorage.setItem('preferred_currency', currency);
        // Trigger currency update across app
        document.dispatchEvent(new CustomEvent('currencyChanged', { detail: { currency } }));
    },

    formatCurrency(amount, currency = 'USD') {
        const formatter = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: currency,
        });
        return formatter.format(amount);
    },
};

// Initialize app on load
document.addEventListener('DOMContentLoaded', () => {
    app.init();
});
