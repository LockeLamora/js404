var page = require('webpage').create();
var args = require('system').args;

page.onResourceError = function(resourceError) {
    if (/.js/g.test(resourceError.url)) {
        console.log(resourceError.url);
    }
};

page.onError = function(msg, trace) {
    system.stderr.writeLine('= onError()');
    var msgStack = ['  ERROR: ' + msg];
    if (trace) {
        msgStack.push('  TRACE:');
        trace.forEach(function(t) {
            msgStack.push('    -> ' + t.file + ': ' + t.line + (t.function ? ' (in function "' + t.function + '")' : ''));
        });
    }
    system.stderr.writeLine(msgStack.join('\n'));
};

page.open(args[1], function (status) {
    if (status == 'success') {
       //page.render('test2.png');
    }
    phantom.exit();
});