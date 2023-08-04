import React from 'react'
import { useSelector } from 'react-redux'
import { useDispatch } from 'react-redux'
import { addToCart } from '../Slice'
import { useParams } from 'react-router-dom'
function SingleProduct() {
  const {id} = useParams()
  // console.log(id)
  const dispatch = useDispatch()
  const product = useSelector((state) => state.ecom.products)
  const cartItems = useSelector((state) => state.ecom.cartItems)
   console.log(cartItems)
  const noItems = useSelector((state) => state.ecom.noItems)
  // console.log(noItems)
  const singlePage = product.filter(ele => ele.name === id)
  // console.log(singlePage)

  const handlePage = (a) => {
    dispatch(addToCart(a))
  }


  return (
    <div className='flex items-center h-[100vh]'>
      <div className='flex  justify-center  '>
       <div className='w-[35%] p-[3rem] '>
        <img   src={singlePage[0].image} alt="im" />
       </div>
      <div className='w-[50%] px-[7rem] text-gray-600'>
        <h2 className='text-[2rem] font-semibold'>{singlePage[0].name}</h2>
        <div>stars</div>
       <div>
        MRP: <span className='text-blue-600'>{singlePage[0].price}</span>
       </div>
       <div>
       {singlePage[0].description}
       </div>

        <div>
          <p>Avilabel: In Stock</p>
          <p>ID: <span className='text-black font-semibold'>{singlePage[0].id}</span></p>
          <p>Brand:<span className='text-black font-semibold' > {singlePage[0].company} </span></p>
        </div>

        <div className='my-[2rem]'>
          <button className='p-3 bg-[#9933ff] text-white font-semibold' onClick={() => handlePage(singlePage[0].name)} > Add to Cart</button>
        </div>
        </div>

        <div>

        </div>

       
        
    </div>
    </div>
  )
}

export default SingleProduct
