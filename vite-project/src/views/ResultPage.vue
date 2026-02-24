<template> 
      <v-container> 
            <v-card class="mx-auto" max-width="600"> 
                  <v-card-title>Результаты теста</v-card-title> 
                  <v-card-text> 
                        <div v-if="result"> 
                              <p>Quiz ID: {{ result.quiz_id }}</p> 
                              <p>Ваш результат: {{ result.score }} из {{ result.total }}</p> 
                        </div> 
                  </v-card-text> 
            </v-card> 
      </v-container> 
</template> 

<script> 
import { ref, onMounted } from 'vue'; 
import { useRoute } from 'vue-router'; 
import axios from 'axios'; 

export default {
       setup() { 
            const route = useRoute(); 
            const result = ref(null); 
            console.log(result)
            onMounted(async () => { 
                  const dataJson = route.query.data; 
                  if (dataJson) { 
                        console.log(dataJson)
                        result.value = JSON.parse(dataJson); 
                  } 
                  else { 
                        const quizId = route.params.quizId; 
                        console.log(quizID)
                        const resp = await axios.get(`http://127.0.0.1:8000/api/quiz/${quizId}/result/`); 
                        result.value = resp.data; 
                        } 
                  })
                               
            return { 
                  result, 
            }; }, 
      }; 
</script>