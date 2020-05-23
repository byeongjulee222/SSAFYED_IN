<template>
    <div>
        <BoardBanner style="background-color:#ffc3a0;">
        <div style="line-height:1em; font-size:6vw; text-align:center; font-weight:bold; " slot="text">
            Competition</div>
        </BoardBanner>
        <v-card>
            <v-card-text class="grey lighten-4">
                <v-sheet max-width="1100" class="mx-auto">
                        
                            <!--제목-->
                            <div id="title">
                                <v-row class="cont-center"> 
                                    <v-col cols="12" md="12">
                                        <h2 class="headline text-center">{{competitions.title}}</h2>
                                    </v-col>
                                </v-row>
                                <p style="text-align:right;">모집 기간 : {{competitions.created_at}} ~ {{competitions.end_date}}</p>
                                <v-divider></v-divider><br>
                            </div>

                            <div id="contents" style="padding:0 20px">
                                <!--대표 이미지 설정-->
                                <template v-if="competitions.recruit_logo != '' && competitions.recruit_logo != null">
                                    <v-card class="upload_image pad" style="width:80%;text-align:center; margin:0 auto;">
                                        <div class="image-preview">
                                            <img class="preview" :src="competitions.recruit_logo" width="100%"/>
                                        </div>
                                    </v-card>
                                </template>
                                <v-row class="cont-center" style="margin:20px 0;">
                                    <v-col cols="12" md="4">
                                        <h5> | 지역    :    {{competitions.region}}</h5>
                                    </v-col>
                                    <v-col cols="12" md="4">
                                        <h5> | 모집인원    :    {{competitions.population}}</h5>
                                    </v-col>
                                    <v-col cols="12" md="4">
                                        <h5> | URL : <a :href="competitions.company_url">클릭 시 해당 사이트로 이동</a></h5> 
                                    </v-col>
                                </v-row>
                                <!--설명-->
                                <h5> | 우대사항</h5>
                                <v-textarea outlined v-model="competitions.qualitification" height="300" readonly></v-textarea>
                                <h5> | 모집내용</h5>
                                <v-textarea outlined v-model="competitions.content" height="300" readonly></v-textarea>
                            </div>
                            <div class="cmp_tech">
                                <span> | 기술스택 : </span>
                                <v-chip v-for="(tech_stacks,index) in competitions.tech_category" :key="index" class="ma-2" label color="primary">
                                    <v-icon left>mdi-label</v-icon>
                                    {{ tech_stacks.tech_stack }}
                                </v-chip>
                            </div>
            <div class="text-center">
                    <v-btn class="ma-2" tile outlined color="red" @click="Delete()" v-if="flag == true && (login_uid != ''&& login_uid != null)">
                    <v-icon left>mdi-cancel</v-icon> Delete
                    </v-btn>

                    <v-btn class="ma-2" tile outlined color="success" @click="Update()" v-if="flag">
                    <v-icon left>mdi-pencil</v-icon> Edit
                    </v-btn>
                    
                    <v-btn class="ma-2" tile outlined color="success" @click="Apply()" v-if="flag == false && (login_uid != ''&& login_uid != null)">
                    <v-icon left>mdi-pencil</v-icon> Apply
                    </v-btn>

                    <v-btn class="ma-2" tile outlined color="blue" @click="goToApplyList" v-if="flag == true && (login_uid != ''&& login_uid != null)">
                    <v-icon left>list</v-icon> Apply list
                    </v-btn>

                    <v-btn class="ma-2" tile outlined color="orange" @click="goToList">
                    <v-icon left>list</v-icon> list
                    </v-btn>
                    
                </div>
                      
                </v-sheet>
            </v-card-text>
        </v-card>
    </div>
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

    .file-upload .fileName {
        display: inline-block;
        width: 400px;
        height: 30px;
        padding-left: 10px;
        margin-right: 5px;
        line-height: 30px;
        border: 1px solid #aaa;
        background-color: #fff;
        vertical-align: middle
    }

    .file-upload .btn_file {
        display: inline-block;
        border: 1px solid #000;
        border-radius: 40px / 40px;
        width: 100px;
        height: 30px;
        font-size: 0.8em;
        line-height: 30px;
        text-align: center;
        vertical-align: middle
    }

    .file-upload input[type="file"] {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        border: 0
    }

    .upload_image {
        width: 100%;
    }
</style>

<script>
    import BoardBanner from '../components/BoardBanner'
    export default {
        name: 'CompetitionList',
        data() {
            return {
                competitions: '',
                id: Number(this.$route.params.id),
                login_uid: sessionStorage.getItem("uid"),
                flag: false,
            }
        },
        methods: {
            Delete(){
                var check_del = confirm("해당 게시글을 삭제 하시겠습니까?")
                if(check_del){
                axios.delete('/competitions/'+this.$route.params.id+'/update/')
                    .then(res => {
                        alert("해당 게시글이 삭제되었습니다.")
                        location.href = '/competition'
                    })
                    .catch(err => {
                        alert("삭제를 하지 못했습니다. 다시 시도해주세요")
                    })
                }else{
                    alert("해당 게시글을 삭제하지 않았습니다.")
                }
            },
            getCompetition() {
                axios.get('/competitions/'+this.$route.params.id)
                    .then(res => {
                        this.competitions = res.data
                        this.flag = this.login_uid == this.competitions.user_name.id ? true : false
                        console.log(this.competitions)
                    })
                    .catch(err => {
                        console.log(err)
                    })
            },
            Update(){
                this.$router.push({
                    name: 'CompetitionWrite',
                    params: {'id' : this.$route.params.id}
                })
            },
            goToList() {
                this.$router.push('/competition')
            },
            Apply(){
                axios.post('/competitions/'+this.$route.params.id+'/applicant/',{
                        user : sessionStorage.getItem("uid")
                    })
                    .then(res => {
                        console.log(res)
                        alert("지원되었습니다.")
                        })
                    .catch(err => {
                        console.log(err)
                    //console.log(tech_category)
                    })
            },
            goToApplyList(){
                this.$router.push('/compmembers/'+this.$route.params.id)
            }
        },
        mounted() {
            this.getCompetition()
        },
        components: {
        BoardBanner
         }
    }
</script>