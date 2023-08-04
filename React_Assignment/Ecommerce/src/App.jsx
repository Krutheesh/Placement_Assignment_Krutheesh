import React from 'react'
import Home from './pages/Home'
import Nav from './Nav'
import {Outlet} from 'react-router-dom'
import Footer from './pages/Footer'

import ProductRedux from './ProductRedux'
function App() {
  return (
    
    <div >
      <Nav/>
      <Outlet/>
      <ProductRedux/>
      <Footer/>
    </div>
    
  )
}

export default App
