import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import Home from './pages/Home.jsx'
import About from './pages/About.jsx'
import Cart from './pages/Cart.jsx'
import Contact from './pages/Contact.jsx'
import Login from './pages/Login.jsx'
import Product from './pages/Product.jsx'
import {createBrowserRouter, RouterProvider} from 'react-router-dom';

const appRouter = createBrowserRouter([
  {
    path:'/',
    element:<App/>,
    children:[
      {
        path:'/',
        element:<Home/>
      },
      
      {
        path:'/about',
        element:<About/>
      },
      {
        path:'/product',
        element:<Product/>
      },
      {
        path:'/contact',
        element:<Contact/>
      },
      {
        path:'/login',
        element:<Login/>
      },
      {
        path:'/cart',
        element:<Cart/>
      }
    ]
  }
])







ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={appRouter}/>
  </React.StrictMode>,
)
