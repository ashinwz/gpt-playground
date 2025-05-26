<template>
  <div class="chat-container">
    <h1>Chatbot</h1>
    <div v-for="(msg, index) in messages" :key="index">
      <strong>{{ msg.sender }}:</strong> {{ msg.text }}
    </div>
    <input v-model="input" @keyup.enter="send" placeholder="Type message" />
    <button @click="send">Send</button>
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
  font-family: sans-serif;
  max-width: 600px;
  margin: auto;
}
input {
  width: 80%;
  padding: 0.5em;
}
button {
  padding: 0.5em;
}
</style>
