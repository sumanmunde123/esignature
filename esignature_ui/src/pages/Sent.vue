<template>
    <div class=" flex h-full text-gray-700">
     <div><sidebar/></div>
     <div class="mx-12  pt-10 flex flex-col  w-full">
       <!--first section-->
       <div class="flex justify-between">
        <div class="text-2xl font-semibold text-gray-900">Sent</div>
      </div>
       <!--end of first section-->
          <!--second section-->
          <div class="flex justify-between">
          <div class="w-96 flex py-5  justify-between ">
              <div class="flex bg-gray-100 mx-4"><div class="w-32 px-2">Status</div><Dropdown :options="[{ label: 'Logout', handler: () => alert('New File') },{ label: 'Settings' }, ]" :button="{ label: 'Drop', icon: 'chevron-down' }"/></div>
                <div class="flex bg-gray-100 mx-4"><div class="w-32 px-2">Priority</div><Dropdown :options="[{ label: 'Logout', handler: () => alert('New File') },{ label: 'Settings' }, ]" :button="{ label: 'Drop', icon: 'chevron-down' }"/></div>
          </div>
        

        </div>
         <!--end of second section-->
          
     </div>
   </div>
 </template>
 
 <script>
 import { Dialog , Dropdown, Input, FeatherIcon} from 'frappe-ui'
 import sidebar from '../components/sidebar.vue';
 
 export default {
   name: 'Sent',
   data() {
   return {
     items: [{status: 'High', color:'bg-orange-400', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'},{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}],  },{status: 'Low', color:'bg-orange-300', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}] }, {status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: 'High', color:'bg-orange-400', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'},{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}],  },{status: 'Low', color:'bg-orange-300', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}] }, {status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]},{status: '', color:'', document:'Sales Order', document_signatories : [{src:'../../public/Male User.png'}, {src:'../../public/Male User.png'}]}]
     
   }
 },
   resources: {
     
   },
   components: {
     Dialog,
     sidebar,
     Input,
     Dropdown, 
     FeatherIcon
     
   },
 }
 </script>
 