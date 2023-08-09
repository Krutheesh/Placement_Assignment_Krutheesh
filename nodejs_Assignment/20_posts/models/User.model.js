const mongoose = require("mongoose");

const userSchema = mongoose.Schema({
  title:{
    type:String,
    required : [true,'title is required']
  },
  content : {
    type: String,
    required:[true,'content is required']
  },
  

},{timestamp:true})

module.exports = mongoose.model('User',userSchema)