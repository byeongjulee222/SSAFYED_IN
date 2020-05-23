<template>
<div id="board" class="hd_sz">
     <v-layout align-center justify-center row fill-height>
        <v-flex text-xs-center>
          <span class="display-2 font-weight-light">
            <slot name="text"/>
          </span>
        </v-flex>
      </v-layout>
</div>
    
</template>

<script>
export default {
    name: 'BoardBanner',
    props: {
        text : {type : String },
    }
}
</script>

<style scoped>
    #board {
        height: 350px;
        color: rgba(255,255,255,0.85);
    }

.container section.home {
  background: #2196f3;
}
.container section.about {
  background: #ffc107;
}
.container section.work {
  background: #4caf50;
}
.container section.contact {
  background: #f44336;
}
.container section h1 {
  margin: 0;
  font-size: 64px;
  transform: translate(0, 40vh);
  text-align: center;
  transition: transform 500ms;
  transform-style: preserve-3d;
}




</style>