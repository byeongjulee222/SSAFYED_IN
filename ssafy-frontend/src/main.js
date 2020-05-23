import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'
import Vue from 'vue'
import './plugins/axios'
import Vuetify from 'vuetify/lib'
import 'vuetify/dist/vuetify.min.css'
import VueSimplemde from 'vue-simplemde'
import 'simplemde/dist/simplemde.min.css'
import 'font-awesome/css/font-awesome.min.css'


import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueSession from 'vue-session'

// import UploadImage from 'vue-upload-image' //vue-upload-image import

//vue-upload-image register
// Vue.component('upload-image', UploadImage)


//vuetify 예제들은 일반 버튼을 쓰는게 아니라 material design의 버튼을 쓴다.
//npm install material-design-icons-iconfont 해준 뒤 해당 구문을 import시킨다.
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'
import '@fortawesome/fontawesome-free/css/all.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(Vuetify)
Vue.use(VueSimplemde)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueSession)
// Vue.prototype.$server = 'http://192.168.0.4:8000'
Vue.prototype.$server = 'http://i02b102.p.ssafy.io:8054'
// Vue.prototype.$server = 'http://127.0.0.1:8000'
// http://192.168.31.126:8000


new Vue({
  router,
	store,
	vuetify: new Vuetify({
		iconfont: 'fa',
		theme: {
			primary: '#3f51b5',
			secondary: '#b0bec5',
			accent: '#8c9eff',
			error: '#b71c1c'
		},
		icons: { //icon 보이게 하려면 이 부분 꼭 필요함
			iconfont: 'md',
		},
	}),
  render: h => h(App)
}).$mount('#app')
