import { configureStore } from "@reduxjs/toolkit";

import SliceReducer from "../Slice"
console.log(SliceReducer)
export const Store = configureStore({
  reducer:{
    ecom:SliceReducer
  }
})