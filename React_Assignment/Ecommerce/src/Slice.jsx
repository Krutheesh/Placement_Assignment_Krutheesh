import {createSlice} from "@reduxjs/toolkit"
const initialState = {
  products: [],
  varProducts:[],
  price:6000000,
  cartItems:[],

  
}
export const Slice = createSlice({
  name:'ecom',
  initialState,
  reducers: {
    addProducts:(state,action) => {
       state.products = action.payload
       console.log(state.products)
       state.varProducts=action.payload
    },
    mobile:(state,action) => {
      state.varProducts= state.products.filter((ele) => {
        return ele.category === 'mobile'
      })
      console.log(state.products)
    },
    laptop:(state,action) => {
      state.varProducts= state.products.filter((ele) => {
        return ele.category === 'laptop'
      })
    },
    computer:(state,action) => {
      state.varProducts= state.products.filter((ele) => {
        return ele.category === 'computer'
      })

    },
    Accessories:(state,action) => {
      state.varProducts= state.products.filter((ele) => {
        return ele.category === 'accessories'
      })
    },
    watch:(state,action) => {
      state.varProducts= state.products.filter((ele) => {
        return ele.category === 'watch'
      })
    }
    ,
    all:(state,action) => {
      console.log(state.products)
      state.varProducts=state.products
    },
    low_to_high: (state,action) => {
      state.varProducts.sort((a,b) => a.price-b.price)
      console.log(state.varProducts)
    },
    high_to_low: (state,action) => {
      state.varProducts.sort((a,b) => b.price-a.price)
      
      console.log(state.varProducts)
    },
    A_to_Z: (state,action) => {
      state.varProducts.sort((a,b) => a.name.localeCompare(b.name))
      
      console.log(state.varProducts)
    }
    , companies:(state,action) => {
      state.varProducts= state.products.filter((ele) => ele.company === action.payload)

    }
    ,rcolors:(state,action) => {
     console.log(action.payload)
    state.varProducts = state.varProducts.filter((value) => value.colors.includes(action.payload) )
   console.log(state.varProducts)  
  },
  maxPrice :(state,action) => {
    console.log(action.payload)
    state.price=action.payload
    state.varProducts=state.products.filter(ele => ele.price<= action.payload)
    console.log(state.varProducts)
  },
  addToCart : (state,action) => {
    
    const alreadyExist = state.cartItems.filter((ele) => ele.ai.name === action.payload)
    console.log(alreadyExist)
    if (alreadyExist.length!==0){
      alreadyExist[0].noItems+=1
       
    }
    else{
      const item = state.products.filter(ele => ele.name === action.payload)
      console.log(item[0].name)
      const ob = {
        ai:item[0],
        noItems:1
      }
      state.cartItems=[...state.cartItems,ob]
    }
    
  
}, 
deleteFromCart: (state,action) => {
  // console.log(action.payload)
  state.cartItems = state.cartItems.filter(ele => ele.ai.name!==action.payload)
  console.log(state.cartItems)
}
,
incr: (state,action) => {
  console.log(action.payload)
  const item = state.cartItems.filter(ele => ele.ai.name === action.payload)
  item[0].noItems+=1
},
decr : (state,action) => {
  console.log(action.payload)
  const item = state.cartItems.filter(ele => ele.ai.name === action.payload)
  if(item[0].noItems<=1){
    state.cartItems = state.cartItems.filter(ele => ele.ai.name!==action.payload)
  }
  else{
    item[0].noItems-=1
  }
}
 
  }
})

export const {decr,incr,deleteFromCart, addToCart,maxPrice,companies,addProducts,mobile,laptop,computer,Accessories,watch,all,low_to_high,high_to_low,A_to_Z,rcolors}=Slice.actions
export default Slice.reducer