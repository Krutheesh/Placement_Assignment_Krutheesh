import React, { useState } from 'react'
import { mobile,laptop,computer,Accessories,watch,all,companies,rcolors,maxPrice } from '../Slice'
import { useSelector,useDispatch } from 'react-redux'
function FilterSection() {
 const dispatch = useDispatch()
const products = useSelector( (state) => state.ecom.products)
const price = useSelector((state) => state.ecom.price)
let maxprice = products.map((value) => value.price)

maxprice.sort((a,b) => a-b)

maxprice = maxprice[maxprice.length-1]



let colarr= []

products.map(ele => {
  colarr = colarr.concat(ele.colors)
  
})
console.log(colarr)
colarr = colarr.filter((val,index,arr) => arr.indexOf(val) === index)
console.log(colarr)



let company = []
products.map(ele => {
  company.push(ele.company)
})
company = company.filter((val,index,array) => array.indexOf(val) === index)
console.log(company)

const companyHandler = (e) => {
  console.log(e.target.value)
  if(e.target.value === 'all'){
    dispatch(all())
  }
  else{
    dispatch(companies(e.target.value))
  }
   
}
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
        <select name="" id="" onChange={companyHandler}>
          <option value='all'>all</option>
          {
              company.map((ele,index) => {
                return (<option key={index} value={ele} >{ele}</option>)
              })
              
          }
          
          
        </select>
      </div>
    </div>

    <div className='space-y-3 text-gray-600 mt-[2rem]'>
      <div  className=' font-semibold text-gray-600'>
        <span>Colors</span>
      </div>
      <div className='flex  items-center space-x-1'>
        <div className='cursor-pointer' onClick={() => dispatch(all())}>all</div>
        {
        
          colarr.map((ele,index) => {
            return (
              <button key={index} type='button' onClick={(e) => {dispatch(rcolors(e.target.value))}} className={`bg-[${ele}] w-[1rem] h-[1rem] rounded-xl cursor-pointer `} value={ele} />
            )
          })
        }
      </div>
    </div>

    <div className='space-y-3 text-gray-600 mt-[2rem]'>
      <div  className=' font-semibold text-gray-600'>
        <div>Price</div>
        <span>{price}</span>
      </div>
      <div>
        <input type="range" min="0" max={maxprice} value={price} onChange={(e) =>{
          dispatch(maxPrice(e.target.value))
        }}/>
      </div>
    </div>

    <div className='mt-6'>
      <button className='bg-orange-600 text-white p-2' onClick={() => dispatch(all())}>
        Reset Filter
      </button>
    </div>
    </div>
    
  )
}

export default FilterSection
