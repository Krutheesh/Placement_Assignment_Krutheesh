import React, { useReducer } from 'react'
import { useState } from 'react'
import './index.css'
import{ AiFillDelete, AiFillEdit, AiFillCheckCircle} from 'react-icons/ai'

function App() {
  const [counter, setCounter] = useState(0)
  const [todo, setTodo] = useState('')
  const [isEdit, setIsedit] = useState(null)
  const reducer = (state,action) => {
    // console.log(state)
    // console.log(action.type,action.payload)
    switch(action.type){
      case 'ADD':
        const id = counter
        setCounter(counter+1)
        const newTodo = {
          id:id,
          text:action.payload,
          completed:false
        }
        return [...state,newTodo]
      case 'COMPLETED': 
        const a = state.map(ele => {
          if (ele.id === action.payload){
            // const newele = {completed : !(ele.completed)}
            // return {...ele,...newele}
            return {...ele,completed:true}
          }
          return ele
        })
        console.log(a)
        return a
        // console.log(state)
      case 'EDIT':
        return state.map(ele => 
          ele.id === action.payload.id ? {...ele,text:action.payload.text}:ele)
         

      case 'DEL': 
        const del = state.filter(ele => {
          return ele.id !== action.payload
        })

        return del

      default:
        break;

    }
  }
  const [state, dispatch] = useReducer(reducer,[])
// console.log(state)


//functions


  const handleAdd = (todo) => {
    if(isEdit){
      dispatch({type:'EDIT',payload:{id:isEdit.id,text:todo}})
      setIsedit(null)
      setTodo('')
    }
    else{
      dispatch({type:'ADD', payload:todo})
      setTodo('')
    }
    
  }
  
 const handleDelete = (id) => {
  dispatch({type:"DEL",payload:id})
 }

 const handleComplete = (ele) => {
  dispatch({type:"COMPLETED", payload:ele.id})

 }
 const handleEdit = (ele) => {

  setTodo(ele.text)
  setIsedit(ele)

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
      <input className='border-2 px-2 py-1 outline-none w-[45%]' value={todo} onChange={(e) => {setTodo(e.target.value)}} type="text" placeholder='enter todo' />
      <button className='bg-sky-600 px-2 py-1 rounded'>save</button>
    </form>
    <div>
    {
      (state.length !== 0) ? state.map(ele => {
        return(
          <div key={ele.id} >
            <div className='flex items-center justify-between w-[50%] border-2 '>
            <p className={`px-2 ${ele.completed?'line-through':""}`}>{ele.text}</p>
            <div className='flex items-center justify-between'>
            <span className={`p-2  ${ele.completed ? 'text-sky-600':''} `} onClick={() => handleComplete(ele) }> <AiFillCheckCircle></AiFillCheckCircle></span>
              <span onClick={ ()=> {handleEdit(ele)}} className='p-2 ' > <AiFillEdit></AiFillEdit></span>
              <span onClick={() => {handleDelete(ele.id)}} className='p-2 hover:text-red-600'> <AiFillDelete></AiFillDelete></span>
              
            </div>
            </div>
          
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
