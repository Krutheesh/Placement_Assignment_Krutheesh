import React from 'react'
import hero from './assets/hero.jpg'
function Headerone({heading}) {
  return (
    <div className='flex flex-col-reverse items-center justify-between md:flex md:flex-row md:justify-center py-[5rem]   md:space-y-0'>
      <div className=' w-[30rem] text-left py-2'>
        <p className='text-gray-600'>Welcome to</p>
        <span className='text-[2.5rem] font-semibold'>{heading}</span>
        <p className='text-gray-600'>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Debitis, error. Dolores impedit quos consequatur dolore.</p>
        <button className='bg-[#9933ff] text-white font-semibold p-2 my-2'>
          SHOP NOW
        </button>
      </div>
      <div className='w-[30rem]'>
        
        <img className=' md:w-[100%]' src={hero} alt="dfghjk" />
      </div>
      <div>

      </div>
    </div>
  )
}

export default Headerone
