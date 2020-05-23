<template>
<div>
    <BoardBanner style="background-color:#ffc3a0;">
      <div style="line-height:1em; font-size:6vw; text-align:center; font-weight:bold; " slot="text">
        Competition</div>
      </BoardBanner>
    <div class="profile">
        <div class="profile_right">
            <div class="profile_wrap">
                <SSAFYRank :users="applicants.applicant_competition_user" :flagBtn="true"></SSAFYRank>
            </div>
        </div>
    </div>
</div>
</template>

<script>
    import Left from '../components/profile/Left'
    import SSAFYRank from '../components/SSAFYRank'
    import BoardBanner from '../components/BoardBanner'
    import {
        eventBus
    } from '../main'

    export default {
        name: 'CompetitionMembers',
        data() {
            return {
                applicants: [],
                sendEmailCheck: [],
                login_uid: sessionStorage.getItem("uid"),
                flag: false,
            }
        },
        components: {
            Left,
            SSAFYRank,
            BoardBanner
        },
        mounted() {
            axios.get('/competitions/'+this.$route.params.id)
                .then(res => {
                    this.applicants = res.data
                    console.log(this.applicants)
                })
                .catch(err => {
                    console.log("지원자 보기 에러" + err)
                })
        },
        // created() {

        // }
    }
</script>