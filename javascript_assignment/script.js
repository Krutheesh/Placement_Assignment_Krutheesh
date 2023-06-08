fetch("https://jsonplaceholder.typicode.com/posts").then(res => res.json()).then(data => 


data.forEach( data => 
{
  const divElement = document.createElement('div')
  divElement.className = 'blogdiv'

  const title = document.createElement('h2')
  const tnode = document.createTextNode(`${data.title}`);
  title.appendChild(tnode)
title.className='title'
  const id = document.createElement('p')
  const inode = document.createTextNode(` id: ${data.id}`);
  id.appendChild(inode)

  const userid = document.createElement('p')
  const unode = document.createTextNode(`user id :${data.userId}`);
  userid.appendChild(unode)

  const div = document.createElement('div')
  const del = document.createElement('button')
  const delnode = document.createTextNode("delete")
  del.appendChild(delnode)
  div.appendChild(del)
  div.className="deldiv"
  del.className='delbutton'


  const body = document.createElement('p')
  const bnode = document.createTextNode(`${data.body}`);
  body.appendChild(bnode)
  body.className='body'

  divElement.appendChild(title)
  divElement.appendChild(userid);
  divElement.appendChild(id);
  divElement.appendChild(body);
  divElement.appendChild(div)
  document.getElementById('main').appendChild(divElement)
  console.log(data)
}
)
).catch(error => console.log(error))
