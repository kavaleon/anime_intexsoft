<script setup>
import page404Gif from '../assets/page404.gif';
</script>

<template>
    <div>
        <center>
            <h1>404 not found</h1>
            <img :src="page404Gif" alt="404 GIF" />
            <h2>иди куда шел</h2>
        </center>
    </div>
</template>


<style scoped>
.not-found-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
}

</style>