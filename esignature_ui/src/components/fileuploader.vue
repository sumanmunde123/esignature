<template>
  <!-- <FileUploader file-types="pdf" @success="(file) => handleFile(file)">
      <template
        v-slot="{
          file,
          uploading,
          progress,
          uploaded,
          message,
          error,
          total,
          success,
          openFileSelector,
        }"
      >
        <div class="w-full text-center">
          <button id="upload" class="bg-blue-400 px-4 py-2 text-white rounded-md" @click="openFileSelector" :loading="uploading">
            {{ uploading ? `Uploading ${progress}%` : 'Attach Pdf' }}
            Attach Pdf
            <input type="file" @change=""  hidden/>
          </button>
          <ErrorMessage class="mt-2" :message="error" />
        </div>
      </template>
    </FileUploader>   -->

  <div class="w-full text-center" @click="updateSelectedFile">
    
<!-- 
    <button id="upload" class="bg-blue-400 px-4 py-2 text-white rounded-md">
      <label for="uploader">Attach Pdf</label>
    </button> -->
  </div>
</template>

<script>
export default {
  name: "UploadFile",
 
  methods: {
    handleFileChange(event) {
      const selectedFile = event.target.files[0];
      this.$emit('file-selected', selectedFile);
     
    },
  },
 
  setup() {},
  mounted() {},
};
</script>
<script setup>
import { FileUploader, Button } from "frappe-ui";
</script>
