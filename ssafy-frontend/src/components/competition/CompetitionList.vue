<template>
    <v-container>
        <h3 class="font-weight-medium apply_title">공모전 모집</h3>
        <div style="border:2px solid #E0E0E0; border-radius:5px; padding:12px;position:relative">            
            <div class="text-right margin-100">
                <v-btn class="ma-2" large outlined color="black" @click="Write()" v-if="flag">
                write
                </v-btn>
            </div>
            <div v-for="(competition, index) in competitions" :key="index" class="competition_div" @click="Read(competition)">
                <div class="cmp_img">
                <img :src="competition.recruit_logo">
                </div>
                <div class="cmp_title">
                <p class="p_title">{{ competition.title }}</p>
                </div>
                <div class="cmp_writter">
                <p><span>모집인원 : </span>{{ competition.population}}</p>
                <p><span>마감일 : </span>{{ competition.end_date }}</p>
                </div>
                <div class="cmp_cont">
                {{competition.content}}
                </div>
                <div class="cmp_tech">
                    <span style="font-weight:bold;">기술스택 :</span><br/>
                    <v-chip v-for="(tech_stacks,index) in competition.tech_category" :key="index" class="ma-2" label color="primary">
                        <v-icon left>mdi-label</v-icon>
                        {{ tech_stacks.tech_stack }}
                    </v-chip>
                </div>
            <!-- </a> -->
            </div>
        </div>
    </v-container>
</template>

<script>
import '../../assets/css/competition/competition.css'
    export default {
        name: 'CompetitionList',
        data() {
            return {
                competitions: [],
                login_uid: sessionStorage.getItem("uid"),
                flag: false,
            }
        },
        methods: {
            getCompetition() {
                axios.get('/competitions/')
                    .then(res => {
                        console.log(res.data)
                        this.competitions = res.data[0]
                        if(this.login_uid==null||this.login_uid==''){
                            this.flag=false
                        }else{
                            this.flag=true
                        }
                    })
                    .catch(err => {
                        console.log(err)
                    })
            },
            Write(){
                this.$router.push({
                    path:'/competition_write'
                })
            },
            Read(values){
                console.log(values)
                this.$router.push({
                    path:'/competition/'+values.id,
                })
            }
        },
        mounted() {
            this.getCompetition()
        }
    }
</script>