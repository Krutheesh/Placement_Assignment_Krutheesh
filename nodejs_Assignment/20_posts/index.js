const express = require("express");
const mongoose = require("mongoose");
const User = require('./models/User.model')
const app = express();

async function db() {
  try {
  await mongoose.connect('mongodb://127.0.0.1:27017/Posting')
    console.log("db jkmconnected");
    app.on("error", (err) => {
      console.log("error",err)
      throw err
    })

    app.listen(4000, () => {
      console.log("listn tfygujrt 4000");
    });
  } catch (err) {
    console.log("hell", err);
  }
}

db();
console.log(User)

app.post('/post', async(req,res) =>{
  try{
    const postsToCreate = Array.from({ length: 20 }, (_, index) => ({
      title: `Post ${index + 1}`,
      content: `Content of Post ${index + 1}`,
    }));
    const info = await User.insertMany(postsToCreate)
    console.log(info)
    res.send(info)
  }
  catch(err){
    console.log(err)
    throw err
  }

})

app.get('/get',(req,res) => {
res.send("hello iam get get me")
})
// app.on???????????????????????????????
// Certainly, let's break down the explanation clearly with an example:

// Imagine you have an Express.js application that interacts with a database to perform user registration. You have a route handler to create a new user in the database. However, there's a possibility of various errors during the registration process, and you might forget to handle some of those errors explicitly using `try...catch` blocks.

// Here's a scenario illustrating the concept:

// ```javascript
// const express = require('express');
// const mongoose = require('mongoose');

// const app = express();

// // Assume mongoose is connected to the database

// app.post('/register', async (req, res) => {
//   const userData = req.body;

//   // Simulate an error by attempting to save user data with a missing required field
//   const newUser = new User(userData);
//   await newUser.save();

//   res.status(201).json({ message: 'User registered successfully' });
// });

// app.listen(3000, () => {
//   console.log('Server is running on port 3000');
// });
// ```

// In this example, an error might occur if the `userData` object doesn't have all the required fields that the `User` model expects. This could lead to an unhandled error during the `newUser.save()` operation.

// Now, let's imagine you didn't include a `try...catch` block to handle errors in this specific route handler.

// Here's where the `app.on("error", ...)` block comes into play:

// ```javascript
// app.on("error", (error) => {
//   console.error('Unhandled error:', error.message);
//   // You can perform additional actions here, such as logging or notifying
// });

// app.listen(3000, () => {
//   console.log('Server is running on port 3000');
// });
// ```

// In this code, the `app.on("error", ...)` block is set up to catch and handle unhandled errors that occur anywhere in your Express application during runtime. If an error occurs in the `/register` route handler or anywhere else that wasn't explicitly caught using `try...catch`, the `app.on("error", ...)` block will catch it.

// So, if there's an unhandled error during the execution of the `/register` route handler (for example, due to the missing required field), the `app.on("error", ...)` block will log the error message and provide a way for you to perform additional actions, such as notifying the admin or gracefully handling the error.

// In essence, the `app.on("error", ...)` block is your last line of defense to catch and handle unhandled errors that occur during the runtime of your Express application, particularly those that might occur in parts of the code where you might have missed including specific `try...catch` blocks.