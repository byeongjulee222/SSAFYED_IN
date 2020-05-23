<template>
  <div id="portfolioBody">
    <!--배너-->
    <BoardBanner style="background-color:#2196f3;">
      <div style="line-height:1em; font-size:6vw; text-align:center; font-weight:bold; " slot="text">
        Portfolio</div>
    </BoardBanner>
    <SearchBar v-on:create_search="getText"></SearchBar>
 
    <!-- Portfolio -->
    <v-layout>
      <v-flex xs12>
        <div class="text-center">
          <SSAFYPortfolioList :portfolios="portfolios"></SSAFYPortfolioList>
          <div style="margin:0 50px 0 50px !important">
             <v-btn v-if="moreBtn" class="my-10" block color="grey" @click="moreLoad" outlined>
              <v-icon>expand_more</v-icon>
            </v-btn>
          </div>
        </div>
      </v-flex>
    </v-layout>
    <ScrollToTop class="hidden-xs-only"></ScrollToTop>
  </div>
</template>

<script>
  import SSAFYPortfolioList from '../components/SSAFYPortfolioList'
  import BoardBanner from '../components/BoardBanner'
  import SearchBar from '../components/SearchBar'
  import ScrollToTop from '../components/ScrollToTop'

  export default {
    name: 'PortfolioPage',
    data() {
      return {
        search_text: '',
        copyPortfolios: [],
        portfolios: [],
        more: 6,
        moreBtn: false,
      }
    },
    components: {
      SSAFYPortfolioList,
      BoardBanner,
      SearchBar,
      ScrollToTop,
    },
    methods: {
      getText(text) {
        this.search_text = text
        console.log("검색 내용은:" + this.search_text)
        axios.post('/portfolios/pagelist/', {
            search_text: this.search_text
          })
          .then(res => {
            if(res.data[0].length == 0) {
              alert('검색 결과가 없습니다.')
            } else {
              this.copyPortfolios = res.data[0]
              this.portfolios = res.data[0]
              console.log(this.portfolios)
              if (this.portfolios.length == 0 || this.portfolios.length < this.more) {
                this.moreBtn = false
              } else {
                this.portfolios = this.portfolios.slice(0, 6)
                console.log(this.portfolios)
                this.moreBtn = true
              }
            }
          })
          .catch(err => {
            console.log(err)
          })
      },
      moreLoad() {
        this.more += 6
        this.portfolios = this.copyPortfolios.slice(0, this.more)
        if (this.more > this.portfolios.length) this.moreBtn = false
      }
    },
  }
</script>