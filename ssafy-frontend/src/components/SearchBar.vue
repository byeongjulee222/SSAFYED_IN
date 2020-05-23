<template>
    <div class="search-bar">
        <!-- -->
        <v-form @submit.prevent="createSearch" class=" input-group">
            <v-toolbar class="my-6 mx-8" flat max-width="400">
                <v-text-field v-model="searchtext" type="text" hide-details single-line placeholder="찾으시는 내용을 검색하세요">
                </v-text-field>
                <v-btn text icon color="light-blue" type="submit">
                    <v-icon>search</v-icon>
                </v-btn>
                <v-btn icon color="light-blue" @click.prevent="deleteSearch">
                    <v-icon>clear</v-icon>
                </v-btn>
            </v-toolbar>
        </v-form>
    </div>
</template>

<script>
    export default {
        name: 'SearchBar',
        data() {
            return {
                searchtext: '',
            }
        },
        methods: {
            createSearch() {
                this.$emit('create_search', this.searchtext)
                // this.searchtext = ''
            },
            deleteSearch() {
                this.searchtext = ''
                this.$emit('create_search', this.searchtext)

            }
        },
        mounted() {
            this.createSearch()
            this.deleteSearch()
        }

    }
</script>