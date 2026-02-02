<template>
  <div>
    <h3>Регистрация</h3>
    <form @submit.prevent="register">
      <div>
        <label>Имя пользователя:</label>
        <input v-model="username" required />
      </div>
      <div>
        <label>Пароль:</label>
        <input v-model="password" type="password" required />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      message: ''
    }
  },
  methods: {
    async register() {
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/register/', {
            username: this.username,
            password: this.password
            }, {
            headers: {
                'Content-Type': 'application/json'
            }
            });
            this.message = 'Пользователь зарегистрирован';
        } catch (error) {
            if (error.response) {
            this.message = error.response.data.error || 'Ошибка регистрации';
            } else {
            this.message = 'Ошибка соединения с сервером';
            }
            console.error(error);
        }
    }
  }
}
</script>