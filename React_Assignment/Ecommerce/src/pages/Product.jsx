import React from 'react'
import FilterSection from '../components/FilterSection'
import ProductList from '../components/ProductList'
import Sort from '../components/Sort'

function Product() {
  
  return (
    <div>
      
     <div className=' px-[10rem] flex '>

      <div className='w-[30%]'>
        <FilterSection/>
      </div>

      <div className='w-[70%]'>
      <Sort/>
        <ProductList/>
       
      </div>
      
     </div>

    </div>
  )
}

export default Product
