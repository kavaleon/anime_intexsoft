<template>
      <v-card>
        <div v-if="currentQuestion.options.length !== 0">
          <v-card-text v-if="currentQuestion">
            <h2>Вопрос {{ currentQuestion.id }}</h2>
            
            <v-img :src="currentQuestion.image_url" height="200px" class="question-image"></v-img>
            
              <v-radio-group >
                <v-row>
                  <v-col
                  cols="4"
                  >
                    <v-radio class="radioButton"
                    
                      v-for="option in currentQuestion.options"
                      :key="option.id"
                      :label="option.text"
                      :value="option"
                      color="#baff29"
                      style="opacity: 50%"
                      :model-value="selectedAnswer"

                      @change="selectAnswer(option)"
                    ></v-radio>
                  </v-col>
                </v-row>
              </v-radio-group>
              <v-btn
              color="#baff29"
              @click="nextQuestion"
              :disabled="!selectedAnswer"
               >
              Далее
            </v-btn>
          </v-card-text>
      </div>

          
        <div v-else>
          <h2>конэц</h2>
          <v-btn
              color="#baff29"
              @click="showResult"
               >
              Посмотреть результаты
            </v-btn>
        </div>
      </v-card>
</template>

<script>
import { ref, computed, watch } from 'vue';
import { useQuizStorage } from '../../stores/quizStorage';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
  setup() {
    const quizStore = useQuizStorage();
    const router = useRouter();
    const currentQuestion = computed(() => quizStore.question);
    const selectedAnswer = ref(quizStore.answers[quizStore.currentQuestionIndex]);
    const user_id = quizStore.userId
    
    watch(
      () => quizStore.currentQuestionIndex,
      (newVal) => {
        selectedAnswer.value = quizStore.answers[newVal];
      }
    );

    const selectAnswer = (answer) => {
      selectedAnswer.value = answer;
      quizStore.setAnswer(answer);
    };

    const nextQuestion = () => {
      quizStore.next();
    };

    const showResult = () => {
      sendResult()
      console.log(quizStore.answers)
      router.push(`/quiz/${quizStore.quizId}/result`);
    }

    const sendResult = () =>{
      const response = axios.post('http://127.0.0.1:8000/api/quiz/user_id/result/', {
        user_id: quizStore.userId,
        answers: quizStore.answers
      }, {
      headers: {
          'Content-Type': 'application/json'
      }
      });
    
    }

    return {
      currentQuestion,
      selectedAnswer,
      selectAnswer,
      nextQuestion,
      showResult,
      sendResult,
    };
  },
};
</script>

<style scoped>
.question-image {
  height: 200px;
  width: 200px;
}
.v-card{
  height: 50%;
  width: 50%;
  background-color: #9a48d0ff;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.radioButton:hover {
  background-color: rgba(96, 30, 139, 0.753);
}
.radioButton:checked {
  background-color: rgba(96, 30, 139, 0.753);
}

</style>