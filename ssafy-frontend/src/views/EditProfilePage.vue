<template>
    <div>
        <v-card-text class="mt-5">
            <v-sheet max-width="650" class="mx-auto">

                <v-col cols="12" class="pb-4">
                    <v-icon>image</v-icon>
                    Profile Picture
                    <v-card width="40%" class="mt-2">
                        <FP v-on:load_img="getServerImag" />
                    </v-card>
                </v-col>

                <!--이메일-->
                <v-col cols="8">
                    <v-text-field label="Email*" v-model="user.username" prepend-icon="email" readonly>
                    </v-text-field>
                </v-col>
                <v-card outlined class="grey lighten-4 mb-4">
                    <!--Password-->
                    <v-col cols="8">
                        <v-text-field label="Password" v-model="pwd" type="password" prepend-icon="check">
                        </v-text-field>
                    </v-col>
                    <!--Password Confirm-->
                    <v-col cols="8">
                        <v-text-field label="Password Confirm" type="password" prepend-icon="done_outline"
                            v-model="confirm_pwd">
                        </v-text-field>
                    </v-col>

                    <v-col class="text-end">
                        <v-btn outlined style="text-transform:none;" class="mb-3" color="primary" @click="sendPassword">
                            Change Password
                        </v-btn>
                    </v-col>
                </v-card>
                <!--이름-->
                <v-col cols="8">
                    <v-text-field label="Name*" v-model="user.nickname" readonly prepend-icon="perm_identity">
                    </v-text-field>
                </v-col>
                <!--기수-->
                <v-col cols="8">
                    <v-text-field label="Grade(기수)" v-model="user.grade" prepend-icon="looks_two" readonly>
                    </v-text-field>
                </v-col>
                <!--회사-->
                <v-col cols="10">
                    <v-text-field label="Company" v-model="company" prepend-icon="work">
                    </v-text-field>
                </v-col>
                <!--전공-->
                <v-col cols="10">
                    <v-text-field label="Major" v-model="major" prepend-icon="school">
                    </v-text-field>
                </v-col>
                <!--github url-->
                <v-col cols="10">
                    <v-text-field label="GitHub Url" v-model="address" prepend-icon="fab fa-github">
                    </v-text-field>
                </v-col>


                <!--기술스택-->
                <v-col cols="12">
                    <v-autocomplete :items="items" label="tech_category" multiple small-chips prepend-icon="assignment"
                        v-model="tech_category">
                    </v-autocomplete>
                </v-col>

                <!--인증-->
                <!-- <v-file-input show-size label="인증파일을 첨부해주세요." hint="ex) SSAFY 학생증 또는 이수증" persistent-hint
                        v-model="verified_img">
                    </v-file-input> -->
                <!-- </v-form> -->

                <!--필수입력 표시-->
                <small style="color:red;">*표시가 된 항목은 필수 입력 항목입니다.</small>
                <!-- <v-divider class="ma-0"></v-divider> -->
                <v-card-actions class="pa-4">
                    <v-spacer></v-spacer>
                    <v-btn color="primary" outlined @click="postUpdateUser">
                        save
                    </v-btn>
                    <v-btn color="gray" outlined @click="postDeleteUser">
                        delete
                    </v-btn>
                </v-card-actions>
            </v-sheet>
        </v-card-text>

    </div>
</template>
<script>
    import FP from '../../src/components/ImageUpload'
    import {
        BIconAlertSquare
    } from 'bootstrap-vue'

    export default {
        name: 'EditProfile',
        data() {
            return {
                user: {},
                pwd: '',
                confirm_pwd: '',
                user_pwd: '',
                company: '',
                major: '',
                address: '',
                gradeRules: [
                    v => !!v || '기수를 선택해주세요',
                ],
                items: ['Java', 'C', 'C++', 'Python', 'AI', 'IoT', '자율주행', '빅데이터', 'Django', 'Vue', 'JavaScript'],
                verified_img: null,
                verifiedFileRules: [
                    v => !!v || '인증파일을 첨부해주세요',
                ],
                checkbox: false,
                tech_category: [],
                profile_img: null,
            }
        },
        components: {
            FP
        },
        methods: {
            getServerImag(serverid) {
                this.profile_img = serverid
                console.log(this.profile_img)
            },
            sendPassword() {
                if (this.pwd != '' && this.confirm_pwd != '' &&
                    this.pwd == this.confirm_pwd) {
                    const requestHeader1 = {
                        headers: {
                            Authorization: 'JWT ' + sessionStorage.getItem("token")
                        }
                    }
                    axios.post('/accouts/password/' + sessionStorage.getItem("uid") + '/', (requestHeader1, {
                            password: this.confirm_pwd
                        }))
                        .then(res => {
                            alert('비밀번호가 수정되었습니다.')
                            console.log("비밀번호 변경 성공")
                            this.pwd = ''
                            this.confirm_pwd = ''
                        })
                        .catch(err => {
                            console.log("비밀번호 변경 실패" + err)
                        })
                } else {
                    alert('비밀번호를 확인해주세요!')
                }
            },
            //업데이트
            postUpdateUser() {
                const techArray = []
                for (let i = 0; i < this.items.length; i++) {
                    for (let j = 0; j < this.tech_category.length; j++) {
                        if (this.items[i] == this.tech_category[j]) {
                            techArray.push(i + 1)
                        }
                    }
                }
                const requestHeader = {
                    headers: {
                        Authorization: 'JWT ' + sessionStorage.getItem("token")
                    }
                }
                console.log(requestHeader)
                axios.post('/accouts/update/' + sessionStorage.getItem("uid") + '/', (requestHeader, {
                        company: this.company,
                        tech_category: techArray,
                        major: this.major,
                        address: this.address,
                        profile_img: this.profile_img,
                    }))
                    .then(res => {
                        console.log("회원 정보 수정 성공")
                        this.user = res.data
                        this.company = this.user.company
                        this.major = this.user.major
                        this.address = this.user.address
                        this.profile_img = this.user.profile_img
                    })
                    .catch(err => {
                        console.log("회원 정보 수정 실패")
                    })

                alert('회원 정보가 수정되었습니다.')
            },

            postDeleteUser() {
                //삭제시
                var delete_confirm = confirm("정말로 탈퇴하시겠습니까?");

                if (delete_confirm) {
                    var confirm_email = prompt("탈퇴를 위한 이메일을 적어주세요", "")
                    if (confirm_email == this.user.username && confirm_email != '') {
                        axios.delete('/accouts/update/' + sessionStorage.getItem("uid") + '/')
                            .then(res => {
                                console.log("회원 삭제")
                            })
                            .catch(err => {
                                console.log("회원 삭제 실패")
                            })
                        alert('탈퇴가 완료되었습니다.')
                        sessionStorage.clear()
                        this.$session.destroy()
                        location.href = '/'
                    } else {
                        alert('이메일을 다시 입력해주세요')
                    }
                }
            }
        },
        created() {
            //패스워드를 제외한 나머지 회원정보 가져오기
            axios.get('/accouts/' + sessionStorage.getItem("uid"))
                .then(res => {
                    this.user = res.data
                    this.company = this.user.company
                    this.major = this.user.major
                    this.address = this.user.address

                    for (let i = 0; i < this.user.tech_category.length; i++) {
                        this.tech_category.push(this.user.tech_category[i].tech_stack)
                    }
                    console.log("회원정보 가져오기 성공")
                })
                .catch(err => {
                    console.log("회원정보 가져오기 에러:" + this.uid)
                })
        }
    }
</script>
