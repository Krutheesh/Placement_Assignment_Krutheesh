import {createSlice} from "@reduxjs/toolkit"
const initialState = {
  products: [],
  varProducts:[]
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
    all:(state,payload) => {
      console.log(state.products)
      state.varProducts=state.products
    },
    low_to_high: (state,payload) => {
      state.varProducts.sort((a,b) => a.price-b.price)
      console.log(state.varProducts)
    },
    high_to_low: (state,payload) => {
      state.varProducts.sort((a,b) => b.price-a.price)
      
      console.log(state.varProducts)
    },
    A_to_Z: (state,payload) => {
      state.varProducts.sort((a,b) => a.name.localeCompare(b.name))
      
      console.log(state.varProducts)
    }
  }
})

export const {addProducts,mobile,laptop,computer,Accessories,watch,all,low_to_high,high_to_low,A_to_Z}=Slice.actions
export default Slice.reducer