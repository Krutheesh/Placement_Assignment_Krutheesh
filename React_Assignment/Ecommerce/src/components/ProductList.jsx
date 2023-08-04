import React from 'react'
import { useSelector } from 'react-redux'
import { Link } from 'react-router-dom'
function ProductList() {
  const products = useSelector((state) => state.ecom.varProducts)
  console.log(products)
  return (
   
     <div className='grid grid-cols-3 gap-4 gap-y-8'>
      {
        products.map((ele,index) => 
           (
            <Link to={`/singleproduct/${ele.name}`}>
            <div key={index} className=' bg-gray-200 p-3'>
              <div>
                <img src={ele.image} className=' h-[10rem]'/>
              </div>
              <div className='flex justify-between pt-2'>
              <span> {ele.name}</span>
               <span className='text-blue-600'>{ele.price}</span>
              </div>
               
              </div>
              </Link>
          )
        )
      }
  
    </div>
   
  )
}

export default ProductList
