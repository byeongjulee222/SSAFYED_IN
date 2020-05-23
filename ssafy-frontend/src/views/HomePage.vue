<template>
  <div>
    <!--이미지 배너-->
    <MainBanner></MainBanner>

    <!--공고 카운트 배너-->
    <CountBanner class="hidden-xs-only"></CountBanner>

    <!--포트폴리오-->
    <div style="background-color:#F5F5F5; padding-top:15px;">
      <router-link to="/portfolio">
        <h2 class="display-1 my-5">Portfolio</h2>
      </router-link>
      <v-flex lg12>
        <SSAFYPortfolioList :portfolios="portfolios"></SSAFYPortfolioList>
      </v-flex>
    </div>

    <!--수시채용, 공모전-->
    <v-row class="ma-8">
      <v-col cols="12" lg="6" md="6">
        <SSAFYPostList></SSAFYPostList>
      </v-col>
      <v-col cols="12" lg="6" md="6">
        <router-link to="/ssafyrank">
          <h2 class="display-1 my-5 mx-3">SSAFYED人 Rank</h2>
        </router-link>
        <SSAFYRankMain></SSAFYRankMain>
      </v-col>
    </v-row>
    <ScrollToTop class="hidden-xs-only"></ScrollToTop>
  </div>
</template>

<script>
  import Vue from 'vue'
  import MainBanner from '../components/MainBanner'
  import CountBanner from '../components/CountBanner'
  import SSAFYPortfolioList from '../components/SSAFYPortfolioList'
  import SSAFYPostList from '../components/SSAFYPostList'
  import SSAFYRankMain from '../components/SSAFYRankMain'
  import ScrollToTop from '../components/ScrollToTop'

  export default {
    name: 'HomePage',
    data() {
      return {
        portfolios: [],
      }
    },
    components: {
      MainBanner,
      CountBanner,
      SSAFYPortfolioList,
      SSAFYPostList,
      SSAFYRankMain,
      ScrollToTop,
    },
    created() {
      axios.get('/portfolios/')
        .then(res => {
          this.portfolios = res.data.slice(0, 6)
        })
        .catch(err => {
          console.log("메인홈페이지 포트폴리오 못가져옴")
        })
    }
  }
</script>

<style scoped>
  h2 {
    text-align: center;
  }
</style>