/**
 * Created by cj on 11/28/16.
 */
function getMessages(url){
    $.get({
        url: url,
        success: function(data, status, jqXHR ) { $('#message-area').html(data); }
    });
}

function postMessage(url, body, csrfmiddlewaretoken) {
    $.post({
        url: url,
        data: { body: body, csrfmiddlewaretoken: csrfmiddlewaretoken },
        success: function (data, status, jqXHR) { getMessages(url); }
    });
}

$('#user-list li a').on('click', function (e) {
    e.preventDefault();
    $('#user-list li .active').removeClass('active');
    $(this).parent().addClass('active');
    url = $(this).attr('href');
    getMessages(url);
});

$('#message-area').on('submit', 'form', function (e) {
    e.preventDefault();
    url = $(this).attr('action');
    body = $(this).find('input[name="body"]').val();
    csrfmiddlewaretoken = $(this).find('input[name="csrfmiddlewaretoken"]').val();
    postMessage(url, body, csrfmiddlewaretoken);
})
