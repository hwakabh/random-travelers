function sample(){
    document.getElementById("output").innerHTML = "<img src='./img/america.png' width='150ps'>";
    document.getElementById("output").append("Americas");
}

function gacha(){
    $.ajax({
        type: 'GET',
        url: 'http://localhost/random-travelers/python/sample.py',
        async: false
    })
    .done(function(result) {
        document.getElementById("output").innerHTML = "<img src='./img/america.png' width='150ps'>";
        document.getElementById("output").append(result);
    }).fail(function(){
        document.getElementById("output").innerHTML = "fail";
    });
}

