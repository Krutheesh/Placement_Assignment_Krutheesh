const tog = document.getElementById('tog');
const moon = document.getElementById('moon');
const sun = document.getElementById('sun');
sun.classList.add('hidden')
console.log(moon)
tog.addEventListener('click', () => {
  const html = document.querySelector('html')
  console.log(html)
const bo = html.classList.toggle('dark')
console.log(bo)
if(bo){
  moon.classList.add('hidden')
  sun.classList.remove('hidden')
}
else{
  sun.classList.add('hidden')
  moon.classList.remove('hidden')
}
})
