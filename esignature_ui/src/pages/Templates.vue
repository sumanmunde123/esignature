<template>
    <div class=" flex h-full text-sm text-gray-700">
     <div><sidebar/> </div>
     <div class="mx-12  pt-10 flex flex-col  w-full">
     <!--first section-->
      <div class="flex justify-between">
        <div class="text-2xl font-semibold text-gray-900">Templates</div>
      </div>
       <!--end of first section-->
         <!--second section-->
         <div class="flex justify-between py-7">
          <Button
				icon-left="plus"
				label=" New Template"
				@click="newTemplate"
			/>
          
         
            <div class="flex items-center gap-2">
              <div class="w-32 flex"><button class="bg-gray-200 w-full px-7  py-2 h-8 text-[12px] mx-3 flex"> <div>filter</div></button></div>
            <div class="w-32 flex"><button class="bg-gray-200 w-full px-7 py-2  h-8 mx-3 text-[12px] flex">sort</button></div>
              <!-- <CompositeFilters />
              <Dropdown :options="['test']">
                <template #default>
                  <Button label="Sort">
                    <template #icon-left>
                      <IconSort class="mr-1.5 h-4 w-4" />
                    </template>
                  </Button>
                </template>
              </Dropdown> -->
            </div>
        
     
        </div>
         <!--end of second section-->
           <!--third section-->
           <div class="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 gap-4 py-5"  >
            <div  class="flex flex-col w-64" v-for="(item) in items" :key="item">
                <div class="border-solid border-2 rounded-md border-gray-400 w-64 h-32 flex flex-col justify-between my-4">
            <div class="h-24 mt-10 flex place-content-center">
              <div class="text-center">{{item.print_format}}</div>
            </div>
            <div class="flex flex-col bg-gray-200 h-24">
              <div class="text-center"> Based On : {{ item.based_on }}</div>
              <div class="flex place-content-end" >
             
              </div>
            </div>
          </div>
          <div class="flex place-self-center "><button class="bg-blue-600 text-white px-5 w-24 h-9 border-none rounded-md">Send</button></div>
            </div>
         
         </div>
         <!--end of third section-->
          
     </div>
   </div>
 </template>
 
 <script >
 import { Dialog , Dropdown, Input, FeatherIcon} from 'frappe-ui'
 import sidebar from '../components/sidebar.vue';


 export default {
   name: 'Templates',
   data() {
   return {
     items: [{status: 'Service Contract', color:'bg-orange-400', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'},{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}],  },{status: 'Low', color:'bg-orange-300', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}] }, {status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: 'High', color:'bg-orange-400', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'},{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}],  },{status: 'Low', color:'bg-orange-300', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}] }, {status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]}]
     
   }
 },
 methods: {
  newTemplate(event) {
      this.$router.push("/New-Templates-Form");
    },

},
   resources: {
     
   },
   components: {
     Dialog,
     sidebar,
     Input,
     Dropdown, 
     FeatherIcon, 
   },
   
 }
 </script>
 <script setup>
import { createResource } from 'frappe-ui'

let todos = createResource({
  url: '/api/method/frappe.client.get_list', 
  url: 'frappe.client.get_list', 
  params: {
     doctype: 'E-Signature Template',
     fields:['*']
  },
})
todos.fetch()
</script>

 