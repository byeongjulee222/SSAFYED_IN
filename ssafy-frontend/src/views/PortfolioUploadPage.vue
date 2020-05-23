<template>
  <v-card>
    <v-card-text class="grey lighten-4">
      <v-sheet max-width="800" class="mx-auto">
        <div class="form_data">
          <!--제목-->
          <v-col cols="12" class="pad">
            <v-text-field v-model="title" required prepend-icon="title">
            </v-text-field>
          </v-col>

          <!--카테고리-->
          <v-col cols="12" class="pad">
            <v-autocomplete :items="items" v-model="tech_category" label="Category" multiple small-chips outlined
              :rules="limits">
            </v-autocomplete>
            <v-divider class="mt-0 pt-0"></v-divider>
          </v-col>

          <!--대표 이미지 설정-->
          <v-col cols="12">
            <v-card-title class="px-0 pt-0">대표 이미지</v-card-title>
            <div v-if="loadImages[0]">
              <v-card-subtitle class="ma-0 pa-0">Before</v-card-subtitle>
              <v-card outlined class="mb-1"><img :src="loadImages[0]" width="100%" height="350px" /></v-card>
              <v-card-subtitle class="ma-0 pa-0">After</v-card-subtitle>
            </div>
            <v-card outlined @change="idx=0" class="pt-4 px-4">
              <FP v-on:load_img="getServerImag"></FP>
            </v-card>
          </v-col>
          <br>
          <!--설명-->
          <v-col cols="12">
            <v-textarea outlined label="포트폴리오에 대한 설명을 적어주세요." v-model="contents[0]" height="200">
            </v-textarea>
          </v-col>

          <!--달력-->
          <v-col offset="5" style="text-align:right;" class="pad">
            <v-card class="d-inline-flex pa-2" outlined tile cols="auto">
              <v-menu ref="startMenu" v-model="startMenu" :close-on-content-click="false" :nudge-right="40"
                :return-value.sync="start" transition="scale-transition" min-width="290px" offset-y>
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="start" label="Start Date" prepend-icon="event" dense readonly outlined
                    hide-details v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="start" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="startMenu = false">
                    Cancel
                  </v-btn>
                  <v-btn text color="primary" @click="$refs.startMenu.save(start)">
                    OK
                  </v-btn>
                </v-date-picker>
              </v-menu>
              <v-icon>remove</v-icon>
              <v-menu ref="endMenu" v-model="endMenu" :close-on-content-click="false" :nudge-right="40"
                :return-value.sync="end" transition="scale-transition" min-width="290px" offset-y>
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="end" label="End Date" dense readonly outlined hide-details v-on="on">
                  </v-text-field>
                </template>
                <v-date-picker v-model="end" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="endMenu = false">
                    Cancel
                  </v-btn>
                  <v-btn text color="primary" @click="$refs.endMenu.save(end)">
                    OK
                  </v-btn>
                </v-date-picker>
              </v-menu>
            </v-card>
          </v-col>

          <!-- 포트폴리오 이미지 stepper -->
          <div>
            <v-card-title class="px-0">프로젝트 디테일 컷</v-card-title>
            <v-card-subtitle class="px-0">Steps를 이용해 등록할 디테일 갯수를 조절해주세요</v-card-subtitle>
            <v-row justify="space-around">
              <v-col cols="12">
                <v-slider v-model="steps" label="Steps" min="2" max="4"></v-slider>
              </v-col>
            </v-row>
            <v-stepper v-model="e1" :vertical="vertical" :alt-labels="altLabels">

              <template>
                <v-stepper-header>
                  <template v-for="n in steps">
                    <v-stepper-step :key="`${n}-step`" :complete="e1 > n" :step="n" :editable="editable">

                    </v-stepper-step>

                    <v-divider v-if="n !== steps" :key="n"></v-divider>
                  </template>
                </v-stepper-header>

                <v-stepper-items>
                  <v-stepper-content v-for="n in steps" :key="`${n}-content`" :step="n">
                    <div v-if="loadImages[n]">
                      <v-card-subtitle class="ma-0 pa-0">Before</v-card-subtitle>
                      <v-card outlined class="mb-1"><img :src="loadImages[n]" width="100%" height="350px" /></v-card>
                      <v-card-subtitle class="ma-0 pa-0">After</v-card-subtitle>
                    </div>
                    <v-card @change="idx=n" outlined class="pt-4 px-4 mb-5">
                      <FP v-on:load_img="getServerImag" />
                    </v-card>

                    <v-col cols="12">
                      <v-text-field outlined label="프로젝트 세부 설명을 적어주세요" v-model="contents[n]" counter="70">
                      </v-text-field>
                    </v-col>

                    <div style="float:left;">
                      <v-btn v-if="n!==1" color="grey lighten-2" @click="nextStep(n-2)">Prev</v-btn>
                    </div>

                    <div>
                      <v-btn v-if="n!==steps" color="primary" @click="nextStep(n)" class="ml-2">Next
                      </v-btn>
                    </div>
                  </v-stepper-content>
                </v-stepper-items>

              </template>
            </v-stepper>
          </div>
        </div>
        <div class="text-end pa-10">
          <v-checkbox v-model="check_public" label="Public" color="blue" hint="동의하시면 외부에 포트폴리오가 공개됩니다." persistent-hint>
          </v-checkbox>
          <v-btn v-if="flag" outlined color="#757575" large @click="deletePortfolio">Delete</v-btn>
          <v-btn outlined color="primary" class="ml-2" large @click="postPortfolioUpload">Save</v-btn>
          <v-btn outlined color="orange" class="ml-2" large @click="movePageList">list</v-btn>
        </div>
      </v-sheet>
    </v-card-text>
  </v-card>

</template>

<style scoped>
  .form_data {
    margin-left: 50px;
    margin-right: 50px;
    padding-top: 50px;
    padding-bottom: 10px;
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

  .filepond--drop-label {
    max-height: 100em;
  }
</style>

<script>
  import FP from "../components/ImageUpload";
  import '../assets/css/portfolio/upload.css'

  export default {
    data() {
      return {
        e1: 1,
        steps: 2,
        vertical: false,
        altLabels: false,
        editable: true,
        title: '',
        tech_category: [],
        startMenu: false,
        start: '2019-01-01',
        endMenu: false,
        end: '2019-01-01',
        items: ['Java', 'C', 'C++', 'Python', 'AI', 'IoT', '자율주행', '빅데이터', 'Django', 'Vue', 'JavaScript'],
        limits: [v => (v.length <= 5) || '최대 5개까지 선택 가능합니다.'],
        contentImgaeRules: [
          v => !!v || '대표 이미지를 첨부해주세요.',
        ],
        contents: [],
        check_public: false,
        flag: false, //수정이면 delete버튼 노출
        images: [],
        idx: 0, //현재 이미지 step
        loadImages: [],
      }
    },
    methods: {
      getServerImag(serverid) {
        console.log(serverid)
        this.images[this.idx] = serverid
      },
      onInput(val) {
        this.steps = parseInt(val)
        console.log(this.steps)
      },
      nextStep(n) {
        if (n === this.steps) {
          this.e1 = 1
        } else {
          this.e1 = n + 1
        }
      },
      postPortfolioUpload() {
        var result = []
        for (let i = 0; i < this.tech_category.length; i++) {
          for (let j = 0; j < this.items.length; j++) {
            if (this.tech_category[i] == this.items[j])
              result.push(j + 1)
          }
        }

        if (this.$route.params.id) {
          axios.put('/portfolios/' + this.$route.params.id + '/delete_update/', {
              user: sessionStorage.getItem("uid"),
              title: this.title,
              tech_category: result,
              project_start: this.start,
              project_end: this.end,
              contents: this.contents,
              images: this.images,
              public: this.check_public,
            })
            .then(res => {
              console.log("포폴 수정 성공")
              alert('수정되었습니다!')
              this.$router.push('/myportfolios/' + sessionStorage.getItem("uid"))
            })
            .catch(err => {
              console.log("포폴 수정 실패")
            })
        } else {
            axios.post('/portfolios/create/', {
                user: sessionStorage.getItem("uid"),
                title: this.title,
                tech_category: result,
                project_start: this.start,
                project_end: this.end,
                contents: this.contents,
                images: this.images,
                public: this.check_public,
              })
              .then(res => {
                console.log("포폴 업 성공")
                alert('등록되었습니다!')
                this.$router.push('/myportfolios/' + sessionStorage.getItem("uid"))
              })
              .catch(err => {
                console.log("포폴 업 실패")
              })
          // }
        }
      },
      movePageList() {
        this.$router.push('/myportfolios/' + sessionStorage.getItem("uid"))
      },
      deletePortfolio() {
        if (confirm("정말 삭제하시겠습니까?"))
          axios.delete('/portfolios/' + this.$route.params.id + '/delete_update/')
          .then(res => {
            console.log("삭제 완료")
            alert("삭제되었습니다!")
            this.$router.go(-1)
          })
          .catch(err => {
            console.log("삭제 실패")
          })
      },
    },
    computed: {
      hasEnd() {
        return this.type in {
          'custom-weekly': 1,
          'custom-daily': 1,
        }
      }
    },
    components: {
      FP,
    },
    created() {
      if (this.$route.params.id) {
        axios.get('/portfolios/' + this.$route.params.id)
          .then(res => {
            console.log("Edit Data 가져옴")
            console.log(res.data)
            this.title = res.data.title
            for (let i = 0; i < res.data.tech_category.length; i++) {
              this.tech_category.push(res.data.tech_category[i].tech_stack)
            }

            if (res.data.content_sub_1) this.contents.push(res.data.content_sub_1)
            if (res.data.content_sub_2) this.contents.push(res.data.content_sub_2)
            if (res.data.content_sub_3) this.contents.push(res.data.content_sub_3)
            if (res.data.content_sub_4) this.contents.push(res.data.content_sub_4)
            if (res.data.content_sub_5) this.contents.push(res.data.content_sub_5)

            if (res.data.content_img_1) this.loadImages.push(res.data.content_img_1)
            if (res.data.content_img_2) this.loadImages.push(res.data.content_img_2)
            if (res.data.content_img_3) this.loadImages.push(res.data.content_img_3)
            if (res.data.content_img_4) this.loadImages.push(res.data.content_img_4)
            if (res.data.content_img_5) this.loadImages.push(res.data.content_img_5)

            this.steps = this.loadImages.length - 1

            this.start = res.data.project_start
            this.end = res.data.project_end
            this.check_public = res.data.public
            this.flag = true
          })
      }
    }
  }
</script>