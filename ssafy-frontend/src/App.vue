<template>
	<v-app>
		<Header></Header>
		<v-content>
			<router-view />
		</v-content>
		<Footer></Footer>
	</v-app>

</template>

<script>
	import store from './store'
	import Header from './components/Header'
	import Footer from './components/Footer'
	import './assets/css/common.css'
	export default {
		name: 'App',
		store,
		data() {
			return {
				//
			}
		},
		components: {
			Header,
			Footer,
		}
	}
</script>

<style>
@media screen and (max-width:768px){
	.v-content{
		padding-bottom: 56px !important;
	}
}
</style>