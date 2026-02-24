<template>
  <div class="home_page">
    <div class="headers">
      <div v-if="user && user.id" class="welcome">
        <h1 class="welcome_text">Добро пожаловать {{ user.username }}</h1>
      </div>
      <div class="logo">
        <img src="../assets/logo.png" alt="Logo" class="logo" />
      </div>
      
      <div class="register-button-container">
        <v-btn 
          v-if="!user || !user.id"  
          color="#baff29" 
          dark  
          @click="router.push('/auth/register')" 
        >
          Регистрация
        </v-btn>
        
        <div v-else class="auth-buttons">
          <v-menu offset-y>
            <template #activator="{ props }">
              <v-btn v-bind="props" color="#baff29" dark>
                Личный кабинет
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="goToResults">
                <v-list-item-title>Результаты квизов</v-list-item-title>
              </v-list-item>
              <v-list-item @click="goToSettings">
                <v-list-item-title>Настройки</v-list-item-title>
              </v-list-item>
              <v-list-item @click="editProfile">
                <v-list-item-title>Редактировать информацию</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
          
          <v-btn
            color="#baff29"
            dark
            @click="logout"
            class="ml-2"
          >
            Выйти
          </v-btn>
        </div>
      </div>
    </div>

    <v-container>
      <h1 class="page-title">Все квизы</h1>
      <v-row>
        <v-col
          v-if="quizzes.length"
          v-for="quiz in quizzes"
          :key="quiz.id"
          cols="4" lg="4"
        >
          <v-card class="quiz-card">
            <v-card-title class="quiz-title">{{ quiz.title }}</v-card-title>
            <v-img :src="quiz.image_url" height="200px" class="quiz-image"></v-img>
            <v-card-text>
              <div class="quiz-description">Описание: {{ quiz.description }}</div>
              <div class="quiz-author">Автор: {{ quiz.author }}</div>
              <div class="quiz-difficulty">Сложность: {{ quiz.difficulty }}</div>
              <div class="quiz-genres">Жанры: {{ quiz.genres }}</div>
              <v-btn 
                color="#baff29"
                @click="() => startQuiz(quiz.id)"
              >
                Начать квиз
              </v-btn>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useQuizStorage } from '../stores/quizStorage.js';
import axios from 'axios';

axios.defaults.withCredentials = true;

export default {
  setup() {
    const quizzes = ref([]);
    const questions = ref([]);
    const router = useRouter();
    const quizStore = useQuizStorage();
    const user = ref({});
    console.log(user.value)


    const goToResults = () => router.push(`/user/${user.value.id}/results`);
    const goToSettings = () => router.push('/settings');
    const editProfile = () => router.push('/profile/edit');

    
    const fetchUser = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/user/', { withCredentials: true });
        console.log('Ответ API:', response.data);
        user.value = response.data;
      } catch (error) {
        user.value = {};
      }
    };

    
    const logout = async () => {
      try {
        await axios.post('http://127.0.0.1:8000/api/logout/');
        user.value = '';
        router.push('/');
      } catch (error) {
        console.error('Ошибка при выходе:', error);
      }
    };


    const fetchQuizzes = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/quizzes/', { withCredentials: true });
        quizzes.value = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке квизов:', error);
      }
    };

    
    const startQuiz = async (quiz_id) => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/quizzes/${quiz_id}/`);
        questions.value = response.data;
        quizStore.setQuestions(quiz_id, response.data);

        if (response.data.length > 0) {
          const firstQuestionId = response.data[0].id;
          router.push(`/quiz/${quiz_id}/question/${firstQuestionId}`);
        }
      } catch (error) {
        console.error('Ошибка при загрузке вопросов:', error);
      }
    };

    
    onMounted(() => {
      fetchUser();
      fetchQuizzes();
    });

    return {
      quizzes,
      startQuiz,
      router,
      user,
      logout,
      goToResults,
      goToSettings,
      editProfile
    };
  },
};
</script>


<style scoped>
.welcome_text{
  text-align: center;
  color: #baff29;
  height: 20%;
  width: 100%;
  position: relative;
  top: 30%;
  font-family: "Kurale", serif;
  font-weight: 400;
  font-style: normal;
}
.welcome{
  height: 100%;
  width: 100%;
}
.home_page {
  background-color: #030027ff;
  min-height: 100%;
}
.page-title {
  font-family: "Kurale", serif;
  font-weight: 400;
  font-style: normal;
  color: #baff29;
  font-size: 36px;
  text-align: center;
  margin-bottom: 20px;
}
.quiz-card {
  font-family: "Kurale", serif;
  font-weight: 400;
  font-style: normal;
  background-color: #9a48d0ff;
  transition: transform 0.2s;
}
.quiz-card:hover {
  transform: scale(1.1);
}
.quiz-title {
  font-family: "Kurale", serif;
  font-weight: 400;
  font-style: normal;
  font-weight: 600;
  font-size: 40px;
  text-align: center;
  color:#030027ff;
}
.quiz-image {
  margin: 0 auto;
}
.quiz-description,
.quiz-author,
.quiz-difficulty,
.quiz-genres {
  margin-top: 8px;
  font-size: 20px;
  color: #030027ff;
}
.headers {
  height: 10%;
  background-color: #9a48d0ff;
}
.logo {
  position: absolute;
  top: 0%;
  left: 0%;
  z-index: 10;
  height: 37%;
}
.register-button-container {
  font-family: "Kurale", serif;
  font-weight: 400;
  font-style: normal;
  position: absolute;
  top: 3%;
  right: 1%;
  z-index: 10;
  font-size: 25px;
  font-weight: 600;
}
</style>