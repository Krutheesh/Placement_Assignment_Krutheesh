import React from 'react'
import  {Link} from 'react-router-dom'
function Nav() {
  return (
    <div className='flex justify-between bg-[#f2e6ff] font-semibold items-center px-[1.5rem] py-[0.5rem]'>
      <div className='text-[2rem]'>
        <Link to='/'><span className='text-[#9933ff] '>K</span>STORE</Link>
      </div>
      <ul className='flex justify-between text-gray-600 font-semibold space-x-[2rem]  '>
        <li className='hover:text-black cursor-pointer'>
          <Link to='/'>Home</Link>
          </li>
        <li className='hover:text-black cursor-pointer'>
          <Link to='/about'>About Us </Link> 
          </li>
        <li className='hover:text-black cursor-pointer'>
          <Link to='/product'>Products</Link>
        </li>
        <li className='hover:text-black cursor-pointer'>
          <Link to='/contact'>Contact Us</Link>
          </li>
        <li className='hover:text-black cursor-pointer'>
          <Link to='/login'>Login</Link>
          </li>
        <li className='hover:text-black cursor-pointer'>
          <Link to="/cart"> Cart</Link></li>

      </ul>
    </div>
  )
}

export default Nav
