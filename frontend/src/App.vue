<template>
  <div class="chat-container">
    <div class="messages">
      <div
        v-for="(msg, index) in messages"
        :key="index"
        :class="['message', msg.sender === 'You' ? 'from-user' : 'from-bot']"
      >
        <div class="bubble">{{ msg.text }}</div>
      </div>
    </div>
    <div class="input-row">
      <input v-model="input" @keyup.enter="send" placeholder="Type message" />
      <button @click="send">Send</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const messages = ref([])
const input = ref('')
const backendUrl = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

async function send() {
  if (!input.value) return
  messages.value.push({ sender: 'You', text: input.value })
  const res = await fetch(`${backendUrl}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: input.value })
  })
  input.value = ''
  if (res.ok) {
    const data = await res.json()
    messages.value.push({ sender: 'Bot', text: data.response })
  } else {
    messages.value.push({ sender: 'Bot', text: 'Error contacting server' })
  }
}
</script>

<style>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  font-family: Arial, Helvetica, sans-serif;
  background: #f5f5f5;
  padding: 1rem;
}

.messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 1rem;
}

.message {
  display: flex;
  margin-bottom: 0.5rem;
}

.from-user {
  justify-content: flex-end;
}

.bubble {
  max-width: 70%;
  padding: 0.5rem 0.75rem;
  border-radius: 12px;
  background-color: #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.from-user .bubble {
  background-color: #42b983;
  color: white;
}

.input-row {
  display: flex;
}

.input-row input {
  flex: 1;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.input-row button {
  margin-left: 0.5rem;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 4px;
  background-color: #42b983;
  color: white;
  cursor: pointer;
}

.input-row button:hover {
  background-color: #369f6e;
}
</style>
