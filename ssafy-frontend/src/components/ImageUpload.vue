<template>
  <div>
    
    <file-pond
        name="filepond"
        ref="pond"
        class-name="my-pond"
        allow-multiple="false"
        max-files="1"
        accepted-file-types="image/jpeg, image/png"
        v-bind:files="myFiles"
        v-on:init="handleFilePondInit"
        v-on:processfile="onload"
        :server="server"
        
    /><!--사용자가 파일 업로드를 되돌릴 수 있습니다 allowRevert = "true" --> 
    
  </div>
</template>

<script>
// Import FilePond
import vueFilePond from 'vue-filepond';

// Import FilePond styles
import 'filepond/dist/filepond.min.css'

// Import plugins
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type/dist/filepond-plugin-file-validate-type.esm.js';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.esm.js';

// Import styles
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css';

// Create FilePond component
const FilePond = vueFilePond( FilePondPluginFileValidateType, FilePondPluginImagePreview );
// FilePond.setOptions({
//     url: 'http://192.168.31.126:8000/fp',
//     process: './process/',
//     revert: './revert/',
//     restore: './restore/',
//     load: './load/',
//     fetch: './fetch/'
// });
export default{
    name: 'ImageUpload',
    data() {
        return { 
           myFiles: [],
           server: {
            //  'http://192.168.31.126:8000/api/v1'       
               url: this.$server + '/api/v1/',
                process: './process/',
                revert: './revert/',
                restore: './restore/',
                load: './load/',
                fetch: './fetch/',
           },
            userid:'1234',
           filenames:'',
         }
    },
    methods: {
        handleFilePondInit() {
            console.log('FilePond has initialized');
            // example of instance method call on pond reference
            // console.log("hello") 
            this.$refs.pond.getFiles()
            // console.log(this.$refs.pond.getFiles())
        },
        onload (e, r) {
            if(e){
              return console.log(e)
            }

            // console.log("error",r)
            this.filenames = r.serverId
            this.$emit('load_img', this.filenames)
            this.filenames = ''
        },
        create_waiting(){ 
          // 입력 받은 데이터를 모아 하나의 객체로 생성
          let wait = { 
            'name' : this.myFiles,
            'people': this.server,
          }
          console.log("wait")
          console.log(wait)
            this.$emit('create_wait', wait); // #하위 컴포넌트에서 상위컴포넌트로 데이터 전달
        },
    },
    components: {
        FilePond
    },
    watch:{
        myFiles(newQuestion){
            console.log("hihi")
            console.log("1")
            console.log(this.myFiles)
            console.log(this.server)
        }
    }

}
</script>