<template>
        <!--페이지업 버튼-->
    <button type="button" aria-label="Scroll to top" title="Scroll to top" @click="scrollToTop"
      class="v-btn v-btn--bottom v-btn--contained v-btn--fab v-btn--fixed v-btn--right v-btn--round theme--dark v-size--large grey"
      style="transform-origin: center center;"><span class="v-btn__content"><i aria-hidden="true"
          class="v-icon notranslate mdi mdi-chevron-up theme--dark"></i></span></button>
</template>

<script>
export default {
    name : 'ScarollToTop',
    data() {
        return {
        }
    },
    methods: {
    scrollToTop() {
        window.scrollTo(0, 0);
      }
    }
}
</script>