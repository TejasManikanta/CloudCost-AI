// Chat Module
const chat = {
    currentChatId: null,
    messages: [],

    async createNewChat() {
        try {
            const response = await apiClient.post('/chat/create', {
                title: 'New Chat',
                chat_type: 'general',
            });
            this.currentChatId = response.id;
            this.clearMessages();
            this.loadChatHistory();
        } catch (error) {
            console.error('Error creating chat:', error);
        }
    },

    async sendMessage(content) {
        if (!this.currentChatId) {
            await this.createNewChat();
        }

        try {
            // Add user message to UI
            this.addMessageToUI('user', content);

            // Send to API
            const response = await apiClient.post(`/chat/${this.currentChatId}/message`, {
                content: content,
            });

            // Add assistant response to UI
            if (response.assistant_message) {
                this.addMessageToUI('assistant', response.assistant_message);
            }
        } catch (error) {
            console.error('Error sending message:', error);
        }
    },

    addMessageToUI(type, content) {
        const messagesArea = document.getElementById('messagesArea');
        const messageEl = document.createElement('div');
        messageEl.className = `message ${type}`;

        const avatarEl = document.createElement('div');
        avatarEl.className = 'message-avatar';
        avatarEl.innerHTML = type === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';

        const contentEl = document.createElement('div');
        contentEl.className = 'message-content';
        contentEl.textContent = content;

        messageEl.appendChild(avatarEl);
        messageEl.appendChild(contentEl);
        messagesArea.appendChild(messageEl);

        // Scroll to bottom
        messagesArea.scrollTop = messagesArea.scrollHeight;
    },

    async loadChatHistory() {
        try {
            const response = await apiClient.get('/chat/list');
            const chatHistory = document.getElementById('chatHistory');
            chatHistory.innerHTML = '';

            response.chats.forEach(chat => {
                const chatItem = document.createElement('div');
                chatItem.className = 'chat-item';
                chatItem.textContent = chat.title;
                chatItem.onclick = () => this.loadChat(chat.id);
                chatHistory.appendChild(chatItem);
            });
        } catch (error) {
            console.error('Error loading chat history:', error);
        }
    },

    async loadChat(chatId) {
        try {
            this.currentChatId = chatId;
            const response = await apiClient.get(`/chat/${chatId}`);
            this.clearMessages();
            this.messages = response.messages;

            const messagesArea = document.getElementById('messagesArea');
            this.messages.forEach(msg => {
                this.addMessageToUI(msg.message_type, msg.content);
            });
        } catch (error) {
            console.error('Error loading chat:', error);
        }
    },

    clearMessages() {
        const messagesArea = document.getElementById('messagesArea');
        messagesArea.innerHTML = '';
    },
};

// Initialize Chat
document.addEventListener('DOMContentLoaded', function() {
    auth.redirectIfNotAuthenticated();

    const messageForm = document.getElementById('messageForm');
    const messageInput = document.getElementById('messageInput');
    const newChatBtn = document.getElementById('newChatBtn');

    if (newChatBtn) {
        newChatBtn.addEventListener('click', async () => {
            await chat.createNewChat();
        });
    }

    if (messageForm) {
        messageForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const content = messageInput.value.trim();
            if (content) {
                await chat.sendMessage(content);
                messageInput.value = '';
            }
        });
    }

    // Load chat history
    chat.loadChatHistory();
});

function sendPrompt(prompt) {
    const messageInput = document.getElementById('messageInput');
    messageInput.value = prompt;
    const event = new Event('submit');
    document.getElementById('messageForm').dispatchEvent(event);
}
