"use strict";
var page = require('webpage').create();
var system = require('system');
var args = system.args;

page.onResourceError = function(resourceError) {
    if (/.js/g.test(resourceError.url)) {
        console.log(resourceError.url)
    }
};

page.open(args[1], function (status) {
    if (status !== 'success') {
        console.log('Unable to access network');
    } else {
        page.render('test2.png');
    }
    phantom.exit();
});