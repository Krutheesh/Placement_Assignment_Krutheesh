import {createSlice} from "@reduxjs/toolkit"
const initialState = {
  products: [],
  varProducts:[],
  price:6000000
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
  }
  
  }
})

export const {maxPrice,companies,addProducts,mobile,laptop,computer,Accessories,watch,all,low_to_high,high_to_low,A_to_Z,rcolors}=Slice.actions
export default Slice.reducer