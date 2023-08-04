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
import ProductRedux from './ProductRedux.jsx'
import {createBrowserRouter, RouterProvider} from 'react-router-dom';
import SingleProduct from './components/SingleProduct.jsx'
import { Provider } from 'react-redux'
import { Store } from './app/Store.jsx'
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
    
  },
  {
    path:'/singleproduct/:id',
    element:<SingleProduct/>
  }
])







ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={Store}>
    <RouterProvider router={appRouter}/>
    </Provider>
    
    
  </React.StrictMode>,
)
