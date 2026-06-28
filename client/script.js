async function loadEvents(){const r=await fetch('/events');const d=await r.json();const ul=document.getElementById('events');if(ul){ul.innerHTML='';d.forEach(e=>{const li=document.createElement('li');li.textContent=e.title;ul.appendChild(li);});}}
async function addEvent(title){await fetch('/events',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title})});loadEvents();}
document.addEventListener('DOMContentLoaded',loadEvents);
