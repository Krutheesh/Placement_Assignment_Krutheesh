import React from 'react'
import Home from './pages/Home'
import Nav from './Nav'
import {Outlet} from 'react-router-dom'
import Footer from './pages/Footer'
function App() {
  return (
    <div className=' text-center'>
      <Nav/>
      <Outlet/>
      <Footer/>
    </div>
  )
}

export default App
