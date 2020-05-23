<template>
    <div class="profile">
        <Left :id="id" />
        <div class="profile_right">
            <div class="profile_wrap">
                <v-layout>
                    <v-flex xs12>
                        <div class="text-center">
                            <div class="pa-5">
                                <h5 class="text-left">Competition</h5>
                                 <v-simple-table>
                                    <template v-slot:default>
                                        <thead>
                                            <tr>
                                                <td class="my_td">번호</td>
                                                <td class="my_td">제목</td>
                                                <td class="my_td">마감일</td>
                                                <td class="my_td">지원자</td>
                                            </tr>
                                        </thead>
                                        <tbody>                                         
                                            <tr v-for="(competition, index) in competitions" :key="index" @click="Read('/competition/'+competition.id)">
                                                <td class="my_td">{{competitions.length - index}}</td>
                                                <td class="my_td tit">{{ competition.title }}</td>
                                                <td class="my_td">{{competition.end_date}}</td>
                                                <td class="my_td">{{competition.applicant_competition_user.length}}</td>
                                            </tr>
                                        </tbody>
                                    </template>
                                </v-simple-table>
                            </div>
                        </div>
                    </v-flex>
                </v-layout>
                <div style="margin:0 50px 0 50px !important">
                    <v-btn v-if="moreBtn_comp" class="my-10" block color="grey" @click="moreLoad('competition')" outlined>
                        <v-icon>expand_more</v-icon>
                    </v-btn>
                </div>
                <v-card v-if="myPosts_competition" outlined width="100%">
                    <v-card-text class="text-center">등록된 Competition이 없습니다.</v-card-text>
                </v-card>
                <v-layout>
                    <v-flex xs12>
                        <div class="text-center">
                            <div class="pa-5">
                                <h5 class="text-left">Recruits</h5>
                                 <v-simple-table>
                                    <template v-slot:default>
                                        <thead>
                                            <tr>
                                                <td class="my_td">번호</td>
                                                <td class="my_td">제목</td>
                                                <td class="my_td">마감일</td>
                                                <td class="my_td">지원자</td>
                                            </tr>
                                        </thead>
                                        <tbody>                                         
                                            <tr v-for="(recruit, index) in recruits" :key="index" @click="Read('/recruits/'+recruit.id)">
                                                <td class="my_td">{{recruits.length - index}}</td>
                                                <td class="my_td tit">{{ recruit.title }}</td>
                                                <td class="my_td">{{ recruit.end_date }}</td>
                                                <td class="my_td">{{recruit.applicant_user.length}}</td>
                                            </tr>
                                        </tbody>
                                    </template>
                                </v-simple-table>
                            </div>
                        </div>
                    </v-flex>
                </v-layout>
                <div style="margin:0 50px 0 50px !important">
                    <v-btn v-if="moreBtn_recruit" class="my-10" block color="grey" @click="moreLoad('recruit')" outlined>
                        <v-icon>expand_more</v-icon>
                    </v-btn>
                </div>
                <v-card v-if="myPosts_recruit" outlined width="100%">
                    <v-card-text class="text-center">등록된 Recruit이 없습니다.</v-card-text>
                </v-card>
            </div>
        </div>
    </div>
</template>

<style scope>
.v-data-table .my_td{
    padding:0;
    font-size: 0.8vw;
}
.v-data-table .tit{
    padding:0 10px;
}
@media screen and (max-width: 768px){
    .profile_wrap {
        margin: 0 10px 10px;
    }
}
</style>
<script>
    import CompetitionList from '../components/competition/CompetitionList'
    import Left from '../components/profile/Left'
    export default {

        name: 'MyPortfoliosPage',
        data() {
            return {
                competitions: [],
                c_competitions: [],
                recruits: [],
                c_recruits: [],
                
                myPosts_competition:false,
                myPosts_recruit:false,
                
                moreBtn_comp: false,
                moreBtn_recruit: false,
                
                more_com:5,
                more_re:5,
                id : Number(this.$route.params.id),
                locks : [],
                login_uid : sessionStorage.getItem("uid"),
            }
        },
        components: {
            CompetitionList,
            Left,
        },
        methods: {
            moreLoad(value) {
                if(value=='competition'){
                    this.more_com += 5
                    this.competitions = this.c_competitions.slice(0, this.more_com)
                    if (this.more_com > this.competitions.length) this.moreBtn_comp = false
                }else if(value=='recruit'){
                    this.more_re += 5
                    this.recruits = this.c_recruits.slice(0, this.more_re)
                    if (this.more_re > this.recruits.length) this.moreBtn_recruit = false
                }else{
w
                }


            },
            Read(value){
                console.log(value)
                this.$router.push(value)
            }
        },
        created() {
            axios.get('/accouts/' + this.id + '/')
                .then(res => {
                    this.competitions = res.data.competition
                    this.c_competitions = res.data.competition
                    this.recruits = res.data.recruit
                    this.c_recruits = res.data.recruit

                    if (this.competitions.length == 0) {
                        this.moreBtn_comp = false
                        this.myPosts_competition = true
                    } else if(this.competitions.length < this.more_com) {
                        this.moreBtn_comp = false
                    } else {
                        this.competitions = this.competitions.slice(0, 5)
                        this.moreBtn_comp = true
                    }

                    if (this.recruits.length == 0) {
                        this.moreBtn_recruit = false
                        this.myPosts_recruit = true
                    } else if(this.recruits.length < this.more_re) {
                        this.moreBtn_recruit = false
                    } else {
                        this.recruits = this.recruits.slice(0, 5)
                        this.moreBtn_recruit = true
                    }
                })
                .catch(err => {
                    console.log(err)
                    this.moreBtn_comp = false
                    this.moreBtn_recruit = false
                })
        }
    }
</script>