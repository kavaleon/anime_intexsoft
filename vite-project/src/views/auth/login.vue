<template>
  <div>
    <h3>Вход</h3>
    <form @submit.prevent="register">
      <div>
        <label>Имя пользователя:</label>
        <input v-model="username" required />
      </div>
      <div>
        <label>Пароль:</label>
        <input v-model="password" type="password" required />
      </div>
      <button type="submit">Вход</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>


<script>
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
        const response = await fetch('http://127.0.0.1:8000/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        });
        const result = await response.json();
        if (response.ok) {
          this.message = 'Вход успешен';
        } else {
          this.message = result.message || 'Ошибка входа';
        }
      } catch (error) {
        this.message = 'Ошибка соединения с сервером';
        console.error(error);
      }
    }
  }
}
</script>