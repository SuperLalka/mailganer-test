

document.addEventListener("DOMContentLoaded", function () {

    $("form.new-mailing-form").on('submit', newMailingFormProcessing);

});


function newMailingFormProcessing(event) {
    event.preventDefault();

    let sending_time = $(this).find('input[id="datetimepickerInput"]').val();
    let data = {
        'title': $(this).find('input[id="titleInput"]').val(),
        'content': $(this).find('textarea[id="contentTextarea"]').val(),
        'recipients': $(this).find('select[id="recipientsSelect"]').val(),
        'sending_time': null,
    };

    if (sending_time) {
        data['sending_time'] = sending_time;
    }

    $.ajax({
        async: false,
        type: 'POST',
        url: `/api/mailings/`,
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (data) {
            clearModal();
            alert('Успешно создано');
        }
    });
}


function clearModal() {
    $('.modal').find('input').val('');
    $('.modal').find('textarea').val('');
    $('.modal').find('option').removeAttr("selected");
    $('#newMailingModal').modal('hide');
}
