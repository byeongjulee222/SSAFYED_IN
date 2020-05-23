<template>
    <div>
        <BoardBanner style="background-color:#ffc107;">
            <div style="line-height:1em; font-size:6vw; text-align:center; font-weight:bold; " slot="text">
                SSAFY Rank</div>
        </BoardBanner>
        <SearchBar v-on:create_search="getText"></SearchBar>
        <SSAFYRank :users="users"></SSAFYRank>
        <div style="margin:0 50px 0 50px !important">
            <v-btn v-if="moreBtn" class="my-10" block color="grey" @click="moreLoad" outlined>
                <v-icon>expand_more</v-icon>
            </v-btn>
        </div>
        <ScrollToTop class="hidden-xs-only"></ScrollToTop>
    </div>
</template>


<script>
    import BoardBanner from '../components/BoardBanner'
    import SearchBar from '../components/SearchBar'
    import SSAFYRank from '../components/SSAFYRank'
    import ScrollToTop from '../components/ScrollToTop'

    export default {
        name: 'SSAFYRankPage',
        data() {
            return {
                users: [],
                copyUsers: [],
                moreBtn: false,
                more: 8,
                search_text: '',
            }
        },
        components: {
            BoardBanner,
            SearchBar,
            SSAFYRank,
            ScrollToTop,
        },
        methods: {
            getText(text) {
                this.search_text = text
                console.log("SSAFYRank 검색 내용은:" + this.search_text)
                axios.post('/accouts/user_page/', {
                        search_text: text
                    })
                    .then(res => {
                        if (res.data.length == 0) {
                            alert('검색 결과가 없습니다.')
                        } else {
                            this.copyUsers = res.data
                            this.users = res.data

                            if (this.users.length > 8) {
                                this.moreBtn = true
                                this.users = this.users.slice(0, 8)
                            } else {
                                this.moreBtn = false
                            }
                        }
                    })
                    .catch(err => {
                        console.log("SSAFYRank 사용자 정보 못불러옴")
                        console.log(err)
                    })
            },
            moreLoad() {
                this.more += 8
                this.users = this.copyUsers
                if (this.users.length > this.more) {
                    this.moreBtn = true
                    this.users = this.users.slice(0, this.more)
                } else {
                    this.moreBtn = false
                }
            },
        }
    }
</script>