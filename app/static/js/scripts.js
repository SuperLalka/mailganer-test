

document.addEventListener("DOMContentLoaded", function () {

    $("form.new-mailing-form").on('submit', newMailingFormProcessing);

});


function newMailingFormProcessing(event) {
    event.preventDefault();

    let sending_time = $(this).find('input[id="datetimepickerInput"]').val();
    let data = {
        'title': $(this).find('input[id="titleInput"]').val(),
        'content': $(this).find('textarea[id="contentTextarea"]').val(),
        'sending_time': null
    };

    if (sending_time) {
        data['sending_time'] = Date.parse(sending_time)/1000;
    }

    $.ajax({
        async: false,
        type: 'POST',
        url: `/api/mailings/`,
        data: data,
        success: function (data) {
            alert('Success');
        }
    });
}
