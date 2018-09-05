let express = require('express');
let router = express.Router();


router.get('/doges', (req, res) => {

    var dataFile = req.app.get("appData");
    let myHTML;

    var pagePhotos = [];

    dataFile.doge.forEach(function(items){
        pagePhotos = pagePhotos.concat(items.artwork[0]);
    })

      
    

    res.render('doges', {
        pageTitle: 'doge',
        artwork: pagePhotos,
        speakers: dataFile.doge,
        pageID: 'home',
        datafile: dataFile
    })
    
    

    // res.send(
    // `
    // <header style=" display: flex; 
    // flex-direction: row;
    // height: 150px;
    // background-color: black;
    // opacity: 80%;
    // justify-content: space-between;
    // align-items: center;
    // position: fixed;
    // width: 100%;">
    // <img style=" width: 150px;
    // height: 150px;" class = "headIMG" src="https://media0.giphy.com/media/ZO8upuwNKfpm0/giphy.gif" alt="doge">
    // <a href="/">
    //     <h1 style="font-size: 100px;
    //     color: lightslategray;">Wow, such Doge!</h1>
    // </a>
    // <a href="/doges">
    //     <h2 style="color: lightslategray;
    //     margin-right: 1vw;">Doge Compendium ></h2>
    // </a>
    // </header>
    // <div style="height: 120px"></div>
    // <ul>
    //     ${myHTML}
    // </ul>
    // `)
})

router.get('/breeds/:dogeID', (req, res) => {

    let dataFile = req.app.get("appData");

    let doge = dataFile.doge[req.params.dogeID];

    var pagePhotos = [];

    dataFile.doge.forEach(function(items){
        pagePhotos = pagePhotos.concat(items.artwork[0]);
    })

      
    

    res.render('breeds', {
        pageTitle: 'doge',
        artwork: pagePhotos,
        speakers: dataFile.doge,
        pageID: 'home',
        datafile: dataFile,
        doge: doge
    })
})

module.exports = router;