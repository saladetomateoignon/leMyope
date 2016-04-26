var casper = require('casper').create({
     pageSettings: {userAgent: 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'}
 });
// Retrieve ftp file URL
var ftpUrl = casper.cli.raw.get(0);
casper.start(ftpUrl, function() {
    this.echo(this.getCurrentUrl());
    this.capture('google1.png', {
    top: 0,
    left: 0,
    width: 1000,
    height: 1000
    });
});

casper.then(function() {
    this.echo(this.getCurrentUrl());
    // New layout tiles page
    if (this.resourceExists('a[class="r-search-5 bia uh_rl"]')) {
        this.echo('New layout tiles page!');
        this.click('a[class="r-search-5 bia uh_rl"]');
        this.echo(this.getHTML('div[data-ri="0"]'));
        // New layout single photo page
        if (this.resourceExists('a[class="irc_fsl irc_but"]')) {
            this.echo('New layout single photo page!');
            this.click('a[class="irc_fsl irc_but"]');
            this.echo(this.getCurrentUrl());
        }
        // other layout single photo page
        else {
            this.echo('Something else?');
            this.echo(this.getCurrentUrl());
        }
    // Old layout tiles page
    }
    else {
        this.echo('Old Layout tiles page');
        this.echo('-----------------');
        this.echo(this.getHTML('a[class="bia uh_rl"]',true));
        this.echo('-----------------');
        var completeURL = this.getHTML('a[class="bia uh_rl"]',true);
        var rx = new RegExp("(imgurl=http|imgurl=https):\\/\\/[\\w\\-_]+(\\.[\\w\\-_]+)+([\\w\\-\\.,@?^=%&amp:!/~\\+#]*[\\w\\-\\@?^%=&amp;/~\\+#])?");
        var arr = rx.exec(completeURL);
        this.echo(arr);
        var fs = require('fs');
        fs.write('htmlblurb.txt', arr, 'w');
    }
});

casper.run();
