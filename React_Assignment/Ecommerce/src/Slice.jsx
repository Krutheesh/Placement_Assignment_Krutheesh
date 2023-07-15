import {createSlice} from "@reduxjs/toolkit"
const initialState = {
  products: [],
}

export const Slice = createSlice({
  name:'ecom',
  initialState,
  reducers: {
    addProducts:(state,action) => {
       state.products = action.payload
    }
  }
})

export const {addProducts}=Slice.actions
export default Slice.reducer