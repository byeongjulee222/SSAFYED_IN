<template>
  <div class="write_wrapper">
    <BoardBanner style="background-color:#ffc3a0;">
        <div style="line-height:1em; font-size:6vw; text-align:center; font-weight:bold; " slot="text">
            Competition</div>
    </BoardBanner>
    <div class="text-center">
        <v-form>
          <v-container>
            <v-row class="w-cont-center"> 
              <v-col cols="12" md="12">
                <v-text-field v-model="data.title" label="제목" required/>
              </v-col>
            </v-row>
            
            <v-row class="w-cont-center">
              <v-col cols="12" md="12">
                <template v-if="this.$route.params.id!==undefined">
                  <div>
                    <p class="b_f_">변경 전<v-btn class="mx-2 delete_image" @click="delete_before" fab dark x-small color="red">
                        <v-icon dark>mdi-minus</v-icon>
                      </v-btn></p>
                    <div class="before_img">
                      <img :src="before_img" class="bf_img"/>
                    </div>
                  </div>
                  <p class="b_f_">변경 후</p>
                </template>
                <FP v-on:load_img="getServerImag"/>
              </v-col>
            </v-row>
            
            <v-row class="w-cont-center">
              <v-col cols="12" md="6">
                <v-text-field v-model="data.region" :counter="10" label="지역" required/>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="data.population" :counter="10" label="모집인원" required/>
              </v-col>
            </v-row>
            
            <v-row class="w-cont-center">
              <v-col cols="12" md="6">
                  <v-text-field v-model="data.company_url" label="URL" required/>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-dialog ref="dialog" v-model="data.modal" :return-value.sync="data.end_date" persistent width="290px">
                  <template v-slot:activator="{ on }">
                    <v-text-field v-model="data.end_date" label="모집마감" prepend-icon="event" readonly v-on="on"/>
                  </template>
                  <v-date-picker v-model="data.end_date" scrollable>
                    <v-spacer></v-spacer>
                    <v-btn text color="primary" @click="data.modal = false">Cancel</v-btn>
                    <v-btn text color="primary" @click="$refs.dialog.save(data.end_date)">OK</v-btn>
                  </v-date-picker>
                </v-dialog>
              </v-col>
            </v-row>

            <v-row class="w-cont-center">
              <v-col cols="12" md="12">
                <v-container fluid>
                  <v-select v-model="data.tech_category" :items="skills" label="기술스택" chips color="primary" deletable-chips multiple>
                    <template v-slot:prepend-item>
                      <v-list-item ripple @click="toggle">
                        <v-list-item-action>
                          <v-icon :color="data.tech_category.length > 0 ? 'indigo darken-4' : ''">{{ icon }}</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                          <v-list-item-title>Select All</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                      <v-divider class="mt-2 hihi"></v-divider>
                    </template>

                    <template v-slot:append-item>
                      <v-divider class="mb-2"></v-divider>
                      <v-list-item disabled>
                        <v-list-item-avatar color="grey lighten-3">
                          <v-icon>mdi-wrench</v-icon>
                        </v-list-item-avatar>

                        <v-list-item-content v-if="likesAllSkill">
                          <v-list-item-title>모든 기술을 선택하셨습니다!!!</v-list-item-title>
                        </v-list-item-content>

                        <v-list-item-content v-else-if="likesSomeSkill">
                          <v-list-item-title>보유기술</v-list-item-title>
                          <v-list-item-subtitle>{{ data.tech_category.length }}개 선택하셨습니다.</v-list-item-subtitle>
                        </v-list-item-content>

                        <v-list-item-content v-else>
                          <v-list-item-title>어떤 기술들을 필요로 하십니까?</v-list-item-title>
                          <v-list-item-subtitle>위의 항목을 선택하십시오!</v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>
                    </template>
                  </v-select>
                </v-container>
              </v-col>
            </v-row>

            <v-row class="w-cont-center">
              <v-col cols="12" md="12">
                <mdb-input type="textarea" v-model="data.qualitification" label="우대사항" :rows="5" :state="data.qualitification.length >= 10"/>
              </v-col>
            </v-row>

            <v-row class="w-cont-center">
              <v-col cols="12" md="12">
                <mdb-input type="textarea" v-model="data.content" label="모집내용" :rows="5" :state="data.content.length >= 10"/>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
    </div>

    <div class="text-center">
        <v-btn class="ma-2" tile outlined color="success" @click="post_id !== undefined ? Update() : Write()">
            <v-icon left>mdi-pencil</v-icon>{{post_id !== undefined ? 'Edit': 'Write'}}
        </v-btn>
        <v-btn class="ma-2" tile outlined color="orange" @click="goToList">
          <v-icon left>list</v-icon> list
        </v-btn>
    </div>
  </div>
</template>

<script>
import { mdbInput } from 'mdbvue';
import FP from "../ImageUpload";
import router from '../../router';
import BoardBanner from '../BoardBanner'
export default({
  name: 'CompetitionWrite',
  data() {
      const user_name =  sessionStorage.getItem("uid")
      const post_id = this.$route.params.id
    return{
        data : {
          user_name: '',
          title: '',
          tech_category: [],
          end_date: new Date().toISOString().substr(0, 10),
          region: '',
          qualitification: '',
          content: '',
          population: '',
          company_url: '',
          recruit_logo: '',
          modal: false,
        },
        skills: ['Java', 'C', 'C++', 'Python', 'AI', 'IoT', '자율주행', '빅데이터', 'Django', 'Vue', 'JavaScript'],
        images:[],
        post_id:post_id,
        user_name:user_name,
        updateObject: null,
        before_img: '',
        login_uid: sessionStorage.getItem("uid"),
        flag: false,
    }
  },
  methods:{
    delete_before(){
      this.before_img=''
      this.data.before_img=''
      console.log(this.data.before_img)
    },
    getServerImag(serverid){
      this.data.recruit_logo=serverid
      console.log(this.data)
    },
    Write() {
      let fr = new FormData();
      console.log(fr)

      //form에선 용어, 백으로 보낼땐 숫자로
       var result = []
        for (let i = 0; i< this.data.tech_category.length; i++) {
          for (let j = 0; j < this.skills.length; j++) {
            if(this.skills[j] == this.data.tech_category[i]) {
              console.log('here'+(j+1))
              result.push(j+1)
              break
            }
          }
        }

      console.log(result)
      console.log('user_name:'+this.user_name)
          axios.post('/competitions/create/',{
              user_name: this.user_name,
              title: this.data.title,
              tech_category: this.data.tech_category,
              end_date: this.data.end_date,
              region: this.data.region,
              qualitification: this.data.qualitification,
              content: this.data.content,
              population: this.data.population,
              company_url: this.data.company_url,
              recruit_logo: this.data.recruit_logo
          })
          .then(res => {
            console.log(res)
              this.$router.push({
                path:'/competition/'
              })
            })
        .catch(err => {
            console.log(err)
          //console.log(tech_category)
        })
      },
    Update() {
        let fr = new FormData();
      console.log(fr)

      //form에선 용어, 백으로 보낼땐 숫자로
       var result = []
        for (let i = 0; i< this.data.tech_category.length; i++) {
          for (let j = 0; j < this.skills.length; j++) {
            if(this.skills[j] == this.data.tech_category[i]) {
              result.push(j+1)
              break
            }
          }
        }
          axios.put('/competitions/'+this.post_id+'/update/',{
              user_name: this.data.user_name,
              title: this.data.title,
              tech_category: this.data.tech_category,
              end_date: this.data.end_date,
              region: this.data.region,
              qualitification: this.data.qualitification,
              content: this.data.content,
              population: this.data.population,
              company_url: this.data.company_url,
              recruit_logo: this.data.recruit_logo
          })
          .then(res => {
            console.log(res)
            this.$router.push({
              path:'/competition/'+this.post_id
            })
            })
        .catch(err => {
            console.log(err)
            alert("error")
            // this.$router.push({
            //   path:'/competition/'+this.post_id
            // })
          //console.log(tech_category)
        })
    },
    toggle () {
      this.$nextTick(() => {
        if (this.likesAllSkill) {
          this.data.tech_category = []
        } else {
          this.data.tech_category = this.skills.slice()
        }
      })
    },
    goToList() {
      this.$router.push('/competition')
    },
    getCompetition() {
                axios.get('/competitions/'+this.$route.params.id)
                    .then(res => {
                        this.data.user_name=res.data.user_name.id
                        this.data.title = res.data.title
                        this.data.end_date=res.data.end_date
                        this.data.region = res.data.region
                        this.data.qualitification= res.data.qualitification
                        this.data.content=res.data.content
                        this.data.population=res.data.population
                        this.data.company_url=res.data.company_url
                        this.data.recruit_logo=res.data.recruit_logo
                        this.before_img = res.data.recruit_logo
                        this.data.modal=res.data.modal
                        for(var tech_list in res.data.tech_category){
                          this.data.tech_category.push(res.data.tech_category[tech_list].tech_stack)
                        }
                        if(res.data.user_name.id == this.login_uid){
                          this.flag = true;
                        }else{
                          alert("잘못된 접근입니다.")
                          this.$router.go(-1)
                        }
                        console.log(res.data)
                    })
                    .catch(err => {
                        console.log(err)
                    })
            },
  },
  components:{
    mdbInput,
    FP,
    BoardBanner
  },
  computed: {
    
    likesAllSkill () {
      return this.data.tech_category.length === this.skills.length
    },
    likesSomeSkill () {
      return this.data.tech_category.length > 0 && !this.likesAllSkill
    },
    icon () {
      if (this.likesAllSkill) return 'mdi-close-box'
      if (this.likesSomeSkill) return 'mdi-minus-box'
      return 'mdi-checkbox-blank-outline'
    },
  },
  mounted() {
            if(this.$route.params.id!==undefined) this.getCompetition()
        }
})

</script>