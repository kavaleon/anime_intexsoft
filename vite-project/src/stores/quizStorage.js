import { defineStore } from 'pinia';

export const useQuizStorage = defineStore('quiz', {
  ststate: () => ({
  quizId: null,
  questions: [],
  answers: [],
  currentQuestionIndex: 0,
  question: null,
}),
actions: {
  setQuestions(quiz_id, questions) {
    // сохранение вопросов
    this.quizId = quiz_id;
    this.questions = questions;
    this.answers = Array(questions.length).fill(null);
    this.currentQuestionIndex = 0;
    this.setQuestion();
  },
  setQuestion() {
    // текущий вопрос
    this.question = this.questions[this.currentQuestionIndex];
  },
  setAnswer(answer) {
    // сохранение ответа
    this.answers[this.currentQuestionIndex] = answer;
  },
  next() {
    // выбор следующего вопроса
    if (this.currentQuestionIndex + 1 < this.questions.length) {
      this.currentQuestionIndex += 1;
      this.setQuestion();
    }
  }
},
});

