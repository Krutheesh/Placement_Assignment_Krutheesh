fetch("https://jsonplaceholder.typicode.com/posts")
  .then((res) => res.json())
  .then((data) => {
    data.forEach((data) => {
      const divElement = document.createElement("div");
      divElement.className = "blogdiv";
      divElement.id= "bdiv"

      const title = document.createElement("h2");
      const tnode = document.createTextNode(`${data.title}`);
      title.appendChild(tnode);
      title.className = "title";
      // const id = document.createElement('p')
      // const inode = document.createTextNode(` id: ${data.id}`);
      // id.appendChild(inode)

      //const userid = document.createElement('p')
      // const unode = document.createTextNode(`user id :${data.userId}`);
      // userid.appendChild(unode)

      const div = document.createElement("div");
      const del = document.createElement("button");
      const delnode = document.createTextNode("delete");
      del.appendChild(delnode);
      div.appendChild(del);
      div.className = "deldiv";
      del.className = "delbutton";
      del.addEventListener("click", () => {
        const deleteUrl = `https://jsonplaceholder.typicode.com/posts/${data.id}`;
        fetch(deleteUrl, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json", 
          },
        })
          .then((response) => {
            if (response.ok) {
              // Successful deletion
              console.log(`Resource with ID ${data.id} deleted successfully`);
              const element = document.getElementById('bdiv');
              if (element) {
                element.remove();
              }
            } else {
              // Handle the error
              throw new Error(`Error deleting resource with ID ${data.id}`);
            }
          })
          .catch((error) => {
            // Handle any errors
            console.error("Error:", error);
          });
      });

      const body = document.createElement("p");
      const bnode = document.createTextNode(`${data.body}`);
      body.appendChild(bnode);
      body.className = "body";

      divElement.appendChild(title);
      // divElement.appendChild(userid);
      // divElement.appendChild(id);
      divElement.appendChild(body);
      divElement.appendChild(div);
      document.getElementById("main").appendChild(divElement);
      console.log(data);
    });
  })
  .catch((error) => console.log(error));

const form = document.getElementById("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.getElementById("intitle");
  const description = document.getElementById("indescrip");
  console.log(title.value, description.value);

  if (title.value !== "" && description.vlaue !== "") {
    const url = "https://jsonplaceholder.typicode.com/posts";
    const data = {
      title: title.value,
      body: description.value,
    };

    const option = {
      method: "POST",
      headers: {
        "content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
    fetch(url, option)
      .then((response) => response.json())
      .then((result) => {
        console.log("Data posted successfully:", result);
        
        

        
      })
      .catch((error) => {
        console.error("Error posting data:", error);
        
      });
  } else {
    alert("title or description is empty");
  }
});
