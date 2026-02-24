<template>
  <v-container>
    <v-card class="mx-auto" max-width="800" v-if="isAuthenticated">
      <v-card-title>Мои пройденные тесты</v-card-title>
      <v-data-table
        :headers="headers"
        :items="results"
      >
        <template #item="{ item }">
          <tr>
            <td>{{ item.quiz_name }}</td>
            <td>{{ item.score }}</td>
            <td>{{ item.total }}</td>
            <td>{{ (item.finished_at) }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-card>
    <div v-else>
      <p>Пожалуйста, авторизуйтесь, чтобы видеть результаты.</p>
    </div>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const user = ref({});
    const results = ref([]);
    const isAuthenticated = ref(false);
    const headers = [
      { text: 'Название теста', value: 'quiz_name' },
      { text: 'Результат', value: 'score' },
      { text: 'Из', value: 'total' },
      { text: 'Дата прохождения', value: 'finished_at' },
    ];

  
    const fetchUser = async () => {
      try {
        const resp = await axios.get('http://127.0.0.1:8000/api/user/', { withCredentials: true });
        user.value = resp.data;
        fetchResults();
        isAuthenticated.value = true;
      } catch (e) {
        user.value = {};
        isAuthenticated.value = false;
        console.log('Ошибка при получении пользователя', e);
      }
    };

    const fetchResults = async () => {
      try {
        const userId = user.value?.id;
        const resp = await axios.get(`http://127.0.0.1:8000/api/user/${userId}/results`, { withCredentials: true });
        results.value = resp.data.map(r => ({
          quiz_name: r.quiz.title,
          score: r.score,
          total: r.total,
          finished_at: r.finished_at,
        }));
      } catch (e) {
        console.error('Ошибка при получении результатов', e);
        results.value = [];
      }
    };



    onMounted(() => {
      fetchUser();
    });

    return {
      results,
      headers,
      isAuthenticated,
    };
  },
};
</script>