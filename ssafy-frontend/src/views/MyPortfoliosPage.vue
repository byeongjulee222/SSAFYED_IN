<template>
    <div class="profile">
        <Left :id="id" />
        <div class="profile_right">
            <div class="profile_wrap">
                <div class="text-end pt-5" v-if="id == login_uid"><v-btn outlined color="blue" @click="movePortUp">Upload</v-btn></div>
                <v-layout>
                    <v-flex xs12>
                        <div class="text-center">
                            <div class="pa-5">
                                <SSAFYPortfolioList :portfolios="portfolios" :locks="locks" :flag="true"></SSAFYPortfolioList>
                            </div>
                        </div>
                    </v-flex>
                </v-layout>
                <div style="margin:0 50px 0 50px !important">
                    <v-btn v-if="moreBtn" class="my-10" block color="grey" @click="moreLoad" outlined>
                        <v-icon>expand_more</v-icon>
                    </v-btn>
                </div>
                <v-card v-if="mypagePortfolios" outlined width="100%">
                    <v-card-text class="text-center">등록된 포트폴리오가 없습니다.</v-card-text>
                </v-card>
            </div>
        </div>
    </div>
</template>

<script>
    import SSAFYPortfolioList from '../components/SSAFYPortfolioList'
    import Left from '../components/profile/Left'
    export default {

        name: 'MyPortfoliosPage',
        data() {
            return {
                portfolios: [],
                copyPortfolios: [],
                mypagePortfolios: false,
                moreBtn: false,
                more: 6,
                id : Number(this.$route.params.id),
                locks : [],
                login_uid : sessionStorage.getItem("uid"),
            }
        },
        components: {
            SSAFYPortfolioList,
            Left,
        },
        methods: {
            moreLoad() {
                this.more += 6
                this.portfolios = this.copyPortfolios.slice(0, this.more)
                if (this.more > this.portfolios.length) this.moreBtn = false
            },
            movePortUp() {
                this.$router.push('/portup')
            }
        },
        created() {
            axios.get('/accouts/' + this.id + '/')
                .then(res => {
                    this.copyPortfolios = res.data.portfolio_set
                    this.portfolios = res.data.portfolio_set

                    for (let i = 0; i < this.portfolios.length; i++) {
                        this.locks.push(this.portfolios[i].public)
                    }

                    console.log(this.locks)

                    if (this.portfolios.length == 0) {
                        this.moreBtn = false
                        this.mypagePortfolios = true
                    } else if(this.portfolios.length < this.more) {
                        this.moreBtn = false
                    } else {
                        this.portfolios = this.portfolios.slice(0, 6)
                        this.moreBtn = true
                    }
                })
                .catch(err => {
                    console.log(err)
                    this.moreBtn = false
                })
        }
    }
</script>