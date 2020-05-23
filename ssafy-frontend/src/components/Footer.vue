<template>
  <v-footer dark padless>
    <v-card flat tile class="grey darken-3 text-left hidden-xs-only" width="100%">

      <div style="float:left;">
        <v-card-text class="white--text">
          이용약관
        </v-card-text>
      </div>
      <div>
        <v-card-text class="blue--text font-weight-bold">
          개인정보처리취급방침
        </v-card-text>
      </div>

      <v-card-text class="grey--text caption">
        대전광역시 유성구 덕명동 124 삼성화재 유성연수원<br>
        <p class="white--text caption ma-0">대표번호 02-3429-5544<span style="color:grey;"> 상담시간 : 평일 09:00 ~ 18:00</span>
        </p>
      </v-card-text>

      <v-card-text>
        <p class="caption ma-0">
          해당 프로젝트는 SSAFY 사람들과의 커뮤니티를 위해 제작되었으며<br>취업, 이직, 공모전, 스터디를 위한 SSAFY만의 인적 네트워크를 구축하자는 취지로 개발 중입니다.</p>
      </v-card-text>

      <v-divider class="ma-0"></v-divider>

      <v-card-text class="white--text text-center">
        {{ new Date().getFullYear() }} — <router-link class="white--text" style="text-decoration: none;" to="/team">
          <strong>GTA5</strong></router-link>
      </v-card-text>
    </v-card>

    <v-bottom-navigation v-model="activeBtn" :input-value="showNav"
      class="light-blue lighten-2 black--text text-center hidden-sm-and-up" fixed>

      <v-btn v-for="item in footMenu" :key="item.title" :to="item.path">
        <span class="black--text">{{ item.title }}</span>
        <v-icon>{{ item.icon }}</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-footer>
</template>

<script>
  export default {
    name: 'Footer',
    data: () => ({
      icons: [
        'fab fa-google-plus',
        'fab fa-linkedin',
        'fab fa-github'
      ],
      footMenu: [{
          title: "Home",
          path: "/",
          icon: "home",
        },
        {
          title: "Portfolio",
          path: "/portfolio",
          icon: "developer_board",
        },
        {
          title: "Rectuit",
          path: "/rectuit",
          icon: "contacts",
        },
        {
          title: "Competition",
          path: '/competition',
          icon: "forum",
        },
        {
          title: "SSAFYed人",
          path: "/ssafyrank",
          icon: "assignment_ind",
        },

      ],
      activeBtn: 1,
      showNav: true,
    }),
  }
</script>