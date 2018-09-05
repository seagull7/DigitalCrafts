let express = require('express');
let router = express.Router();

router.get('/', (req, res) => {


    var data = req.app.get('appData');

    var pagePhotos = [];

    data.doge.forEach(function(items){
        pagePhotos = pagePhotos.concat(items.artwork[0]);
    })
    res.render('index', {
        pageTitle: 'Home',
        artwork: pagePhotos,
        speakers: data.doge,
        pageID: 'home'

    })
})

module.exports = router;