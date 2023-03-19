$(document).ready(function () { 
    $('.section-2__body-predict-btn').attr("disabled",'true');
    $('.lds-hourglass').hide();
    $('.output').hide();
   
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('.section-2__body-image-view').css('background-image', 'url(' + e.target.result + ')');
                $('.section-2__body-image-view').hide();
                $('.section-2__body-image-view').fadeIn(600);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#uploadImage").change(function () {
        $('.section-2__body-image-container').show();
        $('.section-2__body-predict-btn').show();
        $('.section-2__body-predict-btn').removeAttr("disabled");
        
        $('.output').text('');
        $('.output').hide();
        readURL(this);
    });

    $('.section-2__body-predict-btn').click(function () {
        var form_data = new FormData($('.section-2__body-predict-form')[0]);
        $(this).hide();
        $('.lds-hourglass').show();
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                $('.lds-hourglass').hide();
                $('.output').fadeIn(590);
                $('.output').text(data)
            },
        });
    });

});
