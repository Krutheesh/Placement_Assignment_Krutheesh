import React from 'react'
import { useState } from 'react'
import { useDispatch } from 'react-redux'
import { low_to_high,all,high_to_low,A_to_Z} from '../Slice'
function Sort() {

const [valop,setValop] = useState('all')
const dispatch = useDispatch()
const handleSort = (event) => {
 
setValop(event.target.value)
 
 console.log(event.target.value)

}
if(valop == 'all'){
  dispatch(all())
}
if (valop=='low_to_high'){
  dispatch(low_to_high())
}
if (valop=='high_to_low'){
  dispatch(high_to_low())
}
 if (valop=='A_to_Z'){
  dispatch(A_to_Z())
}
 


  return (
    <div className='flex items-center justify-between py-[2rem]'>
      <div className='text-[1.5rem] font-semibold text-[#9933ff] '>
        KStore
      </div>
      <div className=' font-semibold text-gray-600 '>
      Products available
      </div>
      <div>
        <select  className='border-gray-600 border-2' name="" id="" value={valop}  onChange={handleSort}>
        <option value="all">default</option>
          <option value="low_to_high" >Price(low to high)</option>
          <option value="high_to_low">Price(high to low)</option>
          <option value="A_to_Z">Price(A to Z)</option>
          
        </select>
      </div>
    </div>
  )
}

export default Sort
