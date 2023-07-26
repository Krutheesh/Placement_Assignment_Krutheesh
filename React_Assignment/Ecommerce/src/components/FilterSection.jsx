import React from 'react'
import { mobile,laptop,computer,Accessories,watch,all } from '../Slice'
import { useDispatch } from 'react-redux'
function FilterSection() {
 const dispatch = useDispatch()
  console.log(mobile)
  return (
    <div>
      <div className='py-[2rem] '>
        <input type="text" placeholder='search' className='px-2 border-gray-600 border-2'/>
      </div>
        <div className='space-y-3 text-gray-600 '>
      <div className=' font-semibold text-gray-600'>
     Category
      </div>
      <div>
        <span onClick={() =>  dispatch(all())} className='cursor-pointer hover:border-b-2 hover:border-blue-500'>
          All
        </span>
      </div>

      <div>
      <span onClick={() =>  dispatch(mobile())} className='cursor-pointer hover:border-b-2 hover:border-blue-500'>
        Mobile
      </span>
      </div>
      <div>
      <span onClick={() =>  dispatch(laptop())} className='cursor-pointer hover:border-b-2 hover:border-blue-500'>
        Laptop
      </span>
      </div>
      
      <div>
      <span onClick={() =>  dispatch(computer())} className='cursor-pointer hover:border-b-2 hover:border-blue-500'>
      Computer
      </span>
      </div>

      <div>
      <span onClick={() =>  dispatch(Accessories())} className='cursor-pointer hover:border-b-2 hover:border-blue-500'>
      Accessories
      </span>
      </div>

      <div>
      <span onClick={() =>  dispatch(watch())} className='cursor-pointer hover:border-b-2 hover:border-blue-500'>
      Watch
      </span>
      </div>
    </div>

    <div className='space-y-3 text-gray-600 mt-[2rem]'>
      <div  className=' font-semibold text-gray-600'>
        <span>Company</span>
      </div>
      <div>
        <select name="" id="">
          <option value=""></option>
          <option value=""></option>
          <option value=""></option>
          <option value=""></option>

        </select>
      </div>
    </div>

    <div className='space-y-3 text-gray-600 mt-[2rem]'>
      <div  className=' font-semibold text-gray-600'>
        <span>Colors</span>
      </div>
    </div>

    <div className='space-y-3 text-gray-600 mt-[2rem]'>
      <div  className=' font-semibold text-gray-600'>
        <span>Price</span>
      </div>
    </div>
    </div>
    
  )
}

export default FilterSection
