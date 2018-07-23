var page = require('webpage').create();
var args = require('system').args;

page.onResourceError = function(resourceError) {
    if (/.js/g.test(resourceError.url)) {
        console.log(resourceError.url);
    }
};

page.open(args[1], function (status) {
    if (status == 'success') {
       //page.render('test2.png');
    }
    phantom.exit();
});