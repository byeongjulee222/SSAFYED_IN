<template><div class="profile"><Left/><div class="profile_right">
	<v-card>
      <v-card-title>
        Nutrition
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="desserts"
        @click:row="openDetail"
        :search="search"
      ></v-data-table>
    </v-card>
	</div>
  </div>
</template>

<script>
// import PortfolioList from '../components/PortfolioList'
import Left from '../components/profile/Left'
import '../assets/css/profile/profile.css'
export default {
	name: 'SsafypeoplePage',
	components: {
    },
    method:{
        openDetail(item){
            console.log(this.selectedItem +" "+ item.name)
        }
    },
	data() {
		return {
            search: '',
            headers:[
                {
                    text : 'profile',
                    align : 'center',
                    sortable : false,
                    value : 'imgs'
                },
                {text: '기수',value:'grade' },
                {text: '이름',value:'name'},
                {text: '지역',value:'location'},
                {text: '회사',value:'company'},
                {text: '사용언어',value:'tech_stack'}
            ],
            desserts:[
                {
                    imgs : <img src="" alt="없습니당"/>,
                    grade : '2nd',
                    name : '성동민',
                    location : '대전',
                    company : '구직중',
                    tech_stack : 'c,java,php,jsp,vue'
                },
                {
                    grade : '1st',
                    name : '김가은',
                    location : '대전',
                    company : '구직중',
                    tech_stack : 'c,php,jsp,vue'
                },
                {
                    grade : '1st',
                    name : '김가은',
                    location : '대전',
                    company : '구직중',
                    tech_stack : 'c,php,jsp,vue'
                },
                {
                    grade : '1st',
                    name : '김가은',
                    location : '대전',
                    company : '구직중',
                    tech_stack : 'c,php,jsp,vue'
                },
                {
                    grade : '3rd',
                    name : '이병주고약주고',
                    location : '대전',
                    company : '구직중',
                    tech_stack : 'c,java,jsp,vue'
                },
                {
                    grade : '4th',
                    name : '우동균',
                    location : '대전',
                    company : '구직중',
                    tech_stack : 'c,java,php,vue'
                }
            ]
		}
	}
}
</script>

