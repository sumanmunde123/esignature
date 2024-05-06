<template>
  <div
    class="flex pt-2 flex-col justify-evenly h-screen bg-white border border-gray-300 w-64"
  >
    <div class="px-3">
      <div>{{ doctype.data }}</div>
      <div>Name :{{ doctype.data }}</div>
      <div><Input type="text" required v-model="signData.name" /></div>
      <!-- <div><Input type="select" :options="doctype.data" v-model="document_name" /></div> -->
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
      <div><Input type="select" :options="doctype.data" v-model="document_type" /></div>
    </div>
    <div class="px-3">
      <div>Document Name</div>
      <!-- <div><Input type="select" :options="[]" v-model="document_name" /></div> -->
      <div><Input type="select" :options="doctype.data" v-model="document_name" /></div>
    </div>
    <div class="px-3" v-if="showTrigger">
      <div>Trigger On</div>
      <!-- <div><Input type="select" :options="[
                'New',
                'Save',
                'Submit',
                'Cancel',
                'Days After',
                'Days Before',
                'Value Change',
                'Method',
                'Custom',]"/></div> -->
      <div><Input type="select" :options="formats.data" /></div>
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
    <div class="px-3" v-if="showPrintFormat">
      <div>Print Format</div>
      <div><Input type="select" :options="formats.data"  /></div>
    </div>
    <div class="px-3">
      <div>HTML Format</div>
      <div><Input type="textarea" class="h-64" /></div>
    </div>
    <div class="px-3 place-self-center">
      <UploadFile />
     
    </div>
    <div class="px-3">
      <div>Condition</div>
      <div><Input type="textarea" class="h-64" /></div>
    </div>
  </div>
</template>

<script>
import { Dropdown, FeatherIcon, Input } from "frappe-ui";
import UploadFile from "../fileuploader.vue";

import { inject, ref } from "vue";

let formats = ref([]);
let docname = ref([]);

export default {
  name: "TemplatesSideBarMenu",
  components: {
    Dropdown,
    FeatherIcon,
    Input,
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
    };
  },

  props: {
    print_format: {
      type: String,
    },
  },
  methods: {
  },

  watch: {
    document_type: function () {
      let print_formats = createResource({
        url: "/api/method/esignature_app.api.get_print_formats",
        params: { doctype: this.document_type },
      });
      let documents = createResource({
        url: "/api/method/esignature_app.api.get_doctypes_names",
        params: { doctype: this.document_type },
      });
      print_formats.fetch();
      documents.fetch();
      formats.value = print_formats;
      docname.value = documents;
    },
  },
  computed: {
    showDocumentType() {
      return this.basedOn == "Doctype";
    },
    showTrigger() {
      return this.document_type !== "";
    },
    showPrintFormat(Doctype) {
      console.log("doctype", Doctype);
      return this.agreeBasedOn == "Print Format";
    },
  },
  
  setup() {},
  mounted() {},
};
</script>
<script setup>
import { createResource, createListResource, Input } from "frappe-ui";
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

const signData = createListResource({
  doctype: "E-Signature Template",
  fields: ["name", "Status", "Based On", "Document Type"],
  filters: {
    status: "Save",
  },
});
signData.reload();

let print_format = createResource({
  url: "/api/method/esignature_app.api.get_print_formats",
  params: { doctype: this.print_format },
});
print_format.fetch();

let doctype = createResource({
  url: "/api/method/esignature_app.api.get_doctypes",
});
doctype.fetch();

let get_preview = createResource({
  url: "/api/method/esignature_app.api.get_preview",
});
get_preview.fetch();
</script>
