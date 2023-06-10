import React, { useState } from 'react'
import "./style.css"
function App() {
  const [counter, setCounter] = useState(0)
  const increment = () => {
   setCounter(counter+1)
  }
  const decrement = () => {
    setCounter(counter-1)
  }
  return (
    <div className='whole'>
      
      <div className='main'>
        <button onClick={() => increment()}>+</button>
        <span>{counter}</span>
        <button onClick={() => decrement()}>-</button>
      </div>

    </div>
  )
}

export default App
