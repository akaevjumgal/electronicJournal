
$('document').ready( function() {
    /*For mobile version of left side bar*/
    $(".button-collapse").sideNav();

/*Registration form validation*/
    $("#reg_form").validate({
        rules: {
            first_name: {
                required: true
            },
            last_name: {
                required: true
            },
            email: {
                required: true,
                email: true
            },
            pass: {
                required: true,
                minlength: 6
            },
            confirm_password: {
                required: true,
                equalTo: "#password"
            }
        },
        messages: {
            first_name:{
                required: "Заполните поле"
            },
            last_name:{
                required: "Заполните поле"
            },
            email: {
                required: "Заполните поле"
            },
            pass: {
                required: "Заполните поле",
                minlength: "Не менее 6 символов"
            },
            confirm_password: {
                required: "Заполните поле",
                equalTo: "Пароли должны совпадать"
            }
        },
        errorElement: "span"
    });
    /*Authorization form validation*/
    $('#authForm').validate({
        rules: {
            login: {
                required: true
            },
            authPassword: {
                required: true,
                minlength: 6
            }
        },
        messages: {
            login: {
                required: "Заполните поле"
            },
            authPassword: {
                required: "Заполните поле",
                minlength: "Не менее 6 символов"
            }
        },
        errorElement: "span"
    })
});
/*Rendering tables with lesson*/
function renderTable() {

    var table = $('<table>', { "id": "group", "class": "mdl-data-table"}).appendTo('#content');
    var thead = $('<thead>').appendTo(table);
    var tr = $('<tr>').appendTo(thead);
    var name = $('<th>').html("Имя").appendTo(tr);
    var discipline = $('<th>').html("Предмет").appendTo(tr);
    var grade = $('<th>').html("Оценка").appendTo(tr);
    var edit = $('<th>').html("Изменить").appendTo(tr);

/*jquery plugin for work with tables*/
    $('#group').DataTable({
        "ajax": '../arrays.json',
        "language": {
                "url": 'tableLangRus.json'
            }
    });
};
/*Show password button*/
$('#showPassword').click(function(){
  if ($('#password').prop('type') == 'password') {
    $('#password').prop('type', 'text')
} else {
    $('#password').prop('type', 'password')
}
});

// function addNewGroup() {
//     var li = $('<li>', { "id": "inGroup" }).insertBefore("#newGroup");
//     var input = $('<input>', {"type": "text", "placeholder": "введите название"}).appendTo(li);
//
//     var newLi = $('<li>').insertBefore("#inGroup");
//     var a = $('<a>', { "href": "#", "class": "waves-effect"}).html(input.val()).appendTo(newLi);
// };
