<template>
	<div class="profile_left">
		<div class="profile_img">
			<div class="thumbnail">
				<div class="centered">
					<img :src="getProfileImage(user.profile_img)" alt="안나와" />
				</div>
			</div>
		</div>
		<v-card-text class="headline mb-7 text-center" v-if="login_user_id != id && login_user_id" style="font-weight:bold;">{{ user.nickname }}
			<v-dialog width="500" v-model="sendMessageFlag">
					<template v-slot:activator="{ on }">
						<v-btn fab small color="blue" class="mb-2 text-end" v-on="on">
							<v-icon color="yellow">mdi-bell-outline</v-icon>
						</v-btn>
					</template>
					<v-card class="pa-2 pb-5">
						<v-window>
							<v-card-title>Send Message</v-card-title>
							<v-col cols="12">
								<v-text-field outlined label="받는 사람" v-model="left_user_email" readonly>
								</v-text-field>
							</v-col>
							<v-col cols="12">
							<v-textarea outlined label="전송할 메세지를 적어주세요" v-model="send_content"></v-textarea></v-col>
						</v-window>
							<div class="text-end mr-4">
						<v-btn text color="primary" outlined @click="sendMessage">Send</v-btn>
						</div>
					</v-card>
					<!-- <span style="color:black;">Send Message</span> -->
			</v-dialog>
		</v-card-text>

		<v-card-text class="headline mb-7 text-center" v-else style="font-weight:bold;">{{ user.nickname }}</v-card-text>

		<div class="profile_info">

			<v-list-item>
				<v-list-item-icon>
					<v-icon color="blue lighten-1">work</v-icon>
				</v-list-item-icon>

				<v-list-item-content>
					<v-list-item-title class="white--text title">{{ user.company }}</v-list-item-title>
					<v-list-item-subtitle style="color:#BDBDBD;">company</v-list-item-subtitle>
				</v-list-item-content>
			</v-list-item>

			<v-divider inset></v-divider>

			<v-list-item>
				<v-list-item-icon>
					<v-icon color="blue lighten-1">school</v-icon>
				</v-list-item-icon>

				<v-list-item-content>
					<v-list-item-title class="white--text title">{{ user.major }}</v-list-item-title>
					<v-list-item-subtitle style="color:#BDBDBD;">major</v-list-item-subtitle>
				</v-list-item-content>
			</v-list-item>

			<v-divider inset></v-divider>

			<v-list-item>
				<v-list-item-icon>
					<v-icon color="blue lighten-1">mdi-email</v-icon>
				</v-list-item-icon>

				<v-list-item-content>
					<v-list-item-title class="white--text body-1">{{ user.username }}</v-list-item-title>
					<v-list-item-subtitle style="color:#BDBDBD;">email</v-list-item-subtitle>
				</v-list-item-content>
			</v-list-item>

			<v-divider inset></v-divider>

			<v-list-item>
				<v-list-item-icon>
					<v-icon color="blue lighten-1">fab fa-github</v-icon>
				</v-list-item-icon>

				<v-list-item-content>
					<v-list-item-title class="white--text body-1"><a :href="user.address" target="blank">{{ user.address }}</a></v-list-item-title>
					<v-list-item-subtitle style="color:#BDBDBD;">github url</v-list-item-subtitle>
				</v-list-item-content>
			</v-list-item>
		</div>
	</div>
</template>

<script>
	import '../../assets/css/profile/left.css'
	export default {
		name: 'Left',
		data() {
			return {
				user: {},
				login_user_id: sessionStorage.getItem("uid"),
				left_user_email : '',
				send_content : '',
				sendMessageFlag : false,
			}
		},
		props: {
			id: Number,
		},
		methods: {
			getProfileImage(value) {
				console.log(value)
				if (value != null)
					return value;
					// return 'http://127.0.0.1:8000' + value;
				else
					return require('../../assets/no_picture.png');
			},
			sendMessage() {
				if(this.send_content != '') {
					axios.post('/accouts/sendmessage/' + this.id + '/', {
						sender : this.login_user_id,
						content : this.send_content
					})
					.then( res => {
						console.log("메세지 보내기 성공")
						this.sendMessageFlag = false
						alert('메세지가 전송되었습니다!')
						this.send_content = ''
	
						// console.log(res.data)
					})
					.catch( err => {
						console.log("메세지 보내기 실패")
					})
				}
			}
		},
		created() {
			axios.get('/accouts/' + this.id)
				.then(res => {
					console.log("아이디는" + typeof (this.id))
					this.user = res.data
					this.left_user_email = this.user.username
					console.log("Left component id is " + this.id)
				})
				.catch(err => {
					console.log("Left component error : " + this.id)
				})
		}
	}
</script>
