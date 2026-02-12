<template>
  <div class='quiz'>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'QuizLayout'
}
</script>

<style scoped>
  .quiz{
    background-color: #030027ff;
    height: 100%;
    width: 100%;
  }
</style>