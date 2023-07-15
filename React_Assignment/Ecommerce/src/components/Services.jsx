import React from 'react'
import { TbTruckDelivery} from "react-icons/tb";
import {MdSecurity} from "react-icons/md"
import {GiReceiveMoney} from "react-icons/gi"
function services() {
  return (
    <div className='md:flex-row flex flex-col justify-between items-center md:space-y-0 space-y-5'>
      <div className='bg-[#f2e6ff] p-3 h-[15rem] w-[18rem] rounded-xl flex justify-center items-center'>
         <div className='space-y-3'>
         <div >
         <TbTruckDelivery className='text-[#703fa1] m-auto text-[3rem] bg-white p-3 rounded-xl'/>
         </div>
          <div>Lorem ipsum dolor sit amet.</div>
         </div>
      </div>


    <div className='flex flex-col justify-between h-[15rem] w-[18rem]'>
      <div  className='bg-[#f2e6ff] p-3 h-[7rem] w-[18rem] rounded-xl flex justify-center items-center'>
      <div className='flex items-center justify-between space-x-5'>
          <span><MdSecurity className='text-[#703fa1] m-auto text-[2.5rem] bg-white p-3 rounded-xl'/></span>
          <div>Lorem ipsum dolor sit amet.</div>
      </div>
      </div>
      <div className=' bg-[#f2e6ff] p-3 h-[7rem] w-[18rem] rounded-xl flex justify-center items-center'>
      <div className='flex items-center justify-between space-x-5'>
        <span><GiReceiveMoney className='text-[#703fa1] m-auto text-[2.5rem] bg-white p-3 rounded-xl'/></span>
        <div>Lorem ipsum dolor sit amet.</div>

      </div>
      </div>
    </div>



    <div className='bg-[#f2e6ff] p-3 h-[15rem] w-[18rem] rounded-xl flex justify-center items-center'>
         <div className='space-y-3' >
         <div><TbTruckDelivery className='text-[#703fa1] m-auto text-[3rem] bg-white p-3 rounded-xl'/></div>
          <div>Lorem ipsum dolor sit amet.</div>
         </div>
      </div>
      
    </div>
  )
}

export default services
