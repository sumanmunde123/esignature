<template>
    <div class="flex h-full text-gray-700">
      <div><sidebar /></div>
      <Filter />
      <div class="flex flex-col w-full">
        <!--first section-->
        <div class="flex">
          <div>
            <div
              class="flex pt-2 flex-col justify-between h-screen bg-white border border-gray-300 w-64" > 
              <div class="px-3 place-self-center">
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
                  <div id="draged-div" class="dragicons"
        draggable="true">
                    <FeatherIcon name="zoom-in" class="h-6 w-6 mt-2 text-black-500" />
                   
                  </div>
                  <div id="draged-div-sign" class="dragicons" draggable="true">
                    <FeatherIcon name="zoom-out" class="h-6 w-6 mt-2 text-black-500" />
                  </div>
                  <div id="draged-div-check" class="dragicons" draggable="true">
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
                <iframe :srcdoc="pdfContent" ref="pdfContainer" id="pdfContainer"  style="width: 100%; height: 100%;"></iframe>
              </div>
              <div class="popup" v-show="popupVisible">
        <input
          type="text"
          v-model="description"
          placeholder="Enter description"
          
        />
        <canvas  ref="drawingCanvas" id="drawingCanvas" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing">Enter Your Signature Here</canvas>
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
              <div v-html="html_content.data"></div>
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

        drawingCanvas: null,
    drawingContext: null,
    drawing: false,
   
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

      clearDrawingCanvas() {
    this.drawingContext.clearRect(0, 0, this.drawingCanvas.width, this.drawingCanvas.height);
  },
  
      openPopup(childDiv, e) {
        this.currentChild = childDiv;
        this.currentElementId = childDiv.id;
        this.description = this.currentChild.innerHTML;
        this.clearDrawingCanvas();
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
          this.currentChild.style.background = 'none';
        }
        this.popupVisible = false;
      },
      closePopup() {
        this.popupVisible = false;
      },
      resizeChild(e) {
        if (!this.resizingChild) return;  function openDrawingPopup(resizableDiv) {
            const drawingPopup = document.getElementById("drawing-popup");
            drawingPopup.style.display = "block";

            const drawingCanvas = document.getElementById("drawing-canvas");
            const drawingSaveBtn = document.getElementById("drawing-save");
            const drawingCancelBtn = document.getElementById("drawing-cancel");

            const ctx = drawingCanvas.getContext("2d");
            let isDrawing = false;
            let lastX = 0;
            let lastY = 0;

            // Display existing content in the drawing canvas
            const existingImage = resizableDiv.querySelector("img");
            if (existingImage) {
                const img = new Image();
                img.src = existingImage.src;
                img.onload = function () {
                    ctx.drawImage(img, 0, 0);
                };
            }

            // Start drawing
            drawingCanvas.addEventListener("mousedown", (e) => {
                isDrawing = true;
                [lastX, lastY] = [e.offsetX, e.offsetY];
            });

            // Continue drawing
            drawingCanvas.addEventListener("mousemove", (e) => {
                if (!isDrawing) return;
                ctx.strokeStyle = "black";
                ctx.lineWidth = 2;
                ctx.lineJoin = "round";
                ctx.lineCap = "round";

                ctx.beginPath();
                ctx.moveTo(lastX, lastY);
                ctx.lineTo(e.offsetX, e.offsetY);
                ctx.stroke();

                [lastX, lastY] = [e.offsetX, e.offsetY];
            });

            // Stop drawing
            drawingCanvas.addEventListener("mouseup", () => {
                isDrawing = false;
            });
           
            // Save button click event
            drawingSaveBtn.addEventListener("click", function () {
                const drawingDataURL = drawingCanvas.toDataURL();
                // Append the new content to the resizable div
                resizableDiv.innerHTML += `<img src="${drawingDataURL}" alt="Drawing">`;
                drawingPopup.style.display = "none";
            });

            // Cancel button click event
            drawingCancelBtn.addEventListener("click", function () {
                drawingPopup.style.display = "none";
            });
        }

        const width = this.initialWidth + (e.clientX - this.startX);
        const height = this.initialHeight + (e.clientY - this.startY);
        this.resizingChild.style.width = width + "px";
        this.resizingChild.style.height = height + "px";
         console.log("sizeX",e.clientX);
         console.log("sizeY",e.clientY);
  
      },
      startDrawing(event) {
    this.drawing = true;
    const canvas = this.$refs.drawingCanvas;
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    this.drawingContext.beginPath();
    this.drawingContext.moveTo(x, y);
  },

  draw(event) {
    if (!this.drawing) return;

    const canvas = this.$refs.drawingCanvas;
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    this.drawingContext.lineTo(x, y);
    this.drawingContext.stroke();
  },

  stopDrawing() {
    this.drawing = false;
  },

  saveDescription() {
    if (this.currentChild) {
      const newText = this.description;
      const drawingDataUrl = this.drawingCanvas.toDataURL(); // Convert drawing to data URL
      this.currentChild.innerHTML += `${newText}<img id="drawSign" src="${drawingDataUrl}" alt="Drawing"/>`;
      this.currentChild.style.border = 'none';
      this.currentChild.style.background = 'none';
    }
    this.popupVisible = false;
    
  },
  
    
    
    },
    mounted() {
      // Event listeners for resizing
      window.addEventListener("mousemove", this.resizeChild);
      window.addEventListener("mouseup", () => {
        this.resizingChild = null;
      });

      // Initialize drawing canvas context
  this.drawingCanvas = this.$refs.drawingCanvas;
  this.drawingContext = this.drawingCanvas.getContext("2d");
  this.drawingContext.strokeStyle = "black";
  this.drawingContext.lineWidth = 2;
    },
  
    resources: {},
    watch: {
  
    
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
    overflow: auto;
    line-height: 7px;
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
  #drawingCanvas{
    border: 1px dashed black;

  }
  #drawSign{
    width: 100%;
    height: 62%;
  }
  </style>
  