import React, { useReducer } from 'react'
import { useState } from 'react'
import './index.css'


function App() {
  const [counter, setCounter] = useState(0)
  const [todo, setTodo] = useState('')
  const reducer = (state,action) => {
    console.log(state)
    console.log(action.type,action.payload)
    switch(action.type){
      case 'ADD':
        const id = counter
        setCounter(counter+1)
        const newTodo = {
          id:id,
          text:action.payload
        }
        return [...state,newTodo]

    }
  }
  const [state, dispatch] = useReducer(reducer,[])
console.log(state)

//functions

  const handleAdd = (todo) => {
    dispatch({type:'ADD', payload:todo})
  }
  

  
  const formHandler = (e) => {
    e.preventDefault()
    // console.log(todo)
    if(todo ===''){
      alert("add todo")
    }
    else{
      handleAdd(todo)
    }
    
  }
 
  return (

   <>
   <div>
    <form action="" onSubmit={formHandler}>
      <input className='border-2 px-2 py-1 outline-none' value={todo} onChange={(e) => {setTodo(e.target.value)}} type="text" placeholder='enter todo' />
      <button className='bg-sky-600 px-2 py-1 rounded'>submit</button>
    </form>
    <div>
    {
      (state.length !== 0) ? state.map(ele => {
        return(
          <div key={ele.id}>
          {ele.text}
           </div>
        )
        
      }): 
      <div> no todos</div>
    }
    </div>
    </div> 
   </>
  )
}

export default App
