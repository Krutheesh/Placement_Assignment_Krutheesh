import React from 'react'
import Home from './pages/Home'
import Nav from './Nav'
import {Outlet} from 'react-router-dom'
import Footer from './pages/Footer'
import {Store} from "./app/Store"
import { Provider } from 'react-redux'
import ProductRedux from './ProductRedux'
function App() {
  return (
    <Provider store={Store}>
    <div >
      <Nav/>
      <Outlet/>
      <ProductRedux/>
      <Footer/>
    </div>
    </Provider>
  )
}

export default App
