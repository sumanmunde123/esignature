<template>
  <div class="hello">
    <div>
              <!-- <Input type="textarea"  /> -->
     <textarea
      class="h-64 w-[220px]"
      v-model="htmlCode"
     id="textArea"
      placeholder="Enter your HTML code here..."
    ></textarea>
              </div>
    <div ref="pdfContainer"  id="pdfContainer" @dragover="onDragOver"
      @drop="onDrop">
              <iframe  :srcdoc="pdfContent"
  ref="pdfIframe"
  class="pdf-iframe"
  id="pdf-iframe"
  @dragover="onDragOver"
  @drop="onDrop"
  style="width: 100%; height: 100%;"></iframe>
            </div>
  </div>
</template>

<script>
import html2pdf from 'html2pdf.js';

export default {
  name: "HelloWorld",
  data:{
    pdfViewer: "TemplateForm",
      pdfInstance: null,
      htmlCode: "", // Store the HTML code entered by the user
      pdfContent: "",
  },
  methods: {
    async convertToPdf() {
      const htmlInput = document.getElementById('htmlInput');
      const pdfContainer = document.getElementById('pdfContainer');
      const pdfViewer = document.getElementById('pdfViewer');

      const pdfOptions = {
        margin: 10,
        filename: 'converted.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
      };

      const content = htmlInput.value;
      const pdf = await html2pdf().from(content).set(pdfOptions).outputPdf();

      // Display the PDF in the iframe
      pdfViewer.src = URL.createObjectURL(new Blob([pdf], { type: 'application/pdf' }));
    },
  },
  watch: {
    htmlCode: function (newHtmlCode) {
      // Update the iframe content whenever the user enters HTML code
      this.pdfContent = newHtmlCode;
    },
    
    printIframe(iframe) {
      const iframeWindow = iframe.contentWindow || iframe;
      iframeWindow.print();
    },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello{
  display:flex;
  flex-direction: column;
  align-items: center;
  column-gap:10%;
}
#htmlInput {
  border: 1px solid black;
  height: 400px;
  width: 300px;
}
#pdfContainer{
  border:1px solid red;
  height: 800px;
  width:600px;
}
</style>
