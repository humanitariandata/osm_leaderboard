var MetaUtil = require('../');

var meta = MetaUtil({
    'delay': 1000,
    'start': '024', //file number
    'end': '024' //file number
}).pipe(process.stdout) //outputs to console
