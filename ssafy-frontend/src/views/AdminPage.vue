<template>
  <div class="pa-5">
    <div class="text-end pa-5">
      <v-btn outlined large color="primary" @click="postAuth" class="title font-weight-bold">변경사항 저장</v-btn>
    </div>
    <v-row>

      <v-col cols="12" md="6">
        <v-card class="blue lighten-5">
          <v-card-title>
            <span class="blue--text">SSAFY</span><span>사용자</span>
          </v-card-title>

          <v-card-text>
            <v-sheet id="scrolling-techniques" class="overflow-y-auto" max-height="700">
              <div>
                <v-expansion-panels accordion>
                  <v-expansion-panel v-for="(ssafy, index) in ssafy_users" :key="index">
                    <v-expansion-panel-header>
                      <p class=" ma-0 pa-0">
                        <v-row>
                          <v-col cols="4">
                            {{ ssafy.nickname }}<span class="caption pl-2">{{ ssafy.username }}</span>
                          </v-col>
                          <v-col cols="4"><span class="caption pl-2">기수 : {{ ssafy.grade }}</span>
                          </v-col>
                           <v-col cols="4"><span class="caption pl-2">auth유/무 : {{ ssafy.auth }}</span>
                          </v-col>
                        </v-row>
                      </p>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <a :href="ssafy.verified_img" target="blank">
                        <img :src="ssafy.verified_img" height="300px" width="450px" />
                        </a>
                      <v-switch v-model="auth_ssafy[index]" label="Confirm"></v-switch>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </div>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>


      <v-col cols="12" md="6">
        <v-card class="pink lighten-5">
          <v-card-title>
            <span class="pink--text">기업</span><span>사용자</span>
          </v-card-title>

          <v-card-text>
            <v-sheet id="scrolling-techniques" class="overflow-y-auto" max-height="700">
              <div>
                <v-expansion-panels accordion>
                  <v-expansion-panel v-for="(recruit, index) in recruit_users" :key="index">
                    <v-expansion-panel-header>
                      <p class=" ma-0 pa-0">
                        <v-row>
                          <v-col cols="4">
                            {{ recruit.nickname }}<span class="caption pl-2">{{ recruit.username }}</span>
                          </v-col>
                          <v-col cols="4"><span class="caption pl-2">기수 : {{ recruit.grade }}</span>
                          </v-col>
                          <v-col cols="4"><span class="caption pl-2">auth유/무 : {{ recruit.auth }}</span>
                          </v-col>
                        </v-row>
                      </p>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <a :href="recruit.verified_img" target="blank">
                        <img :src="recruit.verified_img" height="300px" width="450px" />
                      </a>
                      <v-switch v-model="auth_recruit[index]" label="Confirm"></v-switch>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </div>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        ssafy_users: [],
        recruit_users: [],
        auth_ssafy: [],
        auth_recruit: [],
      }
    },
    created() {
      axios.get('/accouts/')
        .then(res => {
          for (let i = 0; i < res.data.length; i++) {
            if (res.data[i].grade != 0) {
              this.ssafy_users.push(res.data[i])
              if (res.data[i].auth != null)
                this.auth_ssafy.push(true)
              else
                this.auth_ssafy.push(false)
            } else {
              this.recruit_users.push(res.data[i])
              if (res.data[i].auth != null)
                this.auth_recruit.push(true)
              else
                this.auth_recruit.push(false)
            }
          }
          console.log("사용자들 불러옴")
          console.log(this.ssafy_users)
        })
        .catch(err => {
          console.log(err)
        })
    },
    methods: {
      postAuth() {
        var id = 0
        var sendAuth_ssafy = []
        var sendAuth_recruit = []


        //ssafy 사용자
        for (let i = 0; i < this.ssafy_users.length; i++) {
          id = this.ssafy_users[i].id
          if (this.auth_ssafy[i]) {
            sendAuth_ssafy.push({
              id: id,
              auth: 1
            })
          } else {
            sendAuth_ssafy.push({
              id: id,
              auth: null
            })
          }
        }

        //기업 사용자
        for (let i = 0; i < this.auth_recruit.length; i++) {
          id = this.recruit_users[i].id
          if (this.auth_recruit[i]) {
            sendAuth_recruit.push({
              id: id,
              auth: 2
            })
          } else {
            sendAuth_recruit.push({
              id: id,
              auth: null
            })
          }
        }

        console.log('sendSS', sendAuth_ssafy)
        console.log('sendRe', sendAuth_recruit)

        //싸피 유저
        axios.post('/accouts/authenticate/', {
            sendAuth_ssafy: sendAuth_ssafy,
            sendAuth_recruit: sendAuth_recruit
          })
          .then(res => {
            console.log("권한주기 성공")
            alert('변경사항이 저장되었습니다!')
          })
          .catch(err => {
            console.log("권한주기 실패")
          })
      },
    }
  }
</script>

<style scoped>
  span {
    font-size: 16px;
    font-weight: bold;
  }
</style>

<style>
  tr {
    line-height: 3;
  }
</style>