


let img = document.getElementById('img')
let picture = document.getElementById('picture')
let elements = document.querySelectorAll("#img")

let rev = document.getElementById('rev')
let quest = document.getElementById('quest')
let block_rev = document.getElementById('block_rev')
let block_quest = document.getElementById('block_quest')


quest.onclick = function(){
    rev.style.color = '#9d9da5;'
    quest.style.color = '#000;'
    block_rev.style.display = 'none'
    block_quest.style.display = 'block'
}

rev.onclick = function(){
    quest.style.color = '#9d9da5;'
    rev.style.color = '#000;'
    block_quest.style.display = 'none'
    block_rev.style.display = 'block'
}


function showImage(element) {
    var imageSrc = element.getAttribute("src");
    var pictureImg = document.getElementById("picture");
    pictureImg.setAttribute("src", imageSrc);
  }


let about = document.getElementById('about')
let descp = document.getElementById('descp')
let text = document.getElementById('text1')
let text2 = document.getElementById('text2')
about.onclick = function(){
    about.style.background = '#fff'
    descp.style.background = '#F9F8FB'
    text.classList.add('active-text')
    text.classList.remove('deactive-text')
    text2.classList.remove('active-text')
    text2.classList.add('deactive-text')
}

descp.onclick = function(){
    descp.style.background = '#fff'
    about.style.background = '#F9F8FB'
    text2.classList.add('active-text')
    text2.classList.remove('deactive-text')
    text.classList.remove('active-text')
    text.classList.add('deactive-text')
}