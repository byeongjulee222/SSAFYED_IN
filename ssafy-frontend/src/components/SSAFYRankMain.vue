<template>
  <v-container>
    <v-card max-width="550" class="mx-auto">
      <v-list three-line tag>
        <template v-for="(item, i) in items">
          <v-list-item :key="i" @click='moveUserPage(item.id)'>
            <v-list-item-avatar>
              <img :src="getProfileImage(item.profile_img)"/>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="item.nickname"></v-list-item-title>
              <v-list-item-subtitle v-html="item.introduce" class="subtitle"></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    name: 'SSAFYRankMain',
    data: () => ({
      items: [],
      flag: true,
    }),
    methods: {
      moveUserPage(value) {
        location.href = "/profile/" + value
      },
      getProfileImage(value) {
        if (value == '' || value == null){
          return require('../assets/no_picture.png');
        }else
          return value;
      },
    },
    mounted() {
        axios.get('/accouts/')
          .then(res => {
            this.items = res.data
            this.items = this.items.slice(0, 7)
          })
          .catch(err => {
            console.log("SSAFYRank Main화면 값 불러오기 실패")
          })
    }
  }
</script>

<style>
.subtitle-2 {
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
</style>