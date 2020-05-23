<template>
    <div id="body">
        <v-list>
            <v-list-item>
                <v-list-item-content v-if="!login_flag">
                    <v-col cols="3">
                        <v-list-item-avatar size="80" class="mt-5">
                            <v-img src="../assets/no_picture.png"></v-img>
                        </v-list-item-avatar>
                    </v-col>
                    <v-col cols="9">
                        <v-list-item-title class="title">로그인해주세요</v-list-item-title>
                        <v-list-item-subtitle class="subtitle-2 mt-3"> 회원인증시에만만 사용 가능합니다.</v-list-item-subtitle>
                    </v-col>
                </v-list-item-content>

                <v-list-item-content v-else>
                    <v-col cols="3">
                        <v-list-item-avatar size="80" class="mt-5">
                            <v-img :src="user.profile_img"></v-img>
                        </v-list-item-avatar>
                    </v-col>
                    <v-col cols="9">
                        <v-list-item-title class="title">{{ user.nickname }}</v-list-item-title>
                        <v-list-item-subtitle class="subtitle-2 mt-3">로그아웃하기</v-list-item-subtitle>
                    </v-col>
                </v-list-item-content>
            </v-list-item>


            <v-divider></v-divider>

            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class=" title">프로필수정</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="title">마이페이지</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="title">나의 포트폴리오</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="title">내가 작성한 글</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

        </v-list>
    </div>
</template>
<script>
    export default {
        name: 'ProfileMobile',
        data() {
            return {
                login_flag: false,
            }
        },
    }
</script>