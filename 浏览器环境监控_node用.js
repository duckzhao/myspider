window = new Proxy(global,{
    get: function(target, key, receiver) {
        console.log("window.get", key, target[key]);
        if (key == "location") {
            location = new Proxy(target[key],{
                get: function(_target, _key, _receiver) {
                    console.log("window.get", key, _key, _target[_key]);
                    if (_key == "port") {
                        console.log("111")
                    }
                    return _target[_key];
                }
            })
        }
        return target[key];
    },
    set: function(target, key, value, receiver) {
        console.log("window.set", key, value);
        target[key] = value;
    }
});



/* 
输入
window.a = {}
window.a;
window.b = {a:2};
window.b.a;

输出
window.set a {}
window.get a {}
window.set b { a: 2 }
window.get b { a: 2 }
*/
