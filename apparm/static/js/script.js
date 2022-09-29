/* ------------------------------------------------
 # all the scrips here it will extends to all pages

--------------------------------------------------*/
//1) script to validade all imput
function validateEmail(email){
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validateAll(){

    var nombre = $("#nombre").val();
    var telefono = $("#telefono").val();
    var email = $("#email").val();
    var direccion = $("#direccion").val();
    var rrss = $("#rrss").val();
    
    if (nombre == ''){
        swal("Opps !", "El campo nombre no debe estar vacio", "error");
        return false;
    }
    else if (nombre.split(' ').length < 2 ){
        swal("Opps !", "El apellido es requerido", "info");
        return false;
    }
    else if (telefono == ''){
        swal("Opps !", "El campo telefono no debe estar vacio", "error");
        return false;
    }
    else if (email == ''){
        swal("Opps !", "El campo email no debe estar vacio", "error");
        return false;
    }
    else if (!(validateEmail(email))){
        swal("Opps !", "Poner una dirección de correo electrónico válida", "error");
        return false;
    }
    else if (direccion == ''){
        swal("Opps !", "El campo direccion no debe estar vacio", "error");
        return false;
    }
    else if (rrss == ''){
        swal("Opps !", "El campo rrss no debe estar vacio", "error");
        return false;
    }
    else{
        return true;
    }

}

$(".btn-add").bind("click", validateAll);

// 2) Scripts (nombre field) only letter validate

$(document).ready(function(){
    //only letter
    jQuery('input[name="nombre').keyup(function(){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '' );
        jQuery(this).val(allow);
    });
    // prevent starting whit space
    $("input").on("keypress", function(e){
        if (e.which === 32 && ! this.value.length)
        e.preventDefault();
    });
});

// 3) Script to put First letter captalized

$("#nombre").keyup(function(){
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){return $1.toUpperCase( );}) );
});

// 4) Scripts to lowercase input email

$(document).ready(function(){
    $('#email').keyup(function(){
        this.value = this.value.toLowerCase();

    });
});

// 5)mask telefono
$(document).ready(function(){
    $("#telefono").inputmask("(99) 9999-9999", {"onincomplete":function() {
        $("#telefono").val("");
        swal("Opss !", "Complete telefono.", "error");
        return false;
        }
    });
});

// 6 ) time running al real time

setInterval(function(){
    var date = new Date();
    $("#clock").html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()

    );
}, 500);

// 7) if  not provee show message
var verify = $("#chk_td").length;
    if (verify == 0){
        $("#no-data").text("No se encontraron proveedores");
    };

// 8) close offcanvas when a button is clicked
$(document).ready(function(){
    jQuery("#offcanvasRight, .offcanvas-body a").click(function(){
        console.log($(this).attr('href'));
        jQuery('.offcanvas').offcanvas('hide');
    });
});