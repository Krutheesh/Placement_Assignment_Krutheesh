// console.log("hello krutheesh let party with backend development love u buddy jfnjn")
const express = require('express');
const app = express()
const port = 3000

app.use(express.json())

app.get('/' , (req,res) => {
  res.send("<h1>hello</h1>")
  
})

const ph = [
  {
    id:1,
    name:"ram"
  }
  ,
  {
    id:2,
    name: "akbar",
  }
  ,
  {
    id:3,
    name:"joseph"
  }

]

const a = app.get("/home",(req,res) => {
  return res.send(ph)
})

app.get('/home/:id',(req,res) => {
  const data = ph.filter((item) => item.id.toString() === req.params.id)
  res.send(data);
})
app.post('/hero',(req,res) => {
  const {id} = req.body
  console.log('hello world')
  app.get('/hai', (req,res) => {
    res.send(id)
  })
  res.send(`id = ${id}`)
})
app.listen(port, () => {
  console.log(`example port ${port}`)
})
