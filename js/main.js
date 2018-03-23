
$('document').ready( function() {
    $(".button-collapse").sideNav();
    /*jquery plugin for work with tables*/
});

function renderTable() {

    var table = $('<table>', { "id": "group", "class": "mdl-data-table"}).appendTo('#content');
    var thead = $('<thead>').appendTo(table);
    var tr = $('<tr>').appendTo(thead);
    var name = $('<th>').html("Имя").appendTo(tr);
    var discipline = $('<th>').html("Предмет").appendTo(tr);
    var grade = $('<th>').html("Оценка").appendTo(tr);
    var edit = $('<th>').html("Изменить").appendTo(tr);

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

function addNewGroup() {
    var li = $('<li>', { "id": "inGroup" }).insertBefore("#newGroup");
    var input = $('<input>', {"type": "text", "placeholder": "введите название"}).appendTo(li);

    var newLi = $('<li>').insertBefore("#inGroup");
    var a = $('<a>', { "href": "#", "class": "waves-effect"}).html(input.val()).appendTo(newLi);

};
