var system = require('system');
var args = system.args;

var page = require('webpage').create();

page.onConsoleMessage = function(msg) { 
    console.log('in console mesage');
    console.log(msg); 
 }; 

 page.onResourceError = function(resourceError) {
    console.error(resourceError.url + ': ' + resourceError.errorString);
};

page.onResourceRequested = function (request) {
    system.stderr.writeLine('= onResourceRequested()');
    system.stderr.writeLine('  request: ' + JSON.stringify(request, undefined, 4));
};
 
page.onResourceReceived = function(response) {
    system.stderr.writeLine('= onResourceReceived()' );
    system.stderr.writeLine('  id: ' + response.id + ', stage: "' + response.stage + '", response: ' + JSON.stringify(response));
};
 
page.onLoadStarted = function() {
    system.stderr.writeLine('= onLoadStarted()');
    var currentUrl = page.evaluate(function() {
        return window.location.href;
    });
    system.stderr.writeLine('  leaving url: ' + currentUrl);
};
 
page.onLoadFinished = function(status) {
    system.stderr.writeLine('= onLoadFinished()');
    system.stderr.writeLine('  status: ' + status);
};
 
page.onNavigationRequested = function(url, type, willNavigate, main) {
    system.stderr.writeLine('= onNavigationRequested');
    system.stderr.writeLine('  destination_url: ' + url);
    system.stderr.writeLine('  type (cause): ' + type);
    system.stderr.writeLine('  will navigate: ' + willNavigate);
    system.stderr.writeLine('  from page\'s main frame: ' + main);
};

if (args.length === 1) {
  console.log('URL required');
} 

else {
    args.forEach(function(arg) {
        console.log(arg);
        page.open(arg, function(status) {
            console.log(status);
            page.render('screenshot.jpeg', {format: 'jpeg', quality: '100'});
        });
    });
}

phantom.exit();