<template>
    <div class="home_page">
        <v-container>
        <h1>все квизы</h1>
            <v-col v-if="quizzes.length" v-for="quiz in quizzes":key="quiz.id" cols="6" rows="6">
                <v-btn>
                    <v-card>
                        <v-row>
                            <v-card-title> {{quiz.title}}</v-card-title>
                            <v-card-description>Описание квиза: {{quiz.description }}</v-card-description>
                            <v-card-genres>Жанры: {{quiz.genres}}</v-card-genres>
                            <v-card-author>Автор квиза: {{quiz.author }}</v-card-author>
                            <v-card-difficulty>Сложность квиза: {{quiz.difficulty }}</v-card-difficulty>
                        </v-row>
                    </v-card>
                </v-btn @click="$router.push('/quiz/')">  
            </v-col>
        </v-container>
    </div>
</template>

<style scoped>
    .home_page{
        background-color: #030027ff;
        height: 100%;
    }
    .v-btn, .v-card, .v-row{
        color:#030027ff;
        height:100%;
        margin: 2%;
        background-color: #9a48d0ff;
    }
    .logo {
        position: absolute;
        top: 0%;
        left: 0%;
        z-index: 10;
        height: 37%;
    }
    .content-wrapper{
        background-color: #030027ff;
        height: 15%;
        width: 100%;
    }
    .logo_text{
        font-size: 50px;
        font-weight: 600;
        color: #baff29;
        position: relative;
        top: 20%;
        left: 7%;
    }
</style>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      quizzes: [], 
    };
  },
  created() {
    this.fetchQuizzes();
  },
  methods: {
    fetchQuizzes() {
      axios.get('http://127.0.0.1:8000/api/quizzes/') 
        .then(response => {
          this.quizzes = response.data;
        })
        .catch(error => {
          console.error('Ошибка при загрузке квизов:', error);
        });
    }
  }
}
</script>