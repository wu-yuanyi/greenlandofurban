function warpTable(c) {
    return "<table><thead><tr><th>Place</th><th>Val</th></tr></thead><tbody>"+ c +"</tbody></table>";
}

function parseUrl(obj) {
    var tempArr = [];
    for (var key in obj) {
        if (obj.hasOwnProperty(key)) {
            var str = key + '=' + encodeURIComponent(obj[key]);
            tempArr.push(str);
        }
    }
    return tempArr.join('&');        
}

function getTr(k, v) {
    return "<tr><td>" + k + "</td><td>" + v + "</td></tr>";
}

function sb2() {
    var f = document.getElementById("args");
    var name, e, val;
    var url = 'http://127.0.0.1:8080/query?';
    var args = {};
    for(var i=0;i<f.length;i++)
    {
        name = f[i].name;
        e = document.getElementById(name);
        if (name == 'tree') {
            val = e.value;
            if (val.length === 0) {
                val = 'conandbro';
            }
        } else {
            val = parseFloat(e.value);
            if(Number.isNaN(val)) {
                val = 0;
            }
        }
        //console.log(name + ':'  + typeof(val));
        args[name] = val;
    }
    url += parseUrl(args);
    console.log(url);

    $.ajax({
        url: url,
        // crossDomain: true,
        type:"GET",
        //contentType: "application/json; charset=utf-8",
        dataType:'jsonp',
        timeout: 10000,
        success: function(res) {
            //var objs = JSON.parse(res);
            var objs = res.data;
            var table;
            var content = "";
            var tables = "";
            var len = objs.length;
            for (var i=0; i<len; i++) {
                table = objs[i];
                content = "";
                for(var k in table) {
                    if (table.hasOwnProperty(k)) {
                        content += getTr(k, table[k]);
                    }
                }
                tables += warpTable(content);
            }
            $("#table-place").html(tables);
        }
    }).fail(function(e) {
        console.log(e);
  });

}
(function() {
    $(document).ready(function() {
        /*
        var objs = 
[{"\u51c9\u57ce\u65b0\u6751\u8857\u9053": 1.0, "\u5e7f\u4e2d\u8def\u8857\u9053": 0.7518103037061163, "\u5609\u5174\u8def\u8857\u9053": 0.0, "\u63d0\u7bee\u6865\u8857\u9053": 0.17229516041800336, "\u6c5f\u6e7e\u9547\u8857\u9053": 0.9989197076312212, "\u56db\u5ddd\u5317\u8def\u8857\u9053": 0.15532464607693627, "\u66f2\u9633\u8def\u8857\u9053": 0.8408886103087683, "\u6b27\u9633\u8def\u8857\u9053": 0.7185472000645556}, {"\u51c9\u57ce\u65b0\u6751\u8857\u9053": 0.10672445409253502, "\u5e7f\u4e2d\u8def\u8857\u9053": 0.6774734322557597, "\u5609\u5174\u8def\u8857\u9053": 0.5334260359371813, "\u63d0\u7bee\u6865\u8857\u9053": 0.7864962532360191, "\u6c5f\u6e7e\u9547\u8857\u9053": 0.0, "\u56db\u5ddd\u5317\u8def\u8857\u9053": 0.5602389417710759, "\u66f2\u9633\u8def\u8857\u9053": 0.5921347769362443, "\u6b27\u9633\u8def\u8857\u9053": 1.0}, {"\u51c9\u57ce\u65b0\u6751\u8857\u9053": 0.28071988833830414, "\u5e7f\u4e2d\u8def\u8857\u9053": 0.3662851813663574, "\u5609\u5174\u8def\u8857\u9053": 0.021964193650826126, "\u63d0\u7bee\u6865\u8857\u9053": 0.0, "\u6c5f\u6e7e\u9547\u8857\u9053": 0.16297485576583068, "\u6b27\u9633\u8def\u8857\u9053": 1.0, "\u56db\u5ddd\u5317\u8def\u8857\u9053": 0.20445950327124623, "\u66f2\u9633\u8def\u8857\u9053": 0.2547576488213248}, {"\u51c9\u57ce\u65b0\u6751\u8857\u9053": 0.5423326178661172, "\u5e7f\u4e2d\u8def\u8857\u9053": 0.5671734679356714, "\u5609\u5174\u8def\u8857\u9053": 0.08989779253344896, "\u63d0\u7bee\u6865\u8857\u9053": 0.18689250215260422, "\u6c5f\u6e7e\u9547\u8857\u9053": 0.4729065681471122, "\u56db\u5ddd\u5317\u8def\u8857\u9053": 0.23817247616849668, "\u66f2\u9633\u8def\u8857\u9053": 0.53981660263354, "\u6b27\u9633\u8def\u8857\u9053": 0.8874188800258223}];
         var table;
            var content = "";
            var tables = "";
            var len = objs.length;
            for (var i=0; i<len; i++) {
                table = objs[i];
                content = "";
                for(var k in table) {
                    if (table.hasOwnProperty(k)) {
                        content += getTr(k, table[k]);
                    }
                }
                tables += warpTable(content);
            }
            console.log(tables);
         $("#table-place").html(tables); */
    });
})();
