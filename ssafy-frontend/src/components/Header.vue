<template>
    <div>
        <v-app-bar app color="light-blue lighten-2" dark absolute>
            <div>
                <span class="mx-5 menu white--text hidden-sm-and-down font-weight-medium" v-for="menu in MainMenus"
                    :key="menu.title">
                    <router-link :to="menu.path">{{ menu.title }}</router-link>
                </span>
            </div>
            <router-link class="mx-5 menu white--text hidden-md-and-up font-weight-medium margin-8" to="/"> SSAFYed人
            </router-link>

            <v-spacer></v-spacer>



            <!--로그인 모달-->

            <!--로그인 성공시-->
            <div>
                <div v-if="login_success">
                    <v-menu offset-y>
                        <template v-slot:activator="{ on }">
                            <v-btn text class="font-weight-black" style="text-transform: none;" v-on="on">
                                <v-avatar size="32" color="white" class="mr-2">
                                    <v-img :src="user.profile_img"></v-img>
                                </v-avatar>
                                {{ user.nickname}}
                            </v-btn>
                        </template>
                        <v-list dense>
                            <v-list-item-title v-for="(item, i) in dropDownMenus" :key="i" class="mainMenu">
                                <v-btn text @click="movePages(item.path)" block>
                                    {{ item.title }}</v-btn>
                            </v-list-item-title>
                            <div class="v-list-item__title mainMenu">
                                <v-btn text @click="logout" block>logout</v-btn>
                            </div>
                            <template v-if="user.is_superuser">
                                <div class="v-list-item__title mainMenu" style="background-color:rgba(33,33,33,.1);">
                                    <v-btn text @click="moveAdminPage" block>Members</v-btn>
                                </div>
                            </template>
                        </v-list>
                    </v-menu>
                    <!--알림함-->
                    <v-badge color="red" :content="bell_msg" overlap class="mx-2">
                        <v-icon color="white" @click="movePages('/messagebox/')">mdi-bell-outline</v-icon>
                    </v-badge>

                </div>

                <!--로그인 폼-->
                <div v-else>
                    <v-dialog v-model="loginDialog" width="500">
                        <template v-slot:activator="{ on }">
                            <v-btn v-on="on" text>login</v-btn>
                        </template>
                        <v-card class="mx-auto" max-width="500">
                            <v-window>
                                <v-card-title>Login</v-card-title>
                                <v-card-text>
                                    <v-text-field label="Email" v-model="login.username"></v-text-field>
                                    <v-text-field @keyup.enter="loginBtn" label="Password" type="password"
                                        v-model="login.password">
                                    </v-text-field>
                                    <span class="caption grey--text text--darken-1">
                                        Please enter a password for your account
                                    </span>

                                    <!--비밀번호 찾기-->

                                    <v-dialog v-model="findpwdBtn" width="500">
                                        <template v-slot:activator="{ on }">
                                            <v-card-subtitle class="text-end pa-0 ">
                                                <v-btn v-on="on" text
                                                    style="text-transform:none; color:#039BE5; padding:0px;" @click="loginDialog = false, 
                                                findpwdBtn=true">Find
                                                    Password</v-btn>
                                            </v-card-subtitle>
                                        </template>
                                        <v-card class="mx-auto" max-width="500">
                                            <v-window>
                                                <v-card-text>
                                                    <v-card-title>Find Password</v-card-title>
                                                    <v-text-field label="Email" v-model="findpwd.username"
                                                        hint="이메일을 입력해주세요">
                                                    </v-text-field>
                                                    <v-text-field label="Name" @keyup.enter="postFindPwd"
                                                        v-model="findpwd.nickname" hint="이름을 입력해주세요">
                                                    </v-text-field>
                                                </v-card-text>
                                            </v-window>
                                            <v-divider></v-divider>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn color="primary" outlined @click="postFindPwd">
                                                    find
                                                </v-btn>
                                                <v-btn outlined @click="findpwdBtn = false">
                                                    cancel
                                                </v-btn>
                                            </v-card-actions>
                                        </v-card>
                                    </v-dialog>
                                </v-card-text>
                            </v-window>

                            <v-divider></v-divider>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" outlined @click="loginBtn" @keyup.enter="submit">
                                    login
                                </v-btn>
                                <v-btn color="gray" outlined @click="loginDialog = false">
                                    cancel
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>

                    <!--회원가입 모달-->
                    <v-dialog v-model="signUpDialog" width="500">
                        <template v-slot:activator="{ on }">
                            <v-btn v-on="on" text>sign up</v-btn>
                        </template>
                        <v-card>
                            <v-card-title>Sign Up</v-card-title>
                            <v-card-text>
                                <!--회원가입 Form-->
                                <v-form>
                                    <!-- ref="form" v-model="valid" :lazy-validation="lazy"-->
                                    <!--이메일-->
                                    <v-text-field label="*Email" v-model="signup.username" required :rules="emailRules"
                                        prepend-icon="email"></v-text-field>
                                    <!--Password-->
                                    <v-text-field label="*Password" v-model="signup.password" required type="password"
                                        :rules="passRules" prepend-icon="check"></v-text-field>
                                    <!--Password Confirm-->
                                    <v-text-field label="*Password Confirm" required type="password"
                                        :rules="confirmPass" prepend-icon="done_outline"></v-text-field>
                                    <!--이름-->
                                    <v-text-field label="*Name" v-model="nickname" required :rules="nameRules"
                                        prepend-icon="perm_identity"></v-text-field>
                                    <!--기수-->
                                    <v-select :items="['0', '1', '2', '3']" label="*Grade(기수를 선택해주세요)" v-model="grade"
                                        prepend-icon="looks_two" hint="기업 사용자는 0번을 선택해주세요" required :rules="gradeRules">
                                    </v-select>
                                    <!--회사-->
                                    <v-text-field label="Company" v-model="company" prepend-icon="work"
                                        hint="기업사용자는 재직중인 회사를 입력해주세요">
                                    </v-text-field>
                                    <!--기술스택-->
                                    <v-autocomplete :items="items" label="tech_category" multiple small-chips
                                        prepend-icon="assignment" v-model="tech_category">
                                    </v-autocomplete>
                                    <!--인증-->
                                    <!-- v-on:change="handleFileUpload" -->
                                    <!-- type="file"  -->
                                    <v-card outlined class="pt-4 px-4">
                                        <p class="font-weight-black">
                                            <v-icon>attach_file</v-icon>인증파일을 첨부해주세요
                                        </p>
                                        <FP v-on:load_img="getServerImag" />
                                    </v-card>
                                </v-form>
                                <!--서약서-->
                                <v-checkbox v-model="checkbox" :rules="[v => !!v || '동의하지않으면 회원가입이 불가합니다.']"
                                    label="동의합니까?" required>
                                </v-checkbox>
                                <!--필수입력 표시-->
                                <small style="color:red;">*표시가 된 항목은 필수 입력 항목입니다.</small>
                            </v-card-text>
                            <v-divider class="ma-0"></v-divider>
                            <v-card-actions class="pa-4">
                                <v-spacer></v-spacer>
                                <v-btn color="primary" outlined @click="validate">
                                    save
                                </v-btn>
                                <v-btn color="gray" outlined @click="signUpDialog = false">
                                    cancel
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </div>

            </div>
        </v-app-bar>
    </div>
</template>
<script>
    import router from '../router'
    import jwtDecode from 'jwt-decode'
    import FP from './ImageUpload'
    export default {
        name: 'Header',
        data() {
            return {
                login: {
                    username: '',
                    password: '',
                },
                signup: {
                    username: '',
                    password: '',
                },
                findpwd: {
                    username: '',
                    nickname: '',
                },
                sidebar: false,
                loginDialog: false,
                signUpDialog: false,
                emailRules: [
                    v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'Email 형식을 맞춰주세요.',
                    v => !!v || '이메일을 입력해주세요',
                    v => !!(v.includes('@naver.com') || v.includes('@nate.com') || v.includes('@gmail.com') || v
                        .includes('@hanmail.net')) || '유효하지 않은 이메일입니다',
                ],
                passRules: [
                    v => !!v || '비밀번호를 입력해주세요',
                ],
                confirmPass: [
                    v => !!(v == this.signup.password) || '비밀번호가 다릅니다!',
                ],
                nickname: null,
                nameRules: [
                    v => !!v || '이름을 입력해주세요',
                    v => (v && v.length <= 10) || '이름은 10자 이내로 입력해주세요',
                ],
                grade: null,
                gradeRules: [
                    v => !!v || '기수를 선택해주세요',
                ],
                company: '',
                items: [{
                        value: 1,
                        text: 'Java'
                    },
                    {
                        value: 2,
                        text: 'C'
                    },
                    {
                        value: 3,
                        text: 'C++'
                    },
                    {
                        value: 4,
                        text: 'Python'
                    },
                    {
                        value: 5,
                        text: 'AI'
                    },
                    {
                        value: 6,
                        text: 'IoT'
                    },
                    {
                        value: 7,
                        text: '자율주행'
                    },
                    {
                        value: 8,
                        text: '빅데이터'
                    },
                    {
                        value: 9,
                        text: 'Django'
                    },
                    {
                        value: 10,
                        text: 'Vue'
                    },
                    {
                        value: 11,
                        text: 'JavaScript'
                    },
                ],
                verified_img: null,
                verifiedFileRules: [
                    v => !!v || '인증파일을 첨부해주세요',
                ],
                lazy: false,
                valid: null,
                checkbox: false,
                tech_category: [],
                login_success: false,
                user: {}, //로그인 후 get한 정보를 담음
                dropDownMenus: [{
                        title: 'Profile',
                        path: "/editprofile/"
                    },
                    {
                        title: 'MyPage',
                        path: "/profile/"
                    },
                    {
                        title: 'Portfolios',
                        path: "/myportfolios/"
                    },
                    {
                        title: 'Posts',
                        path: "/mypost/"
                    },
                ],
                findpwdBtn: false,
                MainMenus: [{
                        title: 'Home',
                        path: '/',
                    },
                    {
                        title: 'Portfolio',
                        path: '/portfolio',
                    },
                    {
                        title: 'Recruit',
                        path: '/recruit',
                    },
                    {
                        title: 'Competition',
                        path: '/competition',
                    },
                    {
                        title: 'SSAFYRank',
                        path: '/ssafyrank',
                    },
                ],
                text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                tab: null,
                bell_msg: '',
            }
        },
        components: {
            FP
        },
        methods: {
            getServerImag(serverid) {
                this.verified_img = serverid
                console.log(this.verified_img)
            },
            loginBtn() { //로그인 시 호출
                if (this.checkForm()) {
                    console.log(this.$server)
                    console.log('checkform')
                    axios.post('/token/', {
                            username: this.login.username,
                            password: this.login.password,
                        })
                        .then(res => {
                            this.$session.start() // 추가
                            this.$session.set('jwt', res.data.token) // 추가

                            this.createTodo(); //토큰 생성 후 session에서 얻은 id로 사용자 정보 가져옴
                            location.href = '/'
                        })
                        .catch(err => {
                            console.log("로그인 에러:" + err)
                            alert('이메일/비밀번호를 확인해주세요')
                        })
                } else {
                    console.log('로그인 검증 실패')
                }
            },
            createTodo() {
                // this.$session.start() // 세션 활성화
                const token = this.$session.get('jwt')
                const uid = jwtDecode(token).user_id

                sessionStorage.setItem('uid', uid)
                sessionStorage.setItem('token', token)

                axios.get('/accouts/' + uid)
                    .then(res => {
                        this.user = res.data;
                        sessionStorage.setItem('name', this.user.nickname)
                        sessionStorage.setItem('email', this.user.username)
                        sessionStorage.setItem('auth', this.user.auth)
                        sessionStorage.setItem('super', this.user.is_superuser)
                        if (this.user.profile_img == null || this.user.profile_img == '')
                            this.user.profile_img = require('../assets/no_picture.png')
                        else
                            this.user.profile_img = this.user.profile_img;
                        console.log(this.user.is_superuser)
                        console.log(this.user)
                    })
                    .catch(err => {
                        console.log("사용자 정보 못불러옴:" + err)
                    })

                //알림메세지
                axios.get('/accouts/message_list/' + uid)
                    .then(res => {
                        this.bell_msg = res.data[2].notread + ''
                    })
            },
            checkForm() { //모든 값이 입력되었는지 확인
                this.errors = []
                // id가 없는 경우 에러 발생
                if (!this.login.username || !this.login.password) {
                    // this.errors.push("아이디를 넣어줘ㅓㅓㅓ")
                    alert('이메일과 비밀번호 모두 입력해주세요')
                }
                if (this.errors.length == 0) {
                    return true
                }
            },
            postFindPwd() { //임시비밀번호 발급 위해 호출
                if (this.findpwd.username == '' || this.findpwd.nickname == '') {
                    alert('이메일과 이름을 확인해주세요!')
                } else {
                    axios.post('/accouts/password_email/', {
                            username: this.findpwd.username,
                            nickname: this.findpwd.nickname
                        })
                        .then(res => {
                            alert('임시 비밀번호가 이메일로 발송되었습니다')
                            console.log("비밀번호 찾기 성공")
                        })
                        .catch(err => {
                            console.log("비밀번호 찾기 실패")
                            alert('이메일과 이름을 확인해주세요!')
                        })
                }
            },
            handleFileUpload(event) { //verified_img 업로드 함수
                console.log('event', event)
                const input = event;

                if (input.name !== undefined) {
                    // 이 이미지를 읽고 base64 형식으로 변환 할 새 FileReader를 작성하십시오.
                    var reader = new FileReader();
                    // FileReader가 작업을 완료 할 때 실행할 콜백 함수 정의
                    reader.onload = (e) => {
                        // 참고 : 여기에서 사용 된 화살표 함수, "this.imageData"는 Vue 구성 요소의 imageData를 나타냅니다.
                        // base64로 이미지를 읽고 imageData로 설정
                        this.verified_img = e.target.result;
                    }
                    console.log("hi", this.verified_img)
                    // 리더 작업 시작-파일을 데이터 URL (base64 형식)로 읽습니다.
                    console.log(input)
                    reader.readAsDataURL(input);
                    console.log(input)
                    // this.imageData = input.files[0].name;
                }
                // console.log('ok')
                // console.log(this.verified_img)
            },
            validate() { //회원가입 완료 함수
                if (this.signup.username && this.signup.password && this.nickname && this.grade) {
                    var confirm_ssafy = prompt(
                        "해당 사이트 가입자는 SSAFY내에서 진행된 커리큘럼 및 프로젝트 내용에 대한 부적절한 공유를 금지하고 있으며 이에 동의한다면 괄호 내용을 입력해주세요. [지킴]"
                    )
                    if (confirm_ssafy == '지킴') {
                        axios.post('/accouts/signup/', {
                                headers: {
                                    'Content-Type': 'multipart/form-data'
                                },
                                username: this.signup.username, //
                                password: this.signup.password, //
                                nickname: this.nickname, //
                                grade: this.grade, //
                                company: this.company, //
                                tech_category: this.tech_category, //
                                verified_img: this.verified_img, //
                            })
                            .then(response => {
                                alert('회원가입이 완료되었습니다!')
                                this.signUpDialog = false
                                this.signup.password = '',
                                    this.nickname = null,
                                    this.grade = null,
                                    this.company = '',
                                    this.tech_category = '',
                                    this.verified_img = null,
                                    this.signUpDialog = false
                            })
                            .catch(err => {
                                alert('필수항목값을 확인해주세요!')
                            })
                    } else {
                        alert('서약 내용을 다시 작성해주세요')
                    }
                }

            },
            logout() { //로그아웃시
                var check_logout = confirm("로그아웃 하시겠습니까?")
                if (check_logout) {
                    this.$session.destroy()
                    this.login_success = false
                    sessionStorage.clear()
                    console.log("로그아웃 완료")
                    location.href = '/'
                }
            },
            movePages(path) {
                // this.$router.push(path + sessionStorage.getItem("uid"))
                location.href = path + sessionStorage.getItem("uid")
            },
            moveAdminPage() {
                this.$router.push('/admin')
            }
        },
        created() {
            if (this.$session.has('jwt')) {
                console.log("이미 로그인 된 상태입니다.")
                this.login_success = true;
                this.createTodo();
            }
        }
    }
</script>
<style scoped>
    .menu {
        text-decoration: none;
        color: black;
    }

    .mainMenu:hover {
        background-color: rgb(240, 240, 240);
    }
</style>