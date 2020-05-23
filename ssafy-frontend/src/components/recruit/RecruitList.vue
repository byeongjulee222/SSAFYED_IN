<template>
    <v-container>
        <h3 class="font-weight-medium apply_title">수시채용</h3>
        <div style="border:2px solid #E0E0E0; border-radius:5px; padding:12px;position:relative">
            <div class="text-right margin-100">
                <v-btn class="ma-2" large outlined color="black" @click="Write()" v-if="flag">
                write
                </v-btn>
            </div>
            <v-simple-table>
                <template v-slot:default>
                    <tbody>
                        <template >
                        <tr v-for="(recruit, index) in recruits" :key="index" @click="Read(recruit)">
                            <td>{{recruits.length - index}}</td>
                            <td>{{recruit.population}}  |  {{ recruit.title }}</td>
                            <td>[ {{recruit.user_name.company}} ] {{recruit.user_name.nickname}}</td>
                            <td>|&nbsp;{{ recruit.end_date }} 마감</td>
                        </tr>
                        </template>
                    </tbody>
                </template>
            </v-simple-table>
        </div>
    </v-container>
</template>

<script>
    export default {
        name: 'RecruitList',
        data() {
            return {
                recruits: [],
                login_uid: sessionStorage.getItem("uid"),
                flag: false,
            }
        },
        methods: {
            getRecruit() {
                axios.get('/recruits/')
                    .then(res => {
                        this.recruits = res.data[0]
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
                    path:'/recruit_write'
                })
            },
            Read(values){
                console.log(values)
                this.$router.push({
                    path:'/recruits/'+values.id,
                })
            }
        },
        mounted() {
            this.getRecruit()
        }
    }
</script>