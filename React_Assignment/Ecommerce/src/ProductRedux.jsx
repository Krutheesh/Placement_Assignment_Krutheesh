import axios from 'axios'
import React, { useEffect } from 'react'
import { addProducts } from './Slice'
import {useSelector, useDispatch} from 'react-redux'
function ProductRedux() {

 


  const dispatch = useDispatch()
const apiData = async() => {
  try{
    const data = await axios.get("https://api.pujakaitem.com/api/products")
    console.log(data.data)
    dispatch(addProducts(data.data))
  }
  catch (err){
    console.log(err)
  }
}

useEffect(() => {
 apiData()
},[])



  return (
    <div>
      
    </div>
  )
}

export default ProductRedux
