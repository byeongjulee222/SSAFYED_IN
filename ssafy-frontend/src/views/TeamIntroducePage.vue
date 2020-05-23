<template>
    <div>
        <BoardBanner style="background-color:#B39DDB;">
      <div style="line-height:1em; font-size:6vw; text-align:center; font-weight:bold; " slot="text">
        SSAFYed人 Team</div>
      </BoardBanner>

        <v-container>
            <v-row class="fill-height" align="center">
                <template v-for="user in intro">
                    <v-col :key="user.name" cols="12" class="my-6">
                        <v-hover v-slot:default="{ hover }">
                            <v-card :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }">
                                <div class="rank_div">
                                    <!-- <a :href="'/profile/' + intro.id"> -->
                                    <!--각자 myportfolio페이지 만들어서 등록하기-->
                                    <div class="rank_img hidden-xs-only">
                                        <img :src="getImgUrl(user.img)" style="border:1px solid #BDBDBD;"/>
                                        <!--hover-->
                                        <v-expand-transition>
                                            <div v-if="hover"
                                                class="d-flex light-blue transition-fast-in-fast-out v-card--reveal display-2 white--text text-sm-center">
                                                포트폴리오 보러가기
                                            </div>
                                        </v-expand-transition>
                                    </div>

                                    <div class="rank_title">
                                        <p class="rank_title title my-3 font-weight-bold">{{ user.name }}
                                            <span class="my-3 caption">{{ user.email }}</span>
                                        </p>
                                    </div>

                                    <div class="rank_cont">
                                        {{ user.tech}}
                                    </div>

                                    <!--기술스택-->
                                    <div class="rank_tech">
                                        <span class="font-weight-bold pa-2">기술스택 :</span><br />
                                        <v-chip v-for="(tech,index) in user.tech_category" :key="index" class="ma-2"
                                            label color="primary">
                                            <v-icon left>mdi-label</v-icon>
                                            {{ tech }}
                                        </v-chip>
                                    </div>
                                    <!-- </a> -->
                                </div>
                            </v-card>
                        </v-hover>
                    </v-col>
                </template>
            </v-row>
        </v-container>
    </div>
</template>

<script>
    import BoardBanner from '../components/BoardBanner'
    export default {
        name: 'TeamIntroducePage',
        data() {
            return {
                intro: [{
                        img: '성동민.jpg',
                        name: '성동민',
                        email: 'sung_dongmin@naver.com',
                        tech: 'JAVA, JAVASCRIPT, CSS3, HTML 잘합니다. 팀장이자 동네 북입니다',
                        tech_category: ['Java', 'Javascript', 'CSS3', 'HTML']
                    },
                    {
                        img: '이병주.jpg',
                        name: '이병주고약주고',
                        email: 'juya1503@gmail.com',
                        tech: 'Python, Django 쓸줄 압니다. 포항남자입니다. 야인시대 노래 좋아합니다. 끝입니다.',
                        tech_category: ['Python', 'Django']

                    },
                    {
                        img: '우동균.jpg',
                        name: '우동균',
                        email: 'wdj1207@naver.com',
                        tech: 'Python, Django 주니어의 주니어급입니다. 지금 몹시 배고픕니다.',
                        tech_category: ['Python', 'Django']
                    },
                    {
                        img: '김가은.jpg',
                        name: '김가은 a.k.a(코딩깡패)',
                        email: 'l9960204@naver.com',
                        tech: 'Java를 사용한 SafeFood 경험이 있으며 현재 subPJT2에서 Front를 맡아 수행하고 있습니다.',
                        tech_category: ['Java', 'Vue', 'Spring', 'HTML', 'Javascript']
                    }
                ],
            }
        },
        components: {
            BoardBanner
        },
        methods: {
            getImgUrl(img) {
                return require('../assets/' + img)
            }
        },
    }
</script>