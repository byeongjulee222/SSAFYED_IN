<template>
    <div>
        <div class="my-8" style="margin:0 50px 0 50px !important">
            <!--내가 쓴 글 보기에서 사용됨-->
            <div class="text-end mt-10">
                <v-btn color="primary" @click="sendEmail" v-if="flagBtn" style="text-transform:none;" large
                    class="title">
                    이메일 보내기</v-btn>
            </div>

            <v-row class="fill-height" align="center">
                <template v-for="(user, index) in users">
                    <v-col :key="index" cols="12" md="6" lg="6">
                        <v-hover v-slot:default="{ hover }">
                            <v-card :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }">
                                <div class="rank_div">
                                    <a :href="'/profile/' + user.id">
                                        <div class="rank_img hidden-xs-only">
                                            <img :src="getProfileImage(user.profile_img)">
                                            <!--hover-->
                                            <v-expand-transition>
                                                <div v-if="hover"
                                                    class="d-flex light-blue transition-fast-in-fast-out v-card--reveal display-2 white--text text-sm-center">
                                                    포트폴리오 보러가기
                                                </div>
                                            </v-expand-transition>
                                        </div>

                                        <div class="rank_title">
                                            <p class="rank_title title my-3 font-weight-bold">{{ user.nickname }}
                                            </p>
                                        </div>

                                        <div class="rank_cont">
                                            {{ user.introduce}}
                                        </div>

                                        <!--기술스택-->
                                        <div class="cmp_tech">
                                            <span style="font-weight:bold;">기술스택 :</span><br/>
                                            <v-chip v-for="(tech_stacks,index) in user.tech_category" :key="index" class="ma-2" label color="primary">
                                                <v-icon left>mdi-label</v-icon>
                                                {{ tech_stacks.tech_stack }}
                                            </v-chip>
                                        </div>
                                    </a>
                                </div>
                            </v-card>
                        </v-hover>

                        <div class="mt-3" v-if="flagBtn">
                            <v-checkbox class="title" :label="user.nickname" color="primary" :value="user.username"
                                v-model="checkBox">
                            </v-checkbox>
                        </div>
                    </v-col>
                </template>
            </v-row>
        </div>
    </div>
</template>

<script>
    import '../assets/css/rank/rank.css'
    import {
        eventBus
    } from '../main.js'
    import SearchBar from '../components/SearchBar'

    export default {
        name: 'SSAFYRank',
        data() {
            return {
                checkBox: [],
            }
        },
        components: {
            SearchBar,
        },
        props: {
            flagBtn: Boolean,
            users: Array,
        },
        methods: {
            getProfileImage(value) {
                if (value == null|| value =='')
                    return require('../assets/no_picture.png');
                else
                    return value;
            },
            sendEmail() {
                // this.$store.saveEmail = checkBox
                axios.post('/competitions/' + 1 + '/sendmail/', this.checkBox)
                    .then(res => {
                        console.log("지원자 이메일값 전달 성공")
                    })
                    .catch(err => {
                        console.log("지원자 이메일값 전달 실패")
                    })
                alert("이메일이 전송되었습니다!")
            },
        }
    }
</script>

<style>
    .v-label {
        margin-bottom: 0px;
    }
</style>