import React from 'react'
import { useSelector } from 'react-redux'
function Product() {
  const products = useSelector((state) => state.ecom.products)
  console.log(products)
  return (
    <div>
      {
        products.map((ele,index) => 
           (
            <div key={index}>
                {ele.name}
              </div>
          )
        )
      }
     
    </div>
  )
}

export default Product
