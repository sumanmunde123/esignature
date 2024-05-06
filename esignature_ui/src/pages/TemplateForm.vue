<template>
  <div class="flex h-full text-gray-700">
    <div><sidebar /></div>
    <Filter />
    <div class="flex flex-col w-full">
      <!--first section-->
      <div class="flex">
        <div>
          <div
            class="flex pt-2 flex-col justify-between h-screen bg-white border border-gray-300 w-64"
          >
            <div class="px-3">
              <div>Name</div>
              <div><Input v-model="document_name"/></div>
            </div>
            <div class="px-3">
              <div>Based On</div>
              <div>
                <Input
                  type="select"
                  :options="['', 'Doctype', 'PDF Upload']"
                  v-model="basedOn"
                  required="1"
                />
              </div>
            </div>
            <div class="px-3" v-if="showDocumentType">
              <div>Document Type</div>
              <div>
                <Input type="select" :options="doctype.data" v-model="document_type" />
              </div>
            </div>

            <div class="px-3" v-if="showDocumentType">
              <div>Trigger On</div>
              <div>
                <Input
                  type="select"
                  :options="[
                    'New',
                    'Save',
                    'Submit',
                    'Cancel',
                    'Days After',
                    'Days Before',
                    'Value Change',
                    'Method',
                    'Custom',
                  ]"
                  v-model="document_type"
                />
              </div>
            </div>
            <div class="px-3">
              <div>Agreement Based On</div>
              <div>
                <Input
                  type="select"
                  :options="['', 'Print Format', 'HTML Format']"
                  v-model="agreeBasedOn"
                />
              </div>
            </div>
            <div v-if="showPrintFormat">
              <div class="px-3">
                <div>Print Format</div>
                <div>
                  <Input type="select" :options="formats.data" v-model="print_format" />
                </div>
              </div>
              <div class="px-3">
                <div>Document Name</div>
                <div>
                  <Input type="select" :options="docname.data" v-model="document_name" />
                </div>
              </div>
            </div>

            <div class="px-3" v-if="showHTML">
              <div>HTML Format</div>
              <div>
              <!-- <Input type="textarea"  /> -->
                <textarea
                class="h-64 w-[220px]"
      v-model="htmlCode"
     
      placeholder="Enter your HTML code here..."
    ></textarea>
              </div>
            </div>
            <div class="px-3 place-self-center" v-if="showPDF">
              <!-- <input type="file" @change="handleFileUpload" /> -->
              <UploadFile @fileUploaded="updateSelectedFile" />
              <input @change="loadPDF" type="file" id="pdfFileInput" accept="application/pdf" hidden/>
              <button id="upload" class="bg-blue-400 px-4 py-2 text-white rounded-md">
              <label for="pdfFileInput">Attach Pdf</label>
              </button>
            </div>
            <div class="px-3">
              <div>Condition</div>
              <div><Input type="textarea" class="h-64" /></div>
            </div>
          </div>
        </div>
        <div id="PdfSpace" class="flex justify-between w-full">
          <div id="insidePdfSpace">
            <div id="sideIcons">
              <div id="dragableIcons">
                <!-- <div class="dragicons"
      draggable="true">
                  <FeatherIcon name="zoom-in" class="h-6 w-6 mt-2 text-black-500" />
                 
                </div>
                <div class="dragicons" draggable="true">
                  <FeatherIcon name="zoom-out" class="h-6 w-6 mt-2 text-black-500" />
                </div> -->
                <div class="dragicons" draggable="true">
                  <FeatherIcon name="edit" class="h-5 w-5 ml-0.5 mt-2 text-black-500" />
                </div>
                <div class="dragicons" draggable="true">
                  <FeatherIcon
                    name="check-circle"
                    class="h-5 w-5 ml-0.5 mt-2 text-black-500"
                  />
                </div>
                <div class="dragicons" draggable="true">
                  <FeatherIcon name="edit-2" class="h-5 w-5 ml-0.5 mt-2 text-black-500" />
                </div>
                <div class="dragicons" draggable="true">
                  <FeatherIcon name="phone" class="h-5 w-5 ml-0.5 mt-2 text-black-500" />
                </div>
                <div class="dragicons" draggable="true">
                  <FeatherIcon
                    name="calendar"
                    class="h-5 w-5 ml-0.5 mt-2 text-black-500"
                  />
                </div>
                <div class="dragicons" draggable="true">
                  <FeatherIcon
                    name="clipboard"
                    class="h-5 w-5 ml-0.5 mt-2 text-black-500"
                  />
                </div>
                <div class="dragicons" draggable="true">
                  <FeatherIcon name="mail" class="h-5 w-5 mt-2 ml-0.5 text-black-500" />
                </div>
              </div>
            </div>

            <div ref="pdfContainer" id="pdfContainer"  @dragover="onDragOver"
      @drop="onDrop">
              <iframe :srcdoc="pdfContent" ref="pdfContainer" @dragover="onDragOver" @drop="onDrop" style="width: 100%; height: 100%;"></iframe>
            </div>
            <div class="popup" v-show="popupVisible">
      <input
        type="text"
        v-model="description"
        placeholder="Enter description"
      />
      <button id="popupSave" @click="saveDescription">Save</button>
      <button id="popupClose" @click="closePopup">Close</button>
    </div>
  
          </div>
          <div>
          
            <AppToolbar/>
          </div>
          <div id="pdfSaveBtn" class="flex mx-auto my-20">
            <button
              class="bg-blue-400 h-8 px-9 text-white mx-5 my-3 text-center rounded-md"
              @click="newTemplate"
            >
              Save
            </button>
            <!-- <div v-html="html_content.data"></div> -->

            <div class="displayData">
            width:{{  initialWidth }} 
            <br/> height: {{ initialHeight}}
            <br/> X-Axis: {{ startX}} 
            <br/> Y-Axis:{{startY }} 
            </div>
          </div>
        </div>
      </div>
      <!--end of first section-->
    </div>
  </div>
</template>

<script>
import { Dialog, Dropdown, Input, FeatherIcon, TextEditor } from "frappe-ui";
import sidebar from "../components/sidebar.vue";
import AppToolbar from "../components/templates/side_tool_bar.vue";
import { inject, ref } from "vue";
import UploadFile from "../components/fileuploader.vue";
import TemplatesSideBarMenu from "../components/templates/templates_sidebar.vue";
let formats = ref([]);
let docname = ref([]);
let html_content = ref("");

export default {
  name: "TemplatesForm",
  components: {
    Dialog,
    sidebar,
    Input,
    Dropdown,
    FeatherIcon,
    TextEditor,
    TemplatesSideBarMenu,
    AppToolbar,
    UploadFile,
  },

  data() {
    return {
      name: "",
      basedOn: "",
      document_type: "",
      document_name: "",
      triggerOn: "",
      agreeBasedOn: "",
      print_format: "",
      condition: "",
      pdfViewer: "TemplateForm",
      pdfInstance: null,
      htmlCode: "", // Store the HTML code entered by the user
      pdfContent: "",

      draggableItems: ["1", "2"],
      popupVisible: false,
      description: "",
      currentChild: null,
      resizingChild: null,
      initialWidth: 0,
      initialHeight: 0,
      startX: 0,
      startY: 0,
    };
  },
  props: {},


  computed: {},
  methods: {
    async loadPDF(event) {
      const selectedFile = event.target.files[0];

      if (selectedFile && selectedFile.type === "application/pdf") {
        const fileReader = new FileReader();

        fileReader.onload = async () => {
          const arrayBuffer = fileReader.result;

          // Load the PDF.js worker and library
          const pdfjsLib = await import('pdfjs-dist/build/pdf');

          pdfjsLib.GlobalWorkerOptions.workerSrc = `https://cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version}/pdf.worker.js`;

          // Store the reference within the async function
          const pdfContainer = this.$refs.pdfContainer;
          pdfContainer.innerHTML = "";

          pdfjsLib.getDocument({ data: arrayBuffer }).promise.then((pdf) => {
            this.pdfInstance = pdf;
            for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
              pdf.getPage(pageNum).then((page) => {
                const canvas = document.createElement("canvas");
              
                pdfContainer.appendChild(canvas); // Use the stored reference here

                const viewport = page.getViewport({ scale: 1.5 });
                canvas.width = viewport.width;
                canvas.height = viewport.height;

                const canvasContext = canvas.getContext("2d");
                const renderContext = {
                  canvasContext,
                  viewport
                };

                page.render(renderContext);

                // Enable text annotation on canvas click
                canvas.addEventListener("click", (e) => {
                  const rect = canvas.getBoundingClientRect();
                  const x = e.clientX - rect.left;
                  const y = e.clientY - rect.top;

                  const text = prompt("Enter your text:");
                  if (text) {
                    canvasContext.font = "16px Arial";
                    canvasContext.fillText(text, x, y);
                  }
                });
              });
            }
          });
        };

        fileReader.readAsArrayBuffer(selectedFile);
      } else {
        alert("Please select a valid PDF file.");
      }
    },    
    newTemplate(event) {
      this.$router.push("/Templates");
    },

 // drag Drop code 
    onDragOver(event) {
      event.preventDefault(); // Allow dropping
    },
    onDrop(event) {
      event.preventDefault();

      const dataV = event.dataTransfer.getData("text/plain");
      const draggedElement = document.getElementById(dataV);

      // Create a new child div in the container
      const childDiv = document.createElement("div");
      childDiv.classList.add("draggableChild");
      childDiv.style.width = "100px"; // Set initial width
      childDiv.style.height = "100px"; // Set initial height

      // Position the child div where it was dropped
      childDiv.style.left =
        event.clientX -
        this.$refs.pdfContainer.getBoundingClientRect().left +
        "px";
      childDiv.style.top =
        event.clientY - this.$refs.pdfContainer.getBoundingClientRect().top + "px";
      

      // Append the child div to the container
      this.$refs.pdfContainer.appendChild(childDiv);

      // Add event listener to enable resizing
      childDiv.addEventListener("mousedown", (e) => {
        this.resizingChild = childDiv;
        this.initialWidth = childDiv.offsetWidth;
        this.initialHeight = childDiv.offsetHeight;
        this.startX = e.clientX;
        this.startY = e.clientY;
        e.preventDefault();
        console.log("positionX:",e.clientX);
          console.log("positionY:",e.clientY);
      });

      // Add event listener to open the popup when clicking the child div
      childDiv.addEventListener("click", (e) => {
        this.openPopup(childDiv, e);
      });
    },





    openPopup(childDiv, e) {
      this.currentChild = childDiv;
      this.description = this.currentChild.innerHTML;
      this.popupVisible = true;
      this.$nextTick(() => {
        const popup = document.querySelector(".popup");
        popup.style.left = e.pageX + "px";
        popup.style.top = e.pageY + "px";
        
      });
    },
    saveDescription() {
      if (this.currentChild) {
        const newText = this.description;
        this.currentChild.innerHTML += "<br>" + newText;
        this.currentChild.style.border = 'none';
        this.currentChild.style.background = 'none'
      }
      this.popupVisible = false;
    },
    closePopup() {
      this.popupVisible = false;
    },
    resizeChild(e) {
      if (!this.resizingChild) return;
      const width = this.initialWidth + (e.clientX - this.startX);
      const height = this.initialHeight + (e.clientY - this.startY);
      this.resizingChild.style.width = width + "px";
      this.resizingChild.style.height = height + "px";
       console.log("sizeX",e.clientX);
       console.log("sizeY",e.clientY);
       console.log("width:", width)
       console.log("height:", height)

    },

  
  
  },
  mounted() {
    // Event listeners for resizing
    window.addEventListener("mousemove", this.resizeChild);
    window.addEventListener("mouseup", () => {
      this.resizingChild = null;
    });
  },

  resources: {},
  watch: {

    
    document_name: async function (val) {
      this.document_name = val;
      this.document_type = this.document_type;
      let html = createResource({
        url: "/api/method/esignature_app.api.get_preview",
        params: {
          doctype: this.document_type,
          document_name: this.document_name,
          print_format: this.print_format,
        },
      });
      await html.fetch();
      html_content.value = html;
      console.log("data:", html_content);
    },
    document_type: async function (val) {
      this.document_type = val;
      let documents = createResource({
        url: "/api/method/esignature_app.api.get_doctypes_names",
        params: { doctype: this.document_type },
      });
      await documents.fetch();
      docname.value = documents;

      let print_formats = createResource({
        url: "/api/method/esignature_app.api.get_print_formats",
        params: { doctype: this.document_type },
      });
      await print_formats.fetch();
      formats.value = print_formats;
    },
    htmlCode: function (newHtmlCode) {
      // Update the iframe content whenever the user enters HTML code
      this.pdfContent = newHtmlCode;
    },
    
    printIframe(iframe) {
      const iframeWindow = iframe.contentWindow || iframe;
      iframeWindow.print();
    },
    // document_type: function(){

    // }
  },
  computed: {
    showDocumentType() {
      return this.basedOn == "Doctype";
    },
    showPDF() {
      return this.basedOn == "PDF Upload";
    },

    showTrigger(e) {
      return this.document_type !== "";
    },
    showPrintFormat() {
      return this.agreeBasedOn == "Print Format";
    },
    showHTML() {
      return this.agreeBasedOn == "HTML Format";
    },
    showDocname() {
      return this.print_format != "";
    },
  },

  setup() {},
};
</script>
<script setup>
import { createResource } from "frappe-ui";
import { reactive, watch } from "vue";

const state = reactive({
  name: "",
  basedOn: "",
  document_type: "",
  document_name: "",
  triggerOn: "",
  agreeBasedOn: "",
  print_format: "",
  condition: "",
  htmlcontent: "",
});

let print_format = createResource({
  url: '/api/method/esignature_app.api.get_print_formats',
  params:
  {

  },

})
print_format.fetch()
let doctype = createResource({
  url: "/api/method/esignature_app.api.get_doctypes",
});
doctype.fetch();
let get_preview = createResource({
  url: "/api/method/esignature_app.api.get_preview",
  
});
get_preview.fetch();
</script>
<style>
#PdfSpace {
  border: 1px solid black;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  margin: 0;
  padding: 0;
}
#insidePdfSpace {
  border: 1px solid red;
  margin: 0;
  width: 75%;
  padding: 0;
  display: flex;
  position: relative;
}
#sideIcons {
  margin: 0;
  padding: 0;
  width: 10%;
  height: 100%;
  border: 1px solid teal;
 
}
#pdfSaveBtn {
  border: 1px solid black;
  margin: 0;
  height: 100%;
  width: 25%;
}
#pdfSaveBtn > button {
  margin-left: 30%;
}
#dragableIcons {
  height: 40%;
  width: 40%;
  margin-left: 10%;
  margin-top: 10%;
}
.dragicons {
  border: 1px solid gray;
  width: 100%;
  height: 11.28%;
  color: black;
  font-weight: bold;
  padding-left: 14%;
  border-radius: 5%;
}

#pdfContainer {
  border: 1px solid greenyellow;
  height: 100%;
  width: 90%;
  margin: 0%;
  padding: 0%;  
  
}

canvas{
  width: 100%;
  height: 100%;
  
}


.popup {
  display: block;
  position: absolute;
  background-color: white;
  border: 1px solid #ccc;
  /* margin-right: 40px; */
  padding: 10px;
  margin-left: -40%;
  z-index: 1;
  width: 300px;
  resize: both;
  overflow: auto;
  
}
.popup>input{
  height: 150px;
  width: 100%;
  color: black;
  font-weight: bold;
}
.draggableChild {
  position: absolute;
  border: 1px dashed black;
  resize: both;
  color: black;
  font-weight: normal;
  line-height: 9px;
  overflow: auto;
}

#popupSave{
  background-color: black;
  color: white;
  width: 60px;
  margin-top: 10px;
  border-radius: 5px;
  height: 30px;
}

#popupClose{
  background-color: black;
  color: white;
  width: 60px;
  margin-top: 10px;
  border-radius: 5px;
  height: 30px;
  margin-left: 10px;
}

.displayData{
  border: 1px solid #000;
  width: 224px;
    height: 196px;
    margin-top: 20%;
    margin-left: -57%;
}


</style>
