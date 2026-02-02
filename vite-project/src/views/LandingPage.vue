<template>
  <div class="landing-page" style="position: relative; height: 100vh;">
    <div class="content-wrapper">
      
      <img
        src="../assets/landing_page_fon.jpg"
        alt="Landing Image"
        class="landing-image"
      />
      
      
      <div class="full-width-text">
        ГОТОВ К НАСТОЯЩЕМУ АНИМЕ-МАРАФОНУ?
      </div>

      <div class="full-width-carousel">
        <Splide :options="fullWidthOptions">
          <SplideSlide v-for="(image, index) in fullWidthImages" :key="index">
            <img :src="'../landing_page/' + image" style="width: 100%; height: auto;" />
          </SplideSlide>
        </Splide>
      </div>
      
      <div class="part-width-text">
        Сотня классных квизов с Вашими любимыми персонажами
      </div>

      <div class="sliders_img">
        <div style="padding-bottom: 2%;">
          <Splide :options="options1">
            <SplideSlide v-for="(image, index) in images" :key="index">
              <img :src="'../quizzes/' + image" width="200" height="200" />
            </SplideSlide>
          </Splide>
        </div>

        
        <div style="padding-top: 2%;">
          <Splide :options="options2">
            <SplideSlide v-for="(image, index) in images" :key="index">
              <img :src="'../quizzes/' + image" width="200" height="200"/>
            </SplideSlide>
          </Splide>
        </div>
      </div>
      
      <div class="part-width-text">
        Угадывайте аниме по самым эпичным и трогательным моментам
      </div>
      
      <div class="anime-gif">
        <Splide :options="options3">
          <SplideSlide v-for="(gif, index) in gifs" :key="index">
            <img :src="'../gifs/' + gif" width="600" height="300"/>
          </SplideSlide>
        </Splide>
      </div>

      <div class="part-width-text">
        Все это на Yume Quiz
      </div>
      
      <div class="register-button-container">
        <v-btn 
          color="#baff29" 
          dark  
          @click="$router.push('/auth/register')"
        >
          Регистрация
        </v-btn>
      </div>

      
      <div class="logo">
        <img
          src="../assets/logo.png"
          alt="Logo"
          class="logo"
        />
      </div>
    </div>
  </div>
</template>


<script>
import { Splide, SplideSlide } from '@splidejs/vue-splide';

export default {
  components: {
    Splide,
    SplideSlide,
  },
  data() {
    return {
      images: [
        'quiz1.jpg',
        'quiz2.jpg',
        'quiz3.jpg',
        'quiz4.jpg',
        'quiz5.jpg',
        'quiz6.jpg',
        'quiz7.jpg',
        'quiz8.jpg',
        'quiz9.jpg',
        'quiz10.jpg',
        'quiz11.jpg',
        'quiz12.jpg',
        'quiz13.jpg',
        'quiz14.jpg',
        'quiz15.jpg',
        'quiz16.jpg',
        'quiz17.jpg',
      ],
      gifs: [
        'gif1.gif',
        'gif2.gif',
        'gif3.gif',
        'gif4.gif',
        'gif5.gif',
      ],
      fullWidthImages: ['frame1.png', 'frame2.png', 'frame3.png'],
      fullWidthOptions: {
        type: 'loop',
        perPage: 1,
        autoplay: true,
        interval: 3000, // через 3 сек
        speed: 5000,
        arrows: true,
        pagination: false,
        drag: false,
        height: '100vh', // занимает весь экран по высоте
        width: '100%', // по ширине экрана
      },
      options1: {
        type: 'loop',          
        perPage: 7,             
        autoplay: true,         
        interval: 0,            
        speed: 100000,                   
        arrows: false,          
        pagination: false,     
        drag: false,    
        direction: 'ltr',             
      },
      options2: {
        type: 'loop',          
        perPage: 7,             
        autoplay: true,         
        interval: 0,            
        speed: 90000,                   
        arrows: false,          
        pagination: false,     
        drag: false,  
        direction: 'rtl',               
      },
      options3: {
        type: 'loop',          
        perPage: 3,             
        autoplay: true,         
        interval: 0,            
        speed: 90000,                   
        arrows: false,          
        pagination: false,     
        drag: false,  
        direction: 'ltr',               
      }
    }
  }
}
</script>


<style scoped>
.sliders_img{
  padding-top: 5%;
  padding-bottom: 5%;
  background-color: #030027ff;
}
.full-width-carousel{
  background-color: #030027ff;
}
.logo {
    position: absolute;
    top: 0%;
    left: 0%;
    z-index: 10;
    height: 37%;
}

.part-width-text{
  /* font-family: "Ruslan Display", sans-serif;
  font-weight: 400;
  font-style: normal; */
  font-family: "Kurale", serif;
  font-weight: 500;
  font-style: normal;
  background-color: #9a48d0ff;
  width: 100%;
  padding-top: 2%;
  padding-bottom: 2%;
  text-align: center; 
  font-size: 60px;
  color: #030027ff;
  align-content: center;
}
.anime-gif{
  background-color: #030027ff;
  height: 60%;
  padding-top: 5%;
  padding-bottom: 5%;
}
.content-wrapper {
  position: relative;
  height: 100%;
  padding-top: 5%; 
  box-sizing: border-box;
  width: 100%;
  background-color: #030027ff;
}

.landing-image {
  width: 100%;
  height: 90%;
  object-fit: cover;
  margin: 0px;
}

.register-button-container {
  position: absolute;
  top: 3%;
  right: 1%;
  z-index: 10;
  font-size: 25px;
  font-weight: 600;
}

.full-width-text {
  font-family: "Kurale", serif;
  font-weight: 400;
  font-style: normal;
  width: 100%;
  height: 25%;
  padding: 10px;
  box-sizing: border-box;
  text-align: center; 
  font-size: 70px;
  background-color: #030027ff;
  margin: 0;
  color: #baff29;
  align-content: center;
}

.landing_page{
  background-color: #030027ff;
  margin: 0;
}

</style>