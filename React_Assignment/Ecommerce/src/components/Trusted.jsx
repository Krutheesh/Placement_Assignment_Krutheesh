import React from 'react'
import {FaMicrosoft,FaFacebook,FaAtlassian,FaAmazon} from "react-icons/fa"

function Trusted() {
  return (
    <div  className='space-y-[3rem]'>
      <div >
        Tusted by 1000+ companies
      </div>
      <div className='flex justify-between items-center  '>
        <div className='flex justify-between items-center space-x-4 '>
          <div><FaMicrosoft className='text-[2rem]'/></div>
          <div>Microsoft</div>
        </div>
        <div className='flex justify-between items-center space-x-4  '>
          <div> <FaFacebook className='text-[2rem]'/></div>
          <div>Facebook</div>
        </div>
        <div className='flex justify-between items-center space-x-4  '>
          <div><FaAmazon className='text-[2rem]'/></div>
          <div>Amazon</div>
        </div>
        <div className='flex justify-between items-center space-x-4 '>
          <div><FaAtlassian className='text-[2rem]'/></div>
        <div>Atlassian</div>
        </div>
      </div>
    </div>
  )
}

export default Trusted
