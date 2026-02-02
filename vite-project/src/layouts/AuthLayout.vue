<template>
  <div id='auth'>
    <h2>Auth Layout</h2>
    <nav>
      <router-link to="/auth/login">Вход</router-link>
      <router-link to="/auth/register">Регистрация</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'AuthLayout'
}
</script>