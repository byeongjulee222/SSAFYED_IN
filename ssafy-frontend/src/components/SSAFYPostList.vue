<template>
    <v-container>
        <a href="/recruit">
            <h3 class="display-1 my-5 mx-3">Recruitment board</h3>
        </a>
        <div class="tableBody">
            <v-simple-table dense>
                <template -slot:default>
                    <tbody>
                        <tr v-for="(item, index) in posts" :key="index" @click="moveRecruitPages(item.id)">
                            <td class="font-weight-regular">
                                <p class="skip">{{ item.title }}</p>
                            </td>
                            <td width="40%" class="text-end">|&nbsp;{{ item.update_at }}</td>
                        </tr>
                    </tbody>
                </template>
            </v-simple-table>
        </div>
        <br><br>
        <a href="/competition">
            <h3 class="display-1 my-5 mx-3">Competition board</h3>
        </a>
        <div class="tableBody">
            <v-simple-table dense>
                <template v-slot:default>
                    <tbody>
                        <tr v-for="(item, index) in competitions" :key="index" @click="moveCompPages(item.id)">
                                <td  class="font-weight-regular">
                                    <p class="skip">{{ item.title }}</p>
                                </td>
                                <td class="text-end">|&nbsp;{{ item.update_at }}</td>
                        </tr>
                    </tbody>
                </template>
            </v-simple-table>
        </div>
    </v-container>
</template>

<script>
    export default {
        name: 'SSAFYPostList',
        data() {
            return {
                competitions: [],
                posts: [],
            }
        },
        methods: {
            getCompetition() {
                axios.get('/competitions/')
                    .then(res => {
                        this.competitions = res.data[0]
                        this.competitions = this.competitions.slice(0, 5);
                    })
                    .catch(err => {
                        console.log(err)
                    })
            },
            getPost() {
                axios.get('/recruits/')
                    .then(res => {
                        this.posts = res.data[0]
                        this.posts = this.posts.slice(0, 5);
                    })
                    .catch(err => {
                        console.log(err)
                    })
            },
            moveCompPages(path) {
                this.$router.push('/competition/'+path)
            },
            moveRecruitPages(path) {
                this.$router.push('/recruits/'+path)
            },
        },
        mounted() {
            this.getPost(),
                this.getCompetition()
        }
    }
</script>

<style scoped>
    .tableBody {
        border: 2px solid #E0E0E0;
        border-radius: 5px;
        margin: auto;
    }
</style>

<style>
    .skip {
        overflow: hidden;
        text-overflow: ellipsis;
        display: inline-block;
        white-space: normal;
        height: 2.0em;
        text-align: left;
        word-wrap: break-word;
        display: -webkit-box;
        -webkit-line-clamp: 1;
        -webkit-box-orient: vertical;
    }
</style>