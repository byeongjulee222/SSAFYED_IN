import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './views/HomePage.vue'
import PortfolioUploadPage from './views/PortfolioUploadPage'
import ProfilePage from './views/ProfilePage.vue'
import SsafyPeoplePage from './views/SsafyPeoplePage.vue'
import DetailPortfolioPage from './views/DetailPortfolioPage'
import TeamIntroducePage from './views/TeamIntroducePage'
import PortfolioPage from './views/PortfolioPage'
import RecruitPage from './views/RecruitPage'
import DetailRecruitPage from './views/DetailRecruitPage'
import RecruitWrite from './components/recruit/RecruitWrite'
import RecruitMembers from './views/RecruitMembers'
import CompetitionPage from './views/CompetitionPage'
import DetailCompetitionPage from './views/DetailCompetitionPage'
import CompetitionWrite from './components/competition/CompetitionWrite'
import SSAFYRankPage from './views/SSAFYRankPage'
import CompetitionMembers from './views/CompetitionMembers'
import EditProfilePage from './views/EditProfilePage'
import AdminPage from './views/AdminPage'
import MyPortfoliosPage from './views/MyPortfoliosPage'
import MessageBox from './views/MessageBox'
import MyPostPage from './views/MyPostPage'
Vue.use(Router)

export default new Router({
	mode: 'history',
	base: process.env.BASE_URL,
	routes: [{
			path: '/',
			name: 'home',
			component: HomePage
		},
		{
			path: '/portup/:id?',
			name: 'portup',
			component: PortfolioUploadPage,
			beforeEnter: function (to, from, next) {
				if (authPage.admin_check() || sessionStorage.getItem("uid")) {
					next()
				} else {
					alert("로그인 후 이용가능한 페이지입니다.")
					next({
						path: '/',
					})
				}
			},
		},
		{
			path: '/profile/:id',
			name: 'profile',
			component: ProfilePage,
		},
		{
			path: '/ssafyin',
			name: 'ssafyin',
			component: SsafyPeoplePage
		},
		{
			path: '/detailPort/:id',
			name: 'detailPort',
			component: DetailPortfolioPage
		},
		{
			path: '/team',
			name: 'team',
			component: TeamIntroducePage
		},
		{
			path: '/portfolio',
			name: 'portfolio',
			component: PortfolioPage
		},
		{
			path: '/recruit',
			name: 'Recruit',
			component: RecruitPage
		},
		{
			path: '/recruits/:id',
			name: 'detailRecruit',
			component: DetailRecruitPage
		},
		{
			path: '/recruit_write/:id?',
			name: 'RecruitWrite',
			component: RecruitWrite
		},
		{
			path: '/recruitmembers/:id',
			name: 'recruitmembers',
			component: RecruitMembers
		},
		//competitions
		{
			path: '/competition',
			name: 'Competition',
			component: CompetitionPage
		},
		{
			path: '/competition/:id',
			name: 'detailCompetition',
			component: DetailCompetitionPage
		},
		{
			path: '/competition_write/:id?',
			name: 'CompetitionWrite',
			component: CompetitionWrite
		},
		{
			path: '/ssafyrank',
			name: 'ssafyrank',
			component: SSAFYRankPage
		},
		{
			path: '/compmembers/:id',
			name: 'compmembers',
			component: CompetitionMembers
		},
		{
			path: '/editprofile/:id',
			name: 'editprofile',
			component: EditProfilePage,
			beforeEnter: function (to, from, next) {
				if (!authPage.suc_login()) {
					alert("로그인 후 이용가능한 페이지입니다.")
					next({
						path: '/',
					})
				} else if (to.path.slice(13) != sessionStorage.getItem("uid")) {
					alert("페이지 접근 권한이 없습니다.")
					history.back()
				} else {
					next()
				}
			},
		},
		{
			path: '/admin',
			name: 'admin',
			component: AdminPage,
			beforeEnter: function (to, from, next) {
				if (!authPage.admin_check()) {
					alert("관리자만 접근 가능한 페이지입니다.")
					next({
						path: '/',
					})
				} else {
					next()
				}
			},
		},
		{
			path: '/myportfolios/:id',
			name: 'myportfolios',
			component: MyPortfoliosPage,
		},
		{
			path: '/messagebox/:id',
			name: 'messagebox',
			component: MessageBox,
			beforeEnter: function (to, from, next) {
				if (to.path.slice(12) != sessionStorage.getItem("uid")) {
					alert("페이지 이용 권한이 없습니다.")
					history.back()
				} else {
					next()
				}
			},
		},
		{
			path: '/mypost/:id',
			name: 'mypost',
			component: MyPostPage,
		}
	],
});

var authPage = {
	suc_login: function () {
		if (sessionStorage.getItem("uid") == null || sessionStorage.getItem("uid") == '') {
			return false;
		} else {
			return true;
		}
	},
	admin_check: function () {
		if (!sessionStorage.getItem("super")) {
			return false;
		} else {
			return true;
		}
	},
}