<template>
	<div class="profile">
		<Left :id="pageId" />
		<div class="profile_right">
			<div class="profile_wrap">

				<div class="edit_profile">

					<!--수상내역-->
					<div class="award my-8">
						<v-card-text class="headline text-xs-center pl-0">수상내역</v-card-text>
						<v-col cols="12" lg="8" md="8" class="pa-0">
							<v-card v-if="!editFlag && beforeEdit.award_1 != ''" outlined height="100">
								<ul class="pa-2 mx-2 body-2 black--text">
									<li class="py-1">{{ beforeEdit.award_1 }}</li>
									<li class="py-1">{{ beforeEdit.award_2 }}</li>
									<li class="py-1">{{ beforeEdit.award_3 }}</li>
								</ul>
							</v-card>

							<v-card v-else-if="editFlag" no-resize outlined v-model=" beforeEdit.award">
								<ul class="pa-2 mx-5">
									<v-card-text class="body-2 font-weight-bold">
										최대 3개 항목까지 작성 가능합니다.
									</v-card-text>
									<li>
										<v-text-field v-model="beforeEdit.award_1"></v-text-field>
									</li>
									<li>
										<v-text-field v-model="beforeEdit.award_2"></v-text-field>
									</li>
									<li>
										<v-text-field v-model="beforeEdit.award_3"></v-text-field>
									</li>
								</ul>
							</v-card>

							<v-card v-else outlined height="140">
								<v-card-text class="body-2">
									작성된 내용이 없습니다.
								</v-card-text>
							</v-card>
						</v-col>
					</div>

					<!--자기소개-->
					<div class="introduce my-8">
						<v-card-text class="headline text-xs-center pl-0">자기소개</v-card-text>
						<!--줄바꿈-->
						<v-col cols="12" lg="8" md="8" class="pa-0">
							<v-card v-if="!editFlag && beforeEdit.introduce != ''" outlined height="140">
								<v-card-text class="body-2 font-weight-medium black--text">
									{{ beforeEdit.introduce }}
								</v-card-text>
							</v-card>

							<v-textarea v-else-if="editFlag" outlined no-resize v-model="beforeEdit.introduce"
								class="body-2">
							</v-textarea>

							<v-card v-else outlined height="140">
								<v-card-text class="body-2">
									작성된 내용이 없습니다.
								</v-card-text>
							</v-card>
						</v-col>
					</div>

					<!--기술스택-->
					<div class="tech_stack my-8">
						<v-card-text class="headline text-xs-center pl-0">기술스택</v-card-text>
						<v-col cols="12" lg="8" md="8" class="pa-0">
							<v-card v-if="!editFlag && beforeEdit.tech_category != ''" class="pa-2" outlined
								height="100%">
								<v-chip v-for="(tech, index) in beforeEdit.tech_category" :key="index" class="ma-2"
									color="primary">
									<v-icon left>mdi-label</v-icon>
									{{ tech }}
								</v-chip>
							</v-card>
							<v-autocomplete v-else-if="editFlag" :items="items" multiple chips color="primary"
								v-model="beforeEdit.tech_category" label="select tech"></v-autocomplete>

							<v-card v-else class="pl-2" outlined height="100%">
								<v-card-text class="body-2 font-weight-light pl-2">선택된 기술스택이 없습니다.</v-card-text>
							</v-card>

						</v-col>
					</div>

					<div class="edit_tatalBtn text-end">
						<v-col cols="12" lg="8" md="8" class="pa-0">
							<v-btn class="primary" rounded @click="editForm" v-if="showEditBtn">Edit</v-btn>
							<v-btn color="primary" rounded outlined v-if="editBtn" @click="saveForm">Save</v-btn>
						</v-col>
					</div>
				</div>

				<!--포트폴리오 컴포넌트-->
				<v-layout my-5>
					<v-flex xs12>
						<div style="display:inline-block;">
							<v-card-text class="headline text-xs-center pl-0">포트폴리오</v-card-text>
						</div>
						<div style="text-align:end;" v-if="portfolios != '' && portfolios != undefined">
							<router-link :to="'/myportfolios/' + pageId">More ></router-link>
						</div>

						<v-card v-if="portfolios != '' && portfolios != undefined" outlined>
							<SSAFYPortfolioList :portfolios="portfolios"></SSAFYPortfolioList>
						</v-card>

						<v-card v-else outlined height="350">
							<v-card-text class="body-2">
								등록된 포트폴리오가 없습니다.
							</v-card-text>
						</v-card>

					</v-flex>
				</v-layout>
			</div>
		</div>
	</div>
</template>
<script>
	import Vue from 'vue'
	import Left from '../components/profile/Left'
	import '../assets/css/profile/profile.css'
	import SSAFYPortfolioList from '../components/SSAFYPortfolioList'
	import ProfileMobile from '../components/ProfileMobile'
	import jwtDecode from 'jwt-decode'

	export default {
		name: 'ProfilePage',
		components: {
			Left,
			SSAFYPortfolioList,
			ProfileMobile,
		},
		data() {
			return {
				portfolios: [],
				user: {},
				pageId: Number(this.$route.params.id),
				editFlag: false, //수정하기 버튼을 누르면 항목들이 수정할 수 있는 textarea로 바뀐다.
				showEditBtn: false, //로그인한 사용자이면 수정하기 버튼이 보인다.
				editBtn: false, //수정하기 버튼
				items: ['Java', 'C', 'C++', 'Python', 'AI', 'IoT', '자율주행', '빅데이터', 'Django', 'Vue', 'JavaScript'],
				beforeEdit: {
					award_1: '',
					award_2: '',
					award_3: '',
					introduce: '',
					tech_category: [],
				},
			}
		},
		methods: {
			editForm() {
				//눌리면 텍스트들 보여준다
				this.editFlag = true
				this.showEditBtn = false
				this.editBtn = true
			},
			saveForm() {
				this.showEditBtn = true
				this.editBtn = false
				this.editFlag = false
				var techArray = []
				for (let i = 0; i < this.items.length; i++) {
					for (let j = 0; j < this.beforeEdit.tech_category.length; j++) {
						if (this.items[i] == this.beforeEdit.tech_category[j]) {
							techArray.push(i + 1)
						}
					}
				}

				axios.post('/accouts/update/' + sessionStorage.getItem("uid") + '/', {
						award_1: this.beforeEdit.award_1,
						award_2: this.beforeEdit.award_2,
						award_3: this.beforeEdit.award_3,
						introduce: this.beforeEdit.introduce,
						tech_category: techArray
					})
					.then(res => {
						this.user = res.data
						console.log("포스트 한 후")
						console.log(this.user)
						this.beforeEdit.tech_category = []

						for (let i = 0; i < this.user.tech_category.length; i++) {
							for (let j = 0; j < this.items.length; j++) {
								if (j + 1 == this.user.tech_category[i]) {
									this.beforeEdit.tech_category.push(this.items[j])
									break
								}
							}
						}

						this.beforeEdit.award_1 = this.user.award_1
						this.beforeEdit.award_2 = this.user.award_2
						this.beforeEdit.award_3 = this.user.award_3
						this.beforeEdit.introduce = this.user.introduce

						console.log("수정된 내용 post 성공")
						alert('저장되었습니다')
					})
					.catch(err => {
						console.log("수정하기 내용 post 실패")
					})
			},
		},
		created() {
			if (sessionStorage.getItem("uid") == this.pageId) {
				console.log("id 일치로 수정가능함")
				this.showEditBtn = true
			}

			axios.get('/accouts/' + this.pageId + '/')
				.then(res => {
					this.user = res.data
					this.beforeEdit.award_1 = this.user.award_1
					this.beforeEdit.award_2 = this.user.award_2
					this.beforeEdit.award_3 = this.user.award_3
					this.beforeEdit.introduce = this.user.introduce
					this.beforeEdit.tech_category = []
					for (let i = 0; i < this.user.tech_category.length; i++) {
						this.beforeEdit.tech_category.push(this.user.tech_category[i].tech_stack)
					}
					console.log("회원 마이페이지 정보 가져옴")
				})
				.catch(err => {
					console.log("회원 마이페이지 에러")
				})

			axios.get('/accouts/' + this.pageId)
				.then(res => {
					this.portfolios = res.data.portfolio_set.slice(0, 3)
				})
				.catch(err => {
					console.log("마이페이지 요약 포트폴리오 못가져옴")
				})
		},
	}
</script>