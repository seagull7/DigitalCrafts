function Jscript(){
    //Header
    var header = document.createElement("div");
        header.style.backgroundColor = "blue";
        header.style.height = "10vh";
        header.style.marginLeft = "10vw";
        header.style.marginRight = "10vw";
        header.style.display = "flex";
        header.style.alignItems = "center";
        //Header content
        var HighOnCoding = document.createElement("div");
            HighOnCoding.textContent = "High On Coding";
            HighOnCoding.style.fontSize = "4em";
            HighOnCoding.style.color = "white";
            HighOnCoding.style.marginLeft = "3vw";
        var Home = document.createElement("div");
            Home.textContent = "Home";
            Home.style.fontSize = "2em";
            Home.style.color = "white";
            Home.style.marginLeft = "3vw";
        var Catgories = document.createElement("div");
            Catgories.textContent = "Catgories";
            Catgories.style.fontSize = "2em";
            Catgories.style.color = "white";
            Catgories.style.marginLeft = "3vw";
    //Grey box below header
    var greyBox = document.createElement("div");
    greyBox.setAttribute("style", "background-color: lightgrey; margin-top: 3vh; margin-left: 15vw; margin-right: 15vw; display: flex; flex-direction: column; height: 20vh;");
        var greyHead = document.createElement("div");
            greyHead.setAttribute("style", "color: grey; margin-top: 1vh; margin-left: 10%; width: 80%; height: 50%; font-size: 3em;");
            greyHead.textContent= "Curse of the Current Reviews"
        var greyBody = document.createElement("div");
            greyBody.setAttribute("style", "color: black; margin-top: 5vh; margin-left: 10%; width: 80%; height: 50%;");
            greyBody.textContent= "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Atque, quis nisi ipsam aut, minima eligendi deserunt modi sed vitae corporis doloremque nihil possimus totam asperiores quasi! Nam cum deserunt deleniti!"
    //article 1
    var Art1 = document.createElement("div");
    Art1.setAttribute("style", " margin-top: 3vh; margin-left: 15vw; margin-right: 15vw; display: flex; flex-direction: column; height: 17vh;");
        var ArtHead = document.createElement("div");
            ArtHead.setAttribute("style", "color: darkblue; width: 80%; height: 50%; font-size: 2em;");
            ArtHead.textContent= "Hello WatchKit"
        var ArtBody = document.createElement("div");
            ArtBody.setAttribute("style", "color: black; margin-top: 5vh; width: 98%; height: 50%;");
            ArtBody.textContent= "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Atque, quis nisi ipsam aut, minima eligendi deserunt modi sed vitae corporis doloremque nihil possimus totam asperiores quasi! Nam cum deserunt deleniti!"
        var ArtBox = document.createElement("div");
            ArtBox.setAttribute("style", "background-color: orange; color: white;");
            ArtBox.textContent= ("12 comments          124 Likes")
    //article 2
    var Art2 = document.createElement("div");
    Art2.setAttribute("style", " margin-top: 3vh; margin-left: 15vw; margin-right: 15vw; display: flex; flex-direction: column; height: 17vh;");
        var ArtHead2 = document.createElement("div");
            ArtHead2.setAttribute("style", "color: darkblue; width: 80%; height: 50%; font-size: 2em;");
            ArtHead2.textContent= "Introduction to Swift"
        var ArtBody2 = document.createElement("div");
            ArtBody2.setAttribute("style", "color: black; margin-top: 5vh; width: 98%; height: 50%;");
            ArtBody2.textContent= "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Atque, quis nisi ipsam aut, minima eligendi deserunt modi sed vitae corporis doloremque nihil possimus totam asperiores quasi! Nam cum deserunt deleniti!"
        var ArtBox2 = document.createElement("div");
            ArtBox2.setAttribute("style", "background-color: orange; color: white;");
            ArtBox2.textContent= ("15 comments          45 Likes")
    


  

    document.body.appendChild(header);
        header.appendChild(HighOnCoding);
        header.appendChild(Home);
        header.appendChild(Catgories);
    document.body.appendChild(greyBox);
        greyBox.appendChild(greyHead);
        greyBox.appendChild(greyBody);
    document.body.appendChild(Art1);
        Art1.appendChild(ArtHead);
        Art1.appendChild(ArtBody);
        Art1.appendChild(ArtBox);
    document.body.appendChild(Art2);
        Art2.appendChild(ArtHead2);
        Art2.appendChild(ArtBody2);
        Art2.appendChild(ArtBox2);
}