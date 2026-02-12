<template>
  <v-container>
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
      <v-btn type="submit">Зарегистрироваться</v-btn>
    </form>
    <p v-if="message">{{ message }}</p>
  </v-container>
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

<style scoped>
.v-container{
  justify-items: center;
  background-color: #9a48d0ff;
  position: relative;
  top: 50%;
  width: 50%;
  padding: 5%;
}
input{
  margin: 10px;
  background-color: #030027ff;
}
.v-btn{
  background-color: #030027ff;
  color:aliceblue;
  margin-top: 5%;
  }
</style>