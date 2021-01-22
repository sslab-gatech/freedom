gc = '''
function gc() {
    for(var i=0;i<100;i++) {
        a = new Uint8Array(1024*1024);
    }
}'''

do_nothing = '''
function doNothing() {}
'''