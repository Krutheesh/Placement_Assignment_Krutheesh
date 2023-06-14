import React from 'react'

function Square({fig,setFig,id}) {
  return (
    <div onClick={() => setFig(id)}  className='text-[3rem] font-semibold  flex justify-center items-center  border h-[18vh]'>
    {fig}
    </div>
  )
}

export default Square
