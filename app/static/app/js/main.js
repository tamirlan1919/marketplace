


let img = document.getElementById('img')
let picture = document.getElementById('picture')
let elements = document.querySelectorAll("#img")

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