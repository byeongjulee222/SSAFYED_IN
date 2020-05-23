<template>
  <div id="portfolioBody">
      <BoardBanner style="background-color:#ffb6c1;">
      <div style="line-height:1em; font-size:6vw; text-align:center; font-weight:bold; " slot="text">
        Recruit</div>
      </BoardBanner>
      <!-- Post -->
      <template v-if="idx === undefined"> 
        <v-layout>
          <v-flex xs12>
            <RecruitList :limits="6" :load-more="true"></RecruitList>
          </v-flex>
        </v-layout>
      </template>
      <ScrollToTop class="hidden-xs-only"></ScrollToTop>

  </div>
</template>

<script>
import RecruitList from '../components/recruit/RecruitList'
import BoardBanner from '../components/BoardBanner'
import ScrollToTop from '../components/ScrollToTop'
export default {  
  name: 'RecruitPage',
  data() { 
    const idx = this.$route.params.id
    return{
      idx: idx
    }
  },
  components: {
    RecruitList,
    BoardBanner,
    ScrollToTop
  }
}
</script>
