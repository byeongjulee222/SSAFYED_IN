<template>
  <div id="portfolioBody">
      <BoardBanner style="background-color:#ffc3a0;">
      <div style="line-height:1em; font-size:6vw; text-align:center; font-weight:bold; " slot="text">
        Competition</div>
      </BoardBanner>
      <!-- Post -->
      <template v-if="idx === undefined"> 
        <v-layout>
          <v-flex xs12>
            <CompetitionList :limits="6" :load-more="true"></CompetitionList>
          </v-flex>
        </v-layout>
      </template>
      
      <CompetitionDetail v-if="idx != undefined"></CompetitionDetail>
      <ScrollToTop class="hidden-xs-only"></ScrollToTop>

  </div>
</template>

<script>
import CompetitionList from '../components/competition/CompetitionList'
import CompetitionDetail from '../components/competition/CompetitionDetail'
import BoardBanner from '../components/BoardBanner'
import ScrollToTop from '../components/ScrollToTop'
export default {  
  name: 'CompetitionPage',
  data() { 
    const idx = this.$route.params.id
    return{
      idx: idx
    }
  },
  components: {
    CompetitionList,
    CompetitionDetail,
    BoardBanner,
    ScrollToTop
  }
}
</script>
