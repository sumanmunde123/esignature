<template>
   <div class=" flex h-full  text-gray-700">
    <div><sidebar/></div>
    <div class="mx-12  pt-10 flex flex-col  w-full">
      <!--first section-->
      <div class="flex justify-between">
        <div class="text-2xl font-semibold text-gray-900">Dashboard</div>
        <Button
        icon-left="plus"
        label=" New Document"
        
      />
      </div>
       <!--end of first section-->
        <!--second section-->
        <div class="flex justify-between">
          <div class="w-96 flex py-5  justify-between ">
            <div class="flex bg-gray-100 w-64 mx-4"><div class="w-32 px-2">All Documents</div><Dropdown :options="[{ label: 'Logout', handler: () => alert('New File') },{ label: 'Settings' }, ]" :button="{ label: 'Drop', icon: 'chevron-down' }"/></div>
              <div class="flex bg-gray-100 mx-4"><div class="w-32 px-2">Status</div><Dropdown :options="[{ label: 'Logout', handler: () => alert('New File') },{ label: 'Settings' }, ]" :button="{ label: 'Drop', icon: 'chevron-down' }"/></div>
                <div class="flex bg-gray-100 mx-4"><div class="w-32 px-2">Priority</div><Dropdown :options="[{ label: 'Logout', handler: () => alert('New File') },{ label: 'Settings' }, ]" :button="{ label: 'Drop', icon: 'chevron-down' }"/></div>
          </div>
          <div class="flex w-64 py-2 justify-between">
            <div class="w-32 flex"><button class="bg-gray-200 w-full px-7  py-2 h-8 text-[12px] mx-3 flex"> <FeatherIcon name="align-center" stroke-width="1" class="h-5 w-5 text-gray-500 " /><div>filter</div></button></div>
            <div class="w-32 flex"><button class="bg-gray-200 w-full px-7 py-2  h-8 mx-3 text-[12px] flex"><FeatherIcon name="align-center" stroke-width="1" class="h-5 w-5 text-gray-500 " />sort</button></div>
          </div>

        </div>
         <!--end of second section-->

         <!--third section-->
         <div class="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 gap-4 py-5"  >
          <div class="border-solid border-2 rounded-md border-gray-400 w-64 h-32 flex flex-col justify-between my-4" v-for="(item) in items" :key="item">
            <div class="h-24 flex place-content-end">
              <div :class="`${item.color} mx-3 px-3 my-2 text-center h-7 w-16 border-none rounded-md`">{{ item.status }}</div>
            </div>
            <div class="flex flex-col bg-gray-200 h-24">
              <div class="text-center">{{ item.document }}</div>
              <div class="flex place-content-end" >
                <div class="px-2" v-for="(value, index) in item.document_signatories" :key="index"><img class="" :src="`${value.src}`"></div>
              </div>
            </div>
          </div>
         </div>
         <!--end of third section-->
         
    </div>
  </div>
</template>

<script>
import { Dialog , Dropdown, Input, FeatherIcon} from 'frappe-ui'
import sidebar from '../components/sidebar.vue';

export default {
  name: 'Home',
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
