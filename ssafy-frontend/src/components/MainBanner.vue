<template>
<section class='section'>
    <div class='masthead-image' id='master-container'>
        <div class='content center'>
            <h1 id='master'>
              <div>SSAFYeedIn is</div>
              <div id='master-container-scroller'>
                <div class='master-container-scroller_item'>
                  <a class='cta-link'>Smart</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link'>Kind</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link' >Lovely</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link' >Sweet</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link' >Strong</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link' >Ambitious</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link' >Together</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link' >Enthusiastic</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link' >Friendly</a>
                </div>
                <div class='master-container-scroller_item'>
                  <a class='cta-link' >The Best</a>
                </div>
              </div>
              <!-- <div>Nice to see you</div> -->
            </h1>
        </div>
    </div>
</section>

</template>

<script>
import '../assets/css/mainbanner/mainbanner.css'

  export default {
    name: 'MainBanner',
    props: {
      imgSrc: {
        type: String
      },
      text: {
        type: String
      }
    },
    methods: {}
  }
</script>