<template>
    <div class="grey lighten-4">
        <v-card-text>
            <v-sheet max-width="800" class="mx-auto">
                <div class="form_data">
                    <!--제목-->
                    <div id="title">
                        <h2 class="headline">{{ portfolio.title }}</h2>
                        <v-card-text class="text-end title pa-0 pb-1">
                            <p class="font-weight-bold ma-0">
                                <router-link :to="'/profile/'+portfolio.user.id">{{ portfolio.user.nickname }}
                                </router-link>
                            </p>
                        </v-card-text>
                        <p class="text-end">프로젝트 기간 : {{ portfolio.project_start }} ~
                            {{ portfolio.project_start }}</p>
                        <v-divider></v-divider><br>
                    </div>

                    <div id="contents">

                        <!--대표 이미지 설정-->
                        <v-card>
                            <div>
                                <a :href="portfolio.content_img_1" target="blank"><img :src="portfolio.content_img_1" width="100%" /></a>
                            </div>
                        </v-card>

                        <!--설명-->
                        <v-card-title class="pl-0">프로젝트 설명</v-card-title>
                        <v-textarea outlined v-model="portfolio.content_sub_1" readonly>
                        </v-textarea>

                        <v-card-title class="pl-0">프로젝트 디테일 컷</v-card-title>

                        <!--서브 이미지 & 콘텐츠-->
                        <div v-for="(sub, index) in contents" :key="index">
                            <v-card class="upload_image pad">
                                <div>
                                    <a :href="sub.img" target="blank"><img :src="sub.img" width="100%" /></a>
                                </div>
                            </v-card>
                            <v-text-field outlined v-model="sub.text" readonly></v-text-field>
                        </div>

                        <!--프로젝트 파일-->
                        <!-- <v-file-input class="ma-4" show-size label="첨부파일" readonly></v-file-input> -->

                        <!--카테고리-->
                        <v-chip v-for="techName in portfolio.tech_category" class="ma-2" label color="primary"
                            :key="techName.tech_stack">
                            <v-icon left>mdi-label</v-icon>
                            {{ techName.tech_stack }}
                        </v-chip>
                    </div>
                    <v-divider></v-divider>
                    <div class="text-end">
                        <span class="caption">작성일 : {{ portfolio.created_at }}</span>
                    </div>

                    <!--버튼-->
                    <!--Web ver-->
                    <div id="userBtnweb" style="text-align:center" class="hidden-xs-only ma-12">
                        <v-tooltip bottom v-if="flag">
                            <template v-slot:activator="{ on }">
                                <v-btn class="ma-4" large fab color="primary" v-on="on" @click="moveDetailPage">
                                    <v-icon>mdi-pencil</v-icon>
                                </v-btn>
                            </template>
                            <span>edit</span>
                        </v-tooltip>

                        <!--내가올린 글이 아닐 때 보일 아이콘-->
                        <v-tooltip bottom>
                            <template v-slot:activator="{ on }">
                                <v-btn class="ma-2" large fab color="orange" v-on="on" @click="moveHistoryBack">
                                    <v-icon color="white">format_list_bulleted</v-icon>
                                </v-btn>
                            </template>
                            <span>list</span>
                        </v-tooltip>
                    </div>


                    <!--Mobile ver-->
                    <div id="userBtnMobile" style="text-align:center" class="hidden-sm-and-up my-5">
                        <v-btn class="ma-2" large color="primary" @click="moveDetailPage">Edit</v-btn>
                        <v-btn class="ma-2 white--text" large color="orange" @click="moveHistoryBack">list</v-btn>
                    </div>


                    <!--댓글-->
                    <div id="comment">
                        <p class="text-start font-weight-medium title">Comment</p>
                        <v-row class="text-center">
                            <v-col cols="12" class="pl-3" md="10" sm="10" >
                                <v-textarea v-model="comment" outlined height="80" placeholder="Leave a comment">
                                </v-textarea>
                                <v-btn text outlined block @click="postComment" class="hidden-sm-and-up">write</v-btn>
                            </v-col>

                            <v-col cols="12" class="hidden-xs-only" md="2" sm="2">
                                <v-btn text outlined height="80" @click="postComment">write</v-btn>
                            </v-col>

                        </v-row>
                        <div v-for="comment in portfolio.comment_set" :key="comment.id">
                            <p class="ma-0 text-start title">{{ comment.user.nickname }}
                                <span class="caption" style="color:grey;">{{comment.created_at.slice(0, 19) }}</span>
                            </p>
                            <p class="text-start my-2">{{ comment.content }}</p>
                            <v-divider class="pa-2"></v-divider>
                        </div>
                    </div>
                </div>

            </v-sheet>
        </v-card-text>
        <ScrollToTop class="hidden-xs-only"></ScrollToTop>
    </div>
</template>

<script>
    import ScrollToTop from '../components/ScrollToTop'

    export default {
        name: 'DetailPortfolioPage',
        data() {
            return {
                portfolio: '',
                comment: '',
                id: Number(this.$route.params.id),
                login_uid: sessionStorage.getItem("uid"),
                contents: [],
                flag: false,
            }
        },
        components: {
            ScrollToTop,
        },
        created() {
            axios.get('/portfolios/' + this.id)
                .then(res => {
                    this.portfolio = res.data

                    if (this.portfolio.content_img_2) this.contents.push({
                        img: this.portfolio.content_img_2,
                        text: this.portfolio.content_sub_2
                    })

                    if (this.portfolio.content_img_3) this.contents.push({
                        img: this.portfolio.content_img_3,
                        text: this.portfolio.content_sub_3
                    })

                    if (this.portfolio.content_img_4) this.contents.push({
                        img: this.portfolio.content_img_4,
                        text: this.portfolio.content_sub_4
                    })

                    if (this.portfolio.content_img_5) this.contents.push({
                        img: this.portfolio.content_img_5,
                        text: this.portfolio.content_sub_5
                    })

                    console.log("contents")
                    console.log(this.contents)
                    console.log(this.portfolio)
                    this.flag = this.login_uid == this.portfolio.user.id ? true : false
                })
                .catch(err => {
                    console.log("Portfolio Detail Fail")
                })
        },
        methods: {
            postComment() {
                if (this.login_uid == undefined || this.login_uid == '' || this.login_uid == null) {
                    alert("로그인시 이용가능합니다.")
                    this.comment = ''
                } else {
                    const requestHeader = {
                        headers: {
                            Authorization: 'JWT ' + sessionStorage.getItem("token")
                        }
                    }

                    axios.post('/portfolios/' + this.id + '/comment/', (requestHeader, {
                            content: this.comment,
                            user: Number(this.login_uid),
                            portfolio_id: this.portfolio.id,
                        }))
                        .then(res => {
                            console.log("댓글남기기 완료")
                            alert("댓글이 저장되었습니다.")
                            location.reload()
                            this.comment = ''
                        })
                        .catch(err => {
                            console.log("댓글남기기 실패")
                            console.log(err)
                            console.log(this.comment)
                            console.log("로그인유저" + typeof (this.login_uid))
                            console.log("포폴아이디" + typeof (this.portfolio.id))
                        })
                }
            },
            moveHistoryBack() {
                history.back()
            },
            moveDetailPage() {
                this.$router.push('/portup/' + this.id)
            }
        }
    }
</script>

<style scoped>
    .form_data {
        margin-left: 30px;
        margin-right: 30px;
        padding-top: 50px;
        padding-bottom: 20px;
    }

    .col {
        padding: 0px;
        margin: 0px;
    }

    .pad {
        padding-bottom: 20px;
        margin-bottom: 12px;
    }

    .col-md-7 offset-md-5 col {
        text-align: right;
    }
</style>