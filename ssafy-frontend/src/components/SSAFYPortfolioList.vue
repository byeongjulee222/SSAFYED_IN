<template>
  <div class="text-center my-8" style="margin:0 50px 0 50px !important">
    <v-row class="fill-height" align="center">
      <template v-for="(item, i) in portfolios">
        <v-col :key="i" cols="12" md="4" sm="12" class="my-5">
          <v-hover v-slot:default="{ hover }">
            <v-card :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }" @click="detailPortfolio(item.id)">
              <img :src="item.content_img_1" width="100%" height="250px" />
              <div class="light-blue darken-2">
                <p class="subheading pa-2 white--text font-weight-black">{{item.title}}</p>
                <p class="text-end pa-2 white--text font-weight-medium ma-0">{{ item.user.nickname }}</p>
                <p class="caption font-weight-medium font-italic text-end white--text pr-2 pb-1">{{ item.created_at }}
                </p>
              </div>
            </v-card>
          </v-hover>
          <div v-if="flag">

            <v-btn class="white--text" color="success" dark @click="changePublic(item.id, !locks[i])" v-if="locks[i]">
              <v-icon>lock_open</v-icon>Public
            </v-btn>
            <v-btn class="white--text" color="error" dark @click="changePublic(item.id, !locks[i])" v-else>
              <v-icon>lock</v-icon>Private
            </v-btn>

          </div>
        </v-col>
      </template>
    </v-row>
  </div>
</template>

<style scoped>
  .v-card {
    transition: opacity .4s ease-in-out;
  }

  .v-card:not(.on-hover) {
    opacity: 0.6;
  }

  .show-btns {
    color: rgba(255, 255, 255, 1) !important;
  }
</style>

<script>
  export default {
    name: 'SSAFYPortfolioList',
    data: () => ({
      transparent: 'rgba(255, 255, 255, 0)',
    }),
    props: {
      portfolios: Array,
      locks: Array,
      flag: Boolean,
    },
    methods: {
      detailPortfolio(value) {
        console.log(value);
        location.href = '/detailPort/' + value;
      },
      changePublic(id, val) {
        console.log(val)
        var check_portfolio = confirm("포트폴리오 상태를 변경하시겠습니까?")
        if (check_portfolio) {
          axios.put('/portfolios/' + id + '/delete_update/', {
              public: val
            })
            .then(res => {
              alert('포트폴리오 상태가 변경되었습니다!', )
              location.reload()
            })
            .catch(err => {
              console.log("공개/비공개 상태 변경 실패")
            })
        }
      }
    },
  }
</script>

<style scoped>
  .subheading {
    overflow: hidden;
    text-overflow: ellipsis;
    display: inline-block;
    white-space: normal;
    height: 1.8em;
    text-align: left;
    word-wrap: break-word;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }

  p {
    font-size: 20px;
    color: black;
    padding-left: 5px;
  }

  #detailPort {
    display: none;
  }
</style>