<template>
    <div class="pa-5">
        <v-row>
            <v-col cols="12" md="6">
                <v-card class="grey lighten-4" scrollable>
                    <v-card-title>
                        <span>보낸 메세지</span>
                    </v-card-title>

                    <v-card-text>
                        <div v-if="received_msg != ''">
                            <v-expansion-panels accordion>
                                <v-expansion-panel v-for="(sent, index) in sent_msg" :key="index">
                                    <v-expansion-panel-header>
                                        <p class=" ma-0 pa-0">
                                            {{ sent.recipient.nickname }}<span
                                                class="caption pl-2">{{ sent.sentAt.slice(0, 19) }}</span></p>
                                    </v-expansion-panel-header>
                                    <v-expansion-panel-content>
                                        {{ sent.content }}
                                    </v-expansion-panel-content>
                                </v-expansion-panel>
                            </v-expansion-panels>
                        </div>
                        <v-sheet v-else>
                            <v-card-subtitle>보낸 메세지가 없습니다.</v-card-subtitle>
                        </v-sheet>

                    </v-card-text>
                </v-card>
            </v-col>


            <v-col cols="12" md="6">
                <v-card class="blue lighten-5">
                    <v-card-title>
                        <span>받은 메세지</span>
                    </v-card-title>

                    <v-card-text>
                        <div v-if="received_msg != ''">
                            <v-expansion-panels accordion>
                                <v-expansion-panel v-for="(received, index) in received_msg" :key="index">
                                    <v-expansion-panel-header>
                                        <p class=" ma-0 pa-0">
                                            {{ received.sender.nickname }}<span
                                                class="caption pl-2">{{ received.sentAt.slice(0, 19) }}</span></p>
                                    </v-expansion-panel-header>
                                    <v-expansion-panel-content>
                                        {{ received.content }}


                                        <div class="text-end">
                                            <v-btn text color="grey" outlined small @click="postIsRead(received.id)" 
                                            v-if="!received.isRead" style="display:inline-block;"
                                            >
                                                read</v-btn>

                                            <v-dialog width="500">
                                                <template v-slot:activator="{ on }">
                                                    <v-btn text color="primary" outlined @click="reply_content=''"
                                                        v-on="on" small class="ml-1">
                                                        Send reply</v-btn>
                                                </template>


                                                <v-card class="pa-2 pb-5">
                                                    <v-window>
                                                        <v-card-title>Send Reply Message</v-card-title>
                                                        <v-col cols="12">
                                                            <v-text-field outlined label="받는 사람"
                                                                v-model="received.sender.username" readonly>
                                                            </v-text-field>
                                                        </v-col>
                                                        <v-col cols="12">
                                                            <v-textarea outlined v-model="reply_content"></v-textarea>
                                                        </v-col>
                                                    </v-window>

                                                    <div class="text-end mr-4">
                                                        <v-btn text color="primary" outlined
                                                            @click="sendReply(received.sender.id)">Send</v-btn>
                                                    </div>
                                                </v-card>
                                            </v-dialog>
                                        </div>
                                    </v-expansion-panel-content>
                                </v-expansion-panel>
                            </v-expansion-panels>
                        </div>

                        <v-sheet v-else>
                            <v-card-subtitle>받은 메세지가 없습니다.</v-card-subtitle>
                        </v-sheet>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<script>
    export default {
        name: "MessageBox",
        data() {
            return {
                sent_msg: [],
                received_msg: [],
                reply_content: '',
                login_user_id : sessionStorage.getItem("uid"),
            }
        },
        methods: {
            sendReply(received_id) { //답장보내기
                if (this.reply_content != '') {
                    axios.post('/accouts/sendmessage/' + received_id + '/', {
                            sender: this.login_user_id,
                            content: this.reply_content
                        })
                        .then(res => {
                            console.log("답장 보내기 성공")
                            alert('메세지가 전송되었습니다!')

                            console.log(res.data)
                        })
                        .catch(err => {
                            console.log("답장 보내기 실패")
                        })
                }
            },
            postIsRead(msg_id) {
                axios.get('/accouts/message_read/' + msg_id + '/')
                    .then(res => {
                        console.log("읽힘 표시 됨")
                    })
                    .catch(err => {
                        console.log("안읽힘")
                    })
            },
        },
        mounted() {
            axios.get('/accouts/message_list/' + sessionStorage.getItem("uid"))
                .then(res => {
                    this.sent_msg = res.data[1]
                    this.received_msg = res.data[0]
                    console.log("보낸메세지")
                    console.log(this.sent_msg)
                    console.log("받은메세지")
                    console.log(this.received_msg)
                    console.log("메세지함에서 메세지 읽어오기 완료")
                })
                .catch(err => {
                    console.log("메세지함에서 에러난다.")
                })
        }
    }
</script>

<style scoped>
    span {
        font-size: 16px;
        font-weight: bold;
    }

    .msg_card:hover {
        background-color: rgb(240, 240, 240);
    }
</style>

<style>
    tr {
        line-height: 3;
    }
</style>