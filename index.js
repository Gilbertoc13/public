

async function carregarAnimais(){
    const respons = await axios.get('http://127.0.0.1:8000/animais')
    
    const animais = respons.data

    const lista = document.getElementById('Lista-Animais')
    
    
    animais.forEach(animal =>{
        
    const item  = document.createElement('li')
    item.innerText = animal.name

    lista.appendChild(item)
});



}

function app(){
    console.log("App iniciado")
    console.log("Olá")
    carregarAnimais()

}
app()
