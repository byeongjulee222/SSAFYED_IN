<template>
    <v-card>
        <v-card-text class="grey lighten-4">
            <v-sheet max-width="800" class="mx-auto">
                <v-form>
                    <div class="form_data">
                        <!--제목-->
                        <div id="title">
                            <v-row class="cont-center">
                                <v-col cols="12" md="12">
                                <h2 class="headline"><img class="logo" :src="competitions.recruit_logo"/>{{competitions.title}}</h2>
                                </v-col>
                            <p style="text-align:right;">모집 기간 : {{competitions.created_at}} ~ {{competitions.end_date}}</p>
                            <v-divider></v-divider><br>
                            </v-row>
                        </div>

                        <div id="contents">
                            <!--대표 이미지 설정-->
                            <v-card>
                                <div>
                                    <img :src="competitions.recruit_logo" width="100%" height="350px"/>
                                </div>
                            </v-card>

                            <!--설명-->
                            <v-textarea outlined v-model="competitions.content" height="300" readonly></v-textarea>
                        </div>
                        <div class="cmp_tech">
                            <span>기술스택: </span>
                            <v-chip v-for="(tech_stacks,index) in competitions.tech_category" :key="index" class="ma-2" label color="primary">
                                <v-icon left>mdi-label</v-icon>
                                {{ tech_stacks.tech_stack }}
                            </v-chip>
                        </div>
                    </div>
                </v-form>
                
            </v-sheet>
        </v-card-text>
    </v-card>
</template>

<style scoped>
    .form_data {
        margin-left: 50px;
        margin-right: 50px;
        padding-top: 50px;
        padding-bottom: 150px;
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

<script>
    export default {
        name: 'CompetitionDetail',
        data() {
            return {
                competitions: [],
                id: Number(this.$route.params.id),
                login_uid: sessionStorage.getItem("uid"),
                flag: false,
            }
        },
        methods: {
            getCompetition() {
                axios.get('/competitions/'+this.$route.params.id)
                    .then(res => {
                        this.competitions = res.data
                        this.flag = this.login_uid == this.portfolio.user.id ? true : false
                    })
                    .catch(err => {
                        console.log(err)
                    })
            },
        },
        mounted() {
            this.getCompetition()
        }
    }
</script>