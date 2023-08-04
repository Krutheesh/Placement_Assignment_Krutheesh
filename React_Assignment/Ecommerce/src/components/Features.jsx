import React from 'react'
import { useSelector } from 'react-redux'
import { Link } from 'react-router-dom'
function Features() {
const feature = useSelector((state) => state.ecom.products)
console.log(feature)

  return (
    
      <div>
      <div className='text-gray-600'>
        check now 
      </div>
      <h3 className='text-[1.5rem] font-semibold pb-2'>
        Our Feature Services
      </h3>
      <div className='flex items-center justify-between'>
      {
        
        feature.map((ele)=> {
         
          if (ele?.featured ){
            return(
              <Link to = {`singleproduct/${ele.name}`} className='w-[30%] bg-white p-4'>
              <div key={ele.id} className=' '>
                <img src={ele.image} alt=""  />
                <div className='flex justify-between text-gray-600 py-2'>
                  <span>{ele.name}</span>
                  <span>${ele.price}</span>
                </div>
                
                 </div>
                 </Link>
            )
          }
        }

           )
      }
      
    </div>
    </div>
   
    
  )
}

export default Features
