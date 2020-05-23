<template>
  <v-card color="#8E87F1" dark flat tile height="250">

    <div class="pt-10">
      <v-container >
        <v-row >
          <v-col cols="3">
            <router-link :to="'/ssafyrank/'">
              <div class="counters">
                <v-card-text class="display-2">
                  <AnimatedNumber :value="users_value" :formatValue="formatToUsers" :duration="500" />
                </v-card-text>
                <span>사용자</span>
              </div>
            </router-link>
          </v-col>
          <v-col cols="3">
            <router-link :to="'/recruit/'">
              <div class="counters">
                <v-card-text class="display-2">
                  <AnimatedNumber :value="recruits_value" :formatValue="formatToRecruit" :duration="500" />
                </v-card-text>
                <span>채용공고</span>
              </div>
            </router-link>
          </v-col>
          <v-col cols="3">
            <router-link :to="'/competition/'">
              <div class="counters">
                <v-card-text class="display-2">
                  <AnimatedNumber :value="competitions_value" :formatValue="formatToCompetition" :duration="500" />
                </v-card-text>
                <span>공모전</span>
              </div>
            </router-link>
          </v-col>
          <v-col cols="3">
            <router-link :to="'/portfolio/'">
              <div class="counters">
                <v-card-text class="display-2">
                  <AnimatedNumber :value="portfolios_value" :formatValue="formatToPortfolios" :duration="500" />
                </v-card-text>
                <span>포트폴리오</span>
              </div>
            </router-link>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </v-card>
</template>

<script>
  import AnimatedNumber from "animated-number-vue"

  export default {
    data: () => ({
      users_value: 1,
      portfolios_value: 1,
      competitions_value: 1,
      recruits_value: 1,
    }),
    components: {
      AnimatedNumber
    },
    methods: {
      formatToCompetition(value) {
        return `${Number(value).toFixed(0)}`
      },
      formatToRecruit(value) {
        return `${Number(value).toFixed(0)}`
      },
      formatToUsers(value) {
        return `${Number(value).toFixed(0)}`
      },
      formatToPortfolios(value) {
        return `${Number(value).toFixed(0)}`
      }
    },
    created() {
      //포트폴리오 개수
      axios.get('/portfolios/')
        .then(res => {
          this.portfolios_value = res.data.length
        })

      //사용자 누적 수
      axios.get('/accouts/')
        .then(res => {
          this.users_value = res.data.length
        })

      //채용 공고 수
      axios.get('/recruits/')
        .then(res => {
          this.recruits_value = res.data[1].recruit_count
        })


      //공모전 수
      axios.get('/competitions/')
        .then(res => {
          this.competitions_value = res.data[1].competition_count
        })
    }
  }
</script>

<style>
  .counters {
    border: 1px solid white;
    text-align: center;
    padding-bottom: 20px;
    padding-top: 8px;
  }
</style>