function func() {
    var x = document.getElementById('mon')    
    var a = document.getElementById('tue')
    var b = document.getElementById('wed')
    var c = document.getElementById('thur')
    var d = document.getElementById('fri')
    var mon_dis = document.getElementById('monday')
    var tue_dis = document.getElementById('tuesday')
    var wed_dis = document.getElementById('wednesday')
    var thur_dis = document.getElementById('thursday')
    var fri_dis = document.getElementById('friday')

    x.src = "../static/images/mon_yellow.png"
    a.src = "../static/images/tue_white.png"
    b.src = "../static/images/wed_white.png"
    c.src = "../static/images/thur_white.png"
    d.src = "../static/images/fri_white.png"

    mon_dis.style.display='block'
    tue_dis.style.display='none'
    wed_dis.style.display='none'
    thur_dis.style.display='none'
    fri_dis.style.display='none'
}
function tue() {
    var x = document.getElementById('tue')
    var a = document.getElementById('mon')
    var b = document.getElementById('wed')
    var c = document.getElementById('thur')
    var d = document.getElementById('fri')

    var mon_dis = document.getElementById('monday')
    var tue_dis = document.getElementById('tuesday')
    var wed_dis = document.getElementById('wednesday')
    var thur_dis = document.getElementById('thursday')
    var fri_dis = document.getElementById('friday')

    x.src = "../static/images/tue_yellow.png"
    a.src = "../static/images/mon_white.png"
    b.src = "../static/images/wed_white.png"
    c.src = "../static/images/thur_white.png"
    d.src = "../static/images/fri_white.png"

    mon_dis.style.display='none'
    tue_dis.style.display='block'
    wed_dis.style.display='none'
    thur_dis.style.display='none'
    fri_dis.style.display='none'
}
function wed() {
    var x = document.getElementById('wed')
    var a = document.getElementById('mon')
    var b = document.getElementById('tue')
    var c = document.getElementById('thur')
    var d = document.getElementById('fri')

    var mon_dis = document.getElementById('monday')
    var tue_dis = document.getElementById('tuesday')
    var wed_dis = document.getElementById('wednesday')
    var thur_dis = document.getElementById('thursday')
    var fri_dis = document.getElementById('friday')

    x.src = "../static/images/wed_yellow.png"
    a.src = "../static/images/mon_white.png"
    b.src = "../static/images/tue_white.png"
    c.src = "../static/images/thur_white.png"
    d.src = "../static/images/fri_white.png"

    mon_dis.style.display='none'
    tue_dis.style.display='none'
    wed_dis.style.display='block'
    thur_dis.style.display='none'
    fri_dis.style.display='none'
}
function thur() {
    var x = document.getElementById('thur')
    var a = document.getElementById('mon')
    var b = document.getElementById('tue')
    var c = document.getElementById('wed')
    var d = document.getElementById('fri')

    var mon_dis = document.getElementById('monday')
    var tue_dis = document.getElementById('tuesday')
    var wed_dis = document.getElementById('wednesday')
    var thur_dis = document.getElementById('thursday')
    var fri_dis = document.getElementById('friday')

    x.src = "../static/images/thur_yellow.png"
    a.src = "../static/images/mon_white.png"
    b.src = "../static/images/tue_white.png"
    c.src = "../static/images/wed_white.png"
    d.src = "../static/images/fri_white.png"

    mon_dis.style.display='none'
    tue_dis.style.display='none'
    wed_dis.style.display='none'
    thur_dis.style.display='block'
    fri_dis.style.display='none'
}
function fri() {
    var x = document.getElementById('fri')
    var a = document.getElementById('mon')
    var b = document.getElementById('tue')
    var c = document.getElementById('wed')
    var d = document.getElementById('thur')

    var mon_dis = document.getElementById('monday')
    var tue_dis = document.getElementById('tuesday')
    var wed_dis = document.getElementById('wednesday')
    var thur_dis = document.getElementById('thursday')
    var fri_dis = document.getElementById('friday')

    x.src = "../static/images/fri_yellow.png"
    a.src = "../static/images/mon_white.png"
    b.src = "../static/images/tue_white.png"
    c.src = "../static/images/wed_white.png"
    d.src = "../static/images/thur_white.png"
    
    mon_dis.style.display='none'
    tue_dis.style.display='none'
    wed_dis.style.display='none'
    thur_dis.style.display='none'
    fri_dis.style.display='block'
}

function cir_th() {

    var a = document.getElementById('cir_thur')
    var b = document.getElementById('cir_fri')
    //var x = document.getElementById('bg_thur')

    a.src = "../static/images/thur_circle.png"
    b.src = "../static/images/fri.png"

    //x.src = "../static/images/bg_thur.png"

}
function cir_fri() {

    var a = document.getElementById('cir_thur')
    var b = document.getElementById('cir_fri')
    //var x = document.getElementById('bg_thur')

    a.src = "../static/images/thur.png"
    b.src = "../static/images/fri_circle.png"
    //x.src = "../static/images/bg_fri.png"
}