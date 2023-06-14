import React, { useEffect } from 'react'
import Square from './components/Square'
import { useState } from 'react'
function App() {
  const [boxes,setBoxes] = useState(['','','','','','','','',''])
  const [figChange, setFigchange] = useState(true)
  const [winner, setWinner] = useState(null)
  const [tie,setTie] = useState(0)
 const setFig = (id) => {
  // console.log(id)
    const newBox = boxes.map((ele,index) =>{
      if(index === id && ele === '' && figChange === true){
        setFigchange(!figChange)
        setTie(tie+1)
        return "X"
      }
      else if(index === id && ele === '' && figChange === false){
        setFigchange(!figChange)
        setTie(tie+1)
        return 'O'
      }
      return ele
    }
  
    )
    // console.log(newBox)
    setBoxes(newBox)
    
 }

 const checkWinner = () => {
  const winningConditions = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
  ]

  winningConditions.forEach(ele => {
    const [a,b,c] = ele;
    if(boxes[a] && boxes[a] === boxes[b] && boxes[a] === boxes[c]){
      setWinner(boxes[a]);
      
      // console.log(boxes[a]);
      
    }
   
    
  })

 }


 useEffect( () => {
   checkWinner()
 },[boxes] )
// console.log(winner)

 const resetHandler = () => {

  setBoxes(['','','','','','','','',''])
  setWinner(null)
  setTie(0)
 }

console.log(tie)

 
  return (
    <div className='space-y-[2rem]'> 
    
    <div className='text-[2rem] font-bold text-center text-sky-700 py-[1rem]' >
      Tic-Tac-Toe using ReactJs
    </div >


      <section className='w-[25rem] m-auto  space-y-[2rem]'>
      {/* <div className=' flex justify-between items-center'>
        <span className='text-green-600 font-semibold'>Player X</span>
        <span className='text-red-600 font-semibold'>Player O</span>
      </div> */}
      {winner? <div className='text-center text-[1.5rem]'>Congratulations! <span className='text-green-600 font-semibold'>  {winner}  </span>   won the Match</div> : 
      (tie === 9 ? <div className='text-[2rem] text-center'>-- Match Tie --</div> :  <div className='grid grid-cols-3 bg-white   '>
      {
        boxes.map((ele,index)=> {
          return(
            <Square key={index} fig={ele} setFig={setFig} id={index}/>
          )
        })
      }
    </div> )
      
      }
     
      <div className='text-center '>
        <button onClick={() => resetHandler()} className='border bg-sky-600 rounded text-white font-semibold px-4 py-2'> 
          Restart
        </button>
      </div>
      </section>
    </div>
  )
}

export default App

